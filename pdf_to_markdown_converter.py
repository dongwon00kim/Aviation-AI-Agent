#!/usr/bin/env python3
"""
Enhanced PDF to Markdown Converter for Aviation Documents
Converts both airplane manuals and AIP documents to markdown format.
"""

import os
import logging
import re
from pathlib import Path
from typing import List, Optional
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import PdfFormatOption

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AviationPDFConverter:
    """Enhanced PDF to Markdown converter for aviation documents."""

    def __init__(self, base_dir: str = "./airplane_data"):
        self.base_dir = Path(base_dir)
        self.pdf_dir = self.base_dir / "pdf"
        self.aip_dir = self.base_dir / "aip"
        self.output_dir = self.base_dir / "md"

        # Setup converter with optimized options
        self.pipeline_options = PdfPipelineOptions(
            do_ocr=False,
            do_table_structure=True,
            table_structure_options={
                "do_cell_matching": True,
            }
        )

        format_options = {
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=self.pipeline_options
            )
        }

        self.converter = DocumentConverter(
            format_options=format_options
        )

        # Create output directories
        self._create_output_dirs()

    def _create_output_dirs(self):
        """Create necessary output directories."""
        directories = [
            self.output_dir,
            self.output_dir / "manuals",
            self.output_dir / "aip",
        ]

        for dir_path in directories:
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {dir_path}")

    def _clean_image_placeholders(self, content: str) -> str:
        """이미지 관련 텍스트를 완전히 제거합니다."""
        # 다양한 이미지 플레이스홀더 패턴 제거
        patterns_to_remove = [
            r'\[IMAGE_REMOVED\]',  # [IMAGE_REMOVED] 제거
            r'\[IMAGE\]',          # [IMAGE] 제거
            r'\[img\]',            # [img] 제거 (대소문자 구분없이)
            r'!\[.*?\]\(.*?\)',    # ![alt](url) 마크다운 이미지 제거
            r'<img.*?>',           # HTML img 태그 제거
            r'\[image:.*?\]',      # [image:...] 제거
            r'Figure \d+\..*?\n',  # Figure 1. ... 제거
            r'Fig\. \d+\..*?\n',   # Fig. 1. ... 제거
        ]
        
        cleaned_content = content
        for pattern in patterns_to_remove:
            cleaned_content = re.sub(pattern, '', cleaned_content, flags=re.IGNORECASE)
        
        # 연속된 빈 줄을 최대 2개로 제한
        cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
        
        # 앞뒤 공백 제거
        cleaned_content = cleaned_content.strip()
        
        return cleaned_content

    def _get_pdf_files(self, directory: Path) -> List[Path]:
        """Get all PDF files from a directory."""
        if not directory.exists():
            logger.warning(f"Directory does not exist: {directory}")
            return []

        pdf_files = list(directory.glob("**/*.pdf"))
        logger.info(f"Found {len(pdf_files)} PDF files in {directory}")
        return pdf_files

    def _convert_pdf_to_markdown(self, pdf_path: Path, output_path: Path) -> bool:
        """Convert a single PDF file to markdown."""
        try:
            logger.info(f"Converting: {pdf_path.name}")

            # Convert PDF to document
            result = self.converter.convert(str(pdf_path))

            # Get markdown content without images
            markdown_content = result.document.export_to_markdown(
                image_placeholder=""  # 이미지 위치에 아무것도 표시하지 않음
            )
            
            # 이미지 관련 텍스트 완전 제거
            markdown_content = self._clean_image_placeholders(markdown_content)

            # Write markdown file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {pdf_path.stem}\n\n")
                f.write(f"**Source:** {pdf_path.name}\n\n")
                f.write(f"**Converted:** Aviation Document Processing System\n\n")
                f.write("---\n\n")
                f.write(markdown_content)

            logger.info(f"Successfully converted: {pdf_path.name} -> {output_path.name}")
            return True

        except Exception as e:
            logger.error(f"Failed to convert {pdf_path.name}: {str(e)}")
            return False

    def convert_airplane_manuals(self) -> int:
        """Convert airplane manual PDFs to markdown."""
        logger.info("Starting conversion of airplane manuals...")

        pdf_files = self._get_pdf_files(self.pdf_dir)
        success_count = 0

        for pdf_file in pdf_files:
            # Create relative path structure in output
            relative_path = pdf_file.relative_to(self.pdf_dir)
            output_path = self.output_dir / "manuals" / relative_path.with_suffix('.md')

            # Create subdirectories if needed
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if self._convert_pdf_to_markdown(pdf_file, output_path):
                success_count += 1

        logger.info(f"Converted {success_count}/{len(pdf_files)} airplane manuals")
        return success_count

    def convert_aip_documents(self) -> int:
        """Convert AIP PDFs to markdown."""
        logger.info("Starting conversion of AIP documents...")

        pdf_files = self._get_pdf_files(self.aip_dir)
        success_count = 0

        for pdf_file in pdf_files:
            # Create relative path structure in output
            relative_path = pdf_file.relative_to(self.aip_dir)
            output_path = self.output_dir / "aip" / relative_path.with_suffix('.md')

            # Create subdirectories if needed
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if self._convert_pdf_to_markdown(pdf_file, output_path):
                success_count += 1

        logger.info(f"Converted {success_count}/{len(pdf_files)} AIP documents")
        return success_count

    def convert_all(self) -> dict:
        """Convert all PDF documents."""
        logger.info("Starting conversion of all aviation documents...")

        results = {
            'manuals': self.convert_airplane_manuals(),
            'aip': self.convert_aip_documents(),
            'total_files': 0,
            'success_files': 0
        }

        total_pdfs = len(self._get_pdf_files(self.pdf_dir)) + len(self._get_pdf_files(self.aip_dir))
        total_success = results['manuals'] + results['aip']

        results['total_files'] = total_pdfs
        results['success_files'] = total_success

        logger.info(f"Conversion complete: {total_success}/{total_pdfs} files converted successfully")
        return results

    def list_converted_files(self) -> dict:
        """List all converted markdown files."""
        manual_files = list((self.output_dir / "manuals").glob("**/*.md"))
        aip_files = list((self.output_dir / "aip").glob("**/*.md"))

        return {
            'manuals': [str(f.relative_to(self.output_dir)) for f in manual_files],
            'aip': [str(f.relative_to(self.output_dir)) for f in aip_files],
            'total_count': len(manual_files) + len(aip_files)
        }


def main():
    """Main function to run the converter."""
    converter = AviationPDFConverter()

    # Convert all documents
    results = converter.convert_all()

    print("\n" + "="*50)
    print("AVIATION PDF TO MARKDOWN CONVERSION RESULTS")
    print("="*50)
    print(f"Airplane Manuals Converted: {results['manuals']}")
    print(f"AIP Documents Converted: {results['aip']}")
    print(f"Total Success: {results['success_files']}/{results['total_files']}")

    # List converted files
    converted_files = converter.list_converted_files()
    print(f"\nTotal Markdown Files Created: {converted_files['total_count']}")

    if converted_files['manuals']:
        print("\nAirplane Manual Files:")
        for file in converted_files['manuals']:
        # for file in converted_files['manuals'][:5]:  # Show first 5
            print(f"  - {file}")
        if len(converted_files['manuals']) > 5:
            print(f"  ... and {len(converted_files['manuals']) - 5} more")

    if converted_files['aip']:
        print("\nAIP Document Files:")
        # for file in converted_files['aip'][:5]:  # Show first 5
        for file in converted_files['aip']:
            print(f"  - {file}")
        if len(converted_files['aip']) > 5:
            print(f"  ... and {len(converted_files['aip']) - 5} more")

    print("\nMarkdown files are ready for vector database embedding!")


if __name__ == "__main__":
    main()