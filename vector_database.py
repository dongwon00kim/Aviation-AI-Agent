#!/usr/bin/env python3
"""
Vector Database System for Aviation Documents
Creates embeddings for markdown documents and stores them in Chroma vector database.
"""

import os
import json
import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import re
from dataclasses import dataclass

import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.docstore.document import Document
from langchain_core.documents import Document as CoreDocument

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class DocumentSection:
    """Represents a document section with metadata."""
    content: str
    title: str
    source_file: str
    section_type: str
    page_number: Optional[int] = None

class AviationVectorDatabase:
    """Vector database system for aviation documents."""

    def __init__(self,
                 markdown_dir: str = "./airplane_data/md",
                 vector_store_path: str = "./vectorstore/aviation_chroma",
                 embedding_model: str = "intfloat/multilingual-e5-large"):

        self.markdown_dir = Path(markdown_dir)
        self.vector_store_path = Path(vector_store_path)
        self.embedding_model_name = embedding_model

        # Initialize embeddings with multilingual support
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        # Text splitter for section-based chunking
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=[
                "\n# ",      # Main headers
                "\n## ",     # Sub headers
                "\n### ",    # Sub-sub headers
                "\n#### ",   # Smaller headers
                # "\n\n",      # Paragraphs
                # "\n",        # Lines
                # " ",         # Words
                ""           # Characters
            ],
            keep_separator=True
        )

        self.vector_store = None

        # Create vector store directory
        self.vector_store_path.mkdir(parents=True, exist_ok=True)

    def _extract_sections_from_markdown(self, content: str, source_file: str) -> List[DocumentSection]:
        """Extract sections from markdown content."""
        sections = []

        # Split by main headers (# and ##)
        header_pattern = r'^(#{1,4})\s+(.+)$'
        lines = content.split('\n')

        current_section = ""
        current_title = "Introduction"
        current_level = 0

        for line in lines:
            header_match = re.match(header_pattern, line)

            if header_match:
                # Save previous section if it has content
                if current_section.strip():
                    sections.append(DocumentSection(
                        content=current_section.strip(),
                        title=current_title,
                        source_file=source_file,
                        section_type=self._determine_section_type(current_title)
                    ))

                # Start new section
                level = len(header_match.group(1))
                current_title = header_match.group(2).strip()
                current_level = level
                current_section = line + '\n'
            else:
                current_section += line + '\n'

        # Don't forget the last section
        if current_section.strip():
            sections.append(DocumentSection(
                content=current_section.strip(),
                title=current_title,
                source_file=source_file,
                section_type=self._determine_section_type(current_title)
            ))

        return sections

    def _determine_section_type(self, title: str) -> str:
        """Determine section type based on title keywords."""
        title_lower = title.lower()

        # Aviation-specific section types
        if any(keyword in title_lower for keyword in ['star', 'arrival', 'approach']):
            return 'STAR'
        elif any(keyword in title_lower for keyword in ['ils', 'instrument', 'landing']):
            return 'ILS'
        elif any(keyword in title_lower for keyword in ['atc', 'control', 'frequency', 'radio']):
            return 'ATC'
        elif any(keyword in title_lower for keyword in ['airport', 'runway', 'taxiway']):
            return 'AIRPORT'
        elif any(keyword in title_lower for keyword in ['navigation', 'nav', 'gps']):
            return 'NAVIGATION'
        elif any(keyword in title_lower for keyword in ['emergency', 'malfunction', 'failure']):
            return 'EMERGENCY'
        elif any(keyword in title_lower for keyword in ['checklist', 'procedure', 'operations']):
            return 'PROCEDURES'
        elif any(keyword in title_lower for keyword in ['boeing', 'airbus', 'aircraft', 'system']):
            return 'AIRCRAFT_SYSTEMS'
        else:
            return 'GENERAL'

    def _load_markdown_files(self) -> List[Tuple[str, str]]:
        """Load all markdown files and return (content, file_path) tuples."""
        markdown_files = []

        for md_file in self.markdown_dir.glob("**/*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    markdown_files.append((content, str(md_file)))
                logger.info(f"Loaded: {md_file.name}")
            except Exception as e:
                logger.error(f"Failed to load {md_file}: {str(e)}")

        logger.info(f"Loaded {len(markdown_files)} markdown files")
        return markdown_files

    def create_embeddings(self, force_rebuild: bool = False) -> int:
        """Create embeddings for all markdown documents."""

        # Check if vector store already exists
        if self.vector_store_path.exists() and not force_rebuild:
            logger.info("Vector store already exists. Use force_rebuild=True to recreate.")
            return 0

        logger.info("Creating embeddings for aviation documents...")

        # Load all markdown files
        markdown_files = self._load_markdown_files()

        if not markdown_files:
            logger.error("No markdown files found!")
            return 0

        # Extract sections and create documents
        all_documents = []
        section_count = 0

        for content, file_path in markdown_files:
            sections = self._extract_sections_from_markdown(content, file_path)

            for section in sections:
                # Create LangChain Document with metadata
                doc = CoreDocument(
                    page_content=section.content,
                    metadata={
                        'source': section.source_file,
                        'title': section.title,
                        'section_type': section.section_type,
                        'file_type': 'aip' if '/aip/' in section.source_file else 'manual'
                    }
                )
                all_documents.append(doc)
                section_count += 1

        logger.info(f"Created {section_count} document sections from {len(markdown_files)} files")

        # Split documents further if needed
        final_documents = self.text_splitter.split_documents(all_documents)
        logger.info(f"Split into {len(final_documents)} final chunks")

        # Create vector store with Chroma
        if final_documents:
            self.vector_store = Chroma.from_documents(
                documents=final_documents,
                embedding=self.embeddings,
                persist_directory=str(self.vector_store_path),
                collection_name="aviation_documents"
            )

            logger.info(f"Chroma vector store created at: {self.vector_store_path}")

            # Save metadata
            self._save_metadata(len(final_documents), len(markdown_files))

            return len(final_documents)
        else:
            logger.error("No documents to embed!")
            return 0

    def _save_metadata(self, doc_count: int, file_count: int):
        """Save metadata about the vector store."""
        metadata = {
            'embedding_model': self.embedding_model_name,
            'document_count': doc_count,
            'file_count': file_count,
            'chunk_size': self.text_splitter._chunk_size,
            'chunk_overlap': self.text_splitter._chunk_overlap,
            'created_at': str(np.datetime64('now'))
        }

        with open(self.vector_store_path / 'metadata.json', 'w') as f:
            json.dump(metadata, f, indent=2)

    def load_vector_store(self) -> bool:
        """Load existing vector store."""
        try:
            if not self.vector_store_path.exists():
                logger.error(f"Vector store not found at: {self.vector_store_path}")
                return False

            self.vector_store = Chroma(
                persist_directory=str(self.vector_store_path),
                embedding_function=self.embeddings,
                collection_name="aviation_documents"
            )

            logger.info("Chroma vector store loaded successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to load Chroma vector store: {str(e)}")
            return False

    def search_documents(self,
                        query: str,
                        k: int = 5,
                        section_types: Optional[List[str]] = None,
                        file_types: Optional[List[str]] = None) -> List[Dict]:
        """Search documents using similarity search."""

        if not self.vector_store:
            if not self.load_vector_store():
                return []

        # Perform similarity search
        docs = self.vector_store.similarity_search(query, k=k*2)  # Get more for filtering

        results = []
        for doc in docs:
            metadata = doc.metadata

            # Apply filters
            if section_types and metadata.get('section_type') not in section_types:
                continue
            if file_types and metadata.get('file_type') not in file_types:
                continue

            results.append({
                'content': doc.page_content,
                'metadata': metadata,
                'source': metadata.get('source', 'Unknown'),
                'title': metadata.get('title', 'Untitled'),
                'section_type': metadata.get('section_type', 'GENERAL')
            })

            if len(results) >= k:
                break

        return results

    def search_aviation_info(self,
                           aircraft_type: str,
                           airport_codes: List[str],
                           info_types: List[str] = None) -> Dict[str, List[Dict]]:
        """
        Search for specific aviation information.

        Args:
            aircraft_type: e.g., "Boeing 737", "Airbus A320"
            airport_codes: e.g., ["RKSI", "RKSS", "RKPC"]
            info_types: e.g., ["STAR", "ILS", "ATC"]
        """

        if info_types is None:
            info_types = ["STAR", "ILS", "ATC", "AIRPORT"]

        results = {}

        for info_type in info_types:
            # Create search query
            query_parts = [aircraft_type]
            query_parts.extend(airport_codes)
            query_parts.append(info_type.lower())

            query = " ".join(query_parts)

            # Search documents
            docs = self.search_documents(
                query=query,
                k=3,
                section_types=[info_type]
            )

            results[info_type] = docs

        return results

    def get_statistics(self) -> Dict:
        """Get statistics about the vector database."""
        if not self.vector_store:
            if not self.load_vector_store():
                return {}

        # Try to load metadata
        metadata_file = self.vector_store_path / 'metadata.json'
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
        else:
            metadata = {}

        # Get vector store info for Chroma
        try:
            collection = self.vector_store._collection
            total_docs = collection.count() if collection else 0
        except:
            total_docs = 0

        stats = {
            'total_documents': total_docs,
            'vector_store_type': 'Chroma',
            **metadata
        }

        return stats


def main():
    """Main function to create the vector database."""

    db = AviationVectorDatabase()

    print("="*60)
    print("AVIATION CHROMA VECTOR DATABASE CREATION")
    print("="*60)

    # Create embeddings
    doc_count = db.create_embeddings(force_rebuild=True)

    if doc_count > 0:
        print(f"✅ Successfully created vector database with {doc_count} document chunks")

        # Test the database
        print("\n" + "="*40)
        print("TESTING DATABASE")
        print("="*40)

        # Test searches
        test_queries = [
            "Boeing 737 landing procedures",
            "RKSI airport STAR procedures",
            "ILS approach frequencies",
            "ATC communication Seoul"
        ]

        for query in test_queries:
            results = db.search_documents(query, k=2)
            print(f"\nQuery: '{query}'")
            print(f"Results: {len(results)} documents found")

            for i, result in enumerate(results[:2]):
                print(f"  {i+1}. {result['title']} ({result['section_type']})")

        # Display statistics
        stats = db.get_statistics()
        print(f"\n" + "="*40)
        print("DATABASE STATISTICS")
        print("="*40)
        for key, value in stats.items():
            print(f"{key}: {value}")

    else:
        print("❌ Failed to create vector database")


if __name__ == "__main__":
    main()