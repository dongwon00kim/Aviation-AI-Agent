#!/usr/bin/env python3
"""
Aviation Q&A System with LangGraph Agent and Memory
항공 전문가 AI 시스템 - LangGraph 에이전트 및 단기/장기 메모리 통합 버전
"""

import logging
import os
import re
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

import gradio as gr
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from langgraph.store.base import BaseStore
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, RemoveMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Import our custom modules
from vector_database import AviationVectorDatabase
from flight_data_adapter import FlightDataAdapter, AircraftInfo

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# ============= Tools 정의 =============
@tool
def search_flight_info(callsign: str) -> str:
    """
    실시간 항공편 정보를 검색합니다.

    Args:
        callsign: 항공편명 (예: KAL123, AAR456)

    Returns:
        항공편 정보 (위치, 고도, 속도, 제조사 등)
    """
    try:
        flight_adapter = FlightDataAdapter()
        aircraft_info = flight_adapter.get_aircraft_by_callsign(callsign)

        if aircraft_info:
            nearest_airports = flight_adapter.find_nearest_airports(aircraft_info, max_airports=3)

            result = f"항공편 {callsign} 정보:\n"
            result += f"• 기종: {aircraft_info.aircraft_type}\n"
            result += f"• 제조사: {aircraft_info.manufacturer}\n"
            result += f"• 항공사: {aircraft_info.airline}\n"
            result += f"• 위치: 위도 {aircraft_info.latitude:.4f}°, 경도 {aircraft_info.longitude:.4f}°\n"
            result += f"• 고도: {aircraft_info.altitude:,} ft ({int(aircraft_info.altitude * 0.3048):,} m)\n"
            result += f"• 속도: {aircraft_info.speed} knots ({int(aircraft_info.speed * 1.852)} km/h)\n"
            result += f"• 방향: {aircraft_info.heading}°\n"

            if nearest_airports:
                result += f"• 가장 가까운 공항: {nearest_airports[0][0].name} ({nearest_airports[0][0].code}) - {nearest_airports[0][1]:.1f} km\n"

            result += f"• 지원 여부: {'지원됨' if flight_adapter.is_supported_aircraft(aircraft_info.aircraft_type) else '미지원'}\n"

            return result
        else:
            return f"항공편 {callsign}을(를) 찾을 수 없습니다."

    except Exception as e:
        logger.error(f"Error in flight search: {str(e)}")
        return f"항공편 검색 중 오류 발생: {str(e)}"


@tool
def search_aviation_documents(query: str, airport_codes: Optional[str] = None) -> str:
    """
    항공 기술 문서를 검색합니다.

    Args:
        query: 검색할 질문이나 키워드
        airport_codes: 공항 코드 (선택사항, 예: RKSI, RKSS)

    Returns:
        관련 항공 문서 내용
    """
    try:
        aviation_db = AviationVectorDatabase()
        aviation_db.load_vector_store()

        # 검색 쿼리 구성
        search_query = query
        if airport_codes:
            search_query = f"{query} {airport_codes}"

        # 문서 검색
        docs = aviation_db.search_documents(search_query, k=5)

        if docs:
            result = "관련 항공 문서:\n\n"
            for i, doc in enumerate(docs, 1):
                result += f"{i}. {doc['title']} ({doc['section_type']})\n"
                result += f"   {doc['content'][:200]}...\n\n"
            return result
        else:
            return "관련 문서를 찾을 수 없습니다."

    except Exception as e:
        logger.error(f"Error in document search: {str(e)}")
        return f"문서 검색 중 오류 발생: {str(e)}"


# ============= State 정의 =============
class AviationGraphState(MessagesState):
    """항공 시스템 그래프 상태"""
    summary: str  # 대화 요약
    context: str  # 검색된 메모리 컨텍스트
    extracted_callsign: Optional[str]  # 추출된 항공편명
    extracted_airports: Optional[List[str]]  # 추출된 공항 코드


# ============= Helper Functions =============
def extract_callsign_from_text(text: str) -> Optional[str]:
    """텍스트에서 항공편명 추출"""
    # 항공편명 패턴 매칭
    patterns = [
        r'\b([A-Z]{2,3}\d{1,4})\b',  # KAL123, AAR456
        r'\b([A-Z]{2,3}\s?\d{1,4})\b',  # KAL 123
    ]

    for pattern in patterns:
        match = re.search(pattern, text.upper())
        if match:
            return match.group(1).replace(' ', '')

    return None


def extract_airport_codes_from_text(text: str) -> List[str]:
    """텍스트에서 공항 코드 추출 및 변환"""
    airport_mapping = {
        '서울공항': 'RKSM',
        '김포공항': 'RKSS',
        '인천공항': 'RKSI',
        '김포': 'RKSS',
        '인천': 'RKSI',
        'gimpo': 'RKSS',
        'incheon': 'RKSI'
    }

    airports = []
    text_lower = text.lower()

    # 한국어/영어 공항명 매핑
    for name, code in airport_mapping.items():
        if name in text_lower and code not in airports:
            airports.append(code)

    # 이미 ICAO 코드인 경우
    icao_pattern = r'\b(RK[A-Z]{2})\b'
    matches = re.findall(icao_pattern, text.upper())
    for match in matches:
        if match not in airports:
            airports.append(match)

    return airports


# ============= 노드 함수 =============
def aviation_agent_with_memory(state: AviationGraphState, config: RunnableConfig, *, store: BaseStore):
    """
    항공 전문 에이전트 - 메모리 검색 + 메시지 관리 + LLM 호출 통합
    """
    try:
        user_id = config.get("configurable", {}).get("user_id", "default")
        namespace = (user_id, "aviation_conversation")

        messages = state["messages"]
        summary = state.get("summary", "")

        # ========== 메시지 관리 (10개 초과시 요약 후 삭제) ==========
        delete_messages = []
        if len(messages) > 10:
            # 요약 생성/업데이트
            messages_to_summarize = messages[:-4]  # 마지막 4개 제외

            if messages_to_summarize:
                # 기존 요약이 있으면 확장, 없으면 새로 생성
                summary_prompt = (
                    f"{'Previous summary: ' + summary + chr(10) if summary else ''}"
                    f"Summarize this aviation conversation in Korean:\n"
                    + "\n".join([f"{type(m).__name__}: {m.content}" for m in messages_to_summarize])
                )

                llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
                summary = llm.invoke(f"Provide a concise Korean summary of this aviation conversation:\n{summary_prompt}").content

                # 오래된 메시지 삭제 마크
                delete_messages = [RemoveMessage(id=m.id) for m in messages[:-4]]
                messages = messages[-4:]  # 최근 4개만 유지

        # ========== 장기 메모리에서 관련 대화 검색 ==========
        context = ""
        extracted_callsign = None
        extracted_airports = []

        if messages:
            last_msg = messages[-1]

            # 항공편명과 공항 코드 추출
            extracted_callsign = extract_callsign_from_text(last_msg.content)
            extracted_airports = extract_airport_codes_from_text(last_msg.content)

            # 메모리에서 관련 대화 검색
            memories = store.search(namespace, query=last_msg.content, limit=3)

            if memories:
                context = "관련 과거 대화:\n" + "\n".join([
                    f"[{m.value['timestamp']}] Q: {m.value['query'][:100]}... A: {m.value['response'][:100]}..."
                    for m in memories
                ])

        # ========== 시스템 프롬프트 구성 ==========
        system_content = f"""당신은 항공분야 전문가 AI입니다. 다음 도구들을 활용해서 정확한 답변을 제공하세요:

1. search_flight_info: 실시간 항공편 정보 검색 (항공편명 필요)
2. search_aviation_documents: 항공 기술 문서 검색

답변 지침:
- 항공편 관련 질문이면 search_flight_info 도구를 사용하세요
- 항공 기술, 절차, 공항 정보 질문이면 search_aviation_documents 도구를 사용하세요
- 한국어로 답변하고, 전문 용어는 이해하기 쉽게 설명하세요
- 유저가 "긴급상황 발생", "살려주세요", "조종사가 없어요",  "고장났어요" 등의 긴급상황 발생시 해당 항공편의 위치를 파악 후, 가까운 공항으로 안내하고, 해당 기종의 착륙절차 및 공항의 접근절차 활주로 정보 및  무전 정보 및 ATC 등의 정보를 알려주고 매번 다음 절차를 알려줄 수 있도록 도와주세요.

{f'대화 요약: {summary}' if summary else ''}
{context if context else ''}
{f'추출된 항공편: {extracted_callsign}' if extracted_callsign else ''}
{f'관련 공항: {", ".join(extracted_airports)}' if extracted_airports else ''}"""

        system_msg = SystemMessage(system_content)

        # ========== LLM 호출 ==========
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
        llm_with_tools = llm.bind_tools([search_flight_info, search_aviation_documents])

        model_messages = [system_msg] + messages
        response = llm_with_tools.invoke(model_messages)

        # ========== 상태 업데이트 반환 ==========
        return {
            "messages": delete_messages + [response],
            "summary": summary,
            "context": context,
            "extracted_callsign": extracted_callsign,
            "extracted_airports": extracted_airports
        }

    except Exception as e:
        logger.error(f"Error in aviation agent: {e}")
        return {"messages": [AIMessage(f"오류가 발생했습니다: {str(e)}")]}


def save_aviation_memory(state: AviationGraphState, config: RunnableConfig, *, store: BaseStore):
    """
    항공 시스템 대화를 장기 메모리에 저장
    """
    try:
        user_id = config.get("configurable", {}).get("user_id", "default")
        namespace = (user_id, "aviation_conversation")

        messages = state["messages"]

        # 가장 최근의 연속된 Human-AI 메시지 쌍 찾기
        user_msg = None
        ai_msg = None

        # 마지막 메시지부터 확인
        for i in range(len(messages) - 1, -1, -1):
            msg = messages[i]

            # AI 메시지를 먼저 찾음
            if isinstance(msg, AIMessage) and not ai_msg:
                # Tool 관련 메시지는 스킵
                if not hasattr(msg, 'tool_calls') or not msg.tool_calls:
                    ai_msg = msg
                    ai_msg_idx = i

            # AI 메시지를 찾은 후, 바로 앞의 Human 메시지 찾기
            elif ai_msg and isinstance(msg, HumanMessage):
                # 연속된 메시지인지 확인
                is_consecutive = True
                for j in range(i + 1, ai_msg_idx):
                    if isinstance(messages[j], HumanMessage):
                        is_consecutive = False
                        break

                if is_consecutive:
                    user_msg = msg
                    break

        # 메모리 저장
        if user_msg and ai_msg:
            memory = {
                "query": user_msg.content,
                "response": ai_msg.content,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "summary": state.get("summary", ""),
                "callsign": state.get("extracted_callsign"),
                "airports": state.get("extracted_airports", []),
                "thread_id": config.get("configurable", {}).get("thread_id"),
                "message_count": len(messages),
                "category": "aviation"
            }

            memory_id = f"{datetime.now().timestamp()}_{uuid.uuid4().hex[:8]}"
            store.put(namespace, memory_id, memory)

            logger.info(f"💾 Saved aviation memory: {memory_id[:30]}...")
            logger.info(f"   Q: {user_msg.content[:50]}...")
            logger.info(f"   A: {ai_msg.content[:50]}...")
            if memory['callsign']:
                logger.info(f"   Flight: {memory['callsign']}")
            if memory['airports']:
                logger.info(f"   Airports: {memory['airports']}")
        else:
            logger.info("⚠️  No valid Q&A pair found to save")

        return state

    except Exception as e:
        logger.error(f"Error saving aviation memory: {e}")
        return state


class AviationAgentSystem:
    """항공 에이전트 시스템"""

    def __init__(self):
        self.aviation_db = AviationVectorDatabase()
        self.flight_adapter = FlightDataAdapter()

        # 벡터 데이터베이스 로드
        if not self.aviation_db.load_vector_store():
            logger.error("Failed to load vector database")
            raise RuntimeError("Vector database not available")

        # 임베딩 모델 설정
        self.embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

        # 메모리 스토어 설정
        self.conversation_store = InMemoryStore(
            index={
                "embed": self._embed_texts,
                "dims": 1536,
                "fields": ["query", "response", "summary", "callsign", "airports"]
            }
        )

        # 그래프 구성
        self.graph = self._build_graph()

        logger.info("Aviation Agent System initialized successfully")

    def _embed_texts(self, texts: List[str]) -> List[List[float]]:
        """텍스트 임베딩"""
        return self.embeddings_model.embed_documents(texts)

    def _build_graph(self) -> StateGraph:
        """에이전트 그래프 구성"""
        builder = StateGraph(AviationGraphState)

        # 노드 추가
        builder.add_node("agent", aviation_agent_with_memory)
        builder.add_node("tools", ToolNode([search_flight_info, search_aviation_documents]))
        builder.add_node("memory", save_aviation_memory)

        # 엣지 구성
        builder.add_edge(START, "agent")
        builder.add_conditional_edges(
            "agent",
            tools_condition,
            {
                "tools": "tools",
                "__end__": "memory"
            }
        )
        builder.add_edge("tools", "agent")
        builder.add_edge("memory", END)

        # 그래프 컴파일
        graph = builder.compile(
            checkpointer=InMemorySaver(),
            store=self.conversation_store
        )

        # 그래프 이미지 저장
        try:
            graph_image = graph.get_graph().draw_mermaid_png()
            with open("aviation_agent_workflow.png", "wb") as f:
                f.write(graph_image)
            logger.info("✅ Agent graph image saved as 'aviation_agent_workflow.png'")
        except Exception as e:
            logger.warning(f"⚠️ Could not save graph image: {str(e)}")

        return graph

    def process_message(self, message: str, user_id: str = "default", thread_id: str = None) -> str:
        """메시지 처리"""
        if not thread_id:
            thread_id = f"aviation_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"

        config = RunnableConfig(
            configurable={
                "user_id": user_id,
                "thread_id": thread_id
            }
        )

        try:
            # 입력 메시지
            input_state = {
                "messages": [HumanMessage(content=message)]
            }

            # 그래프 실행
            result = self.graph.invoke(input_state, config)

            # AI 응답 추출
            if result["messages"]:
                last_message = result["messages"][-1]
                if isinstance(last_message, AIMessage):
                    return last_message.content

            return "죄송합니다. 응답을 생성할 수 없습니다."

        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            return f"메시지 처리 중 오류가 발생했습니다: {str(e)}"


def main():
    """메인 함수"""

    # 항공 에이전트 시스템 초기화
    try:
        aviation_system = AviationAgentSystem()
        logger.info("Aviation Agent System ready")
    except Exception as e:
        logger.error(f"Failed to initialize system: {str(e)}")
        print(f"❌ 시스템 초기화 실패: {str(e)}")
        return

    # 사용자별 세션 관리
    user_sessions = {}

    def chat_function(message: str, history: List) -> str:
        """Gradio 채팅 함수"""
        if not message.strip():
            return "질문을 입력해주세요."

        # 간단한 사용자 식별 (실제 환경에서는 더 정교한 방법 사용)
        user_id = "gradio_user"

        # 세션 관리
        if user_id not in user_sessions:
            user_sessions[user_id] = {
                "thread_id": f"aviation_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}",
                "start_time": datetime.now()
            }

        thread_id = user_sessions[user_id]["thread_id"]

        try:
            return aviation_system.process_message(message, user_id, thread_id)
        except Exception as e:
            logger.error(f"Chat error: {str(e)}")
            return f"오류가 발생했습니다: {str(e)}"

    # Gradio 인터페이스 생성
    demo = gr.ChatInterface(
        fn=chat_function,
        title="🛩️ Aviation AI Agent",
        description="""
        **메모리 기능이 있는 항공 질문 답변 에이전트**

        - 실시간 항공편 정보 조회 (seoul_flight.py 연동)
            - https://seoul.flightfeeder.page/
        - 항공 기술 문서 검색 (RAG)
        - 대화 기록 저장 및 활용
        - 단기/장기 메모리 관리

        **사용 예시:**
        - "KAL123편 정보 알려주세요" (항공편 조회)
        - "보잉 737 착륙 절차는?" (문서 검색)
        - "김포공항 STAR 절차" (공항 정보)
        """,
        examples=[
            ["KAL123편은 지금 어디에 있나요?"],
            ["AAR456 항공기의 고도와 속도를 알려주세요"],
            ["보잉 777 착륙 절차를 알려주세요"],
            ["인천공항 STAR 절차는 어떻게 되나요?"],
            ["에어버스 A320의 특징은 무엇인가요?"],
        ],
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="gray",
        ),
        type="messages"
    )

    # 인터페이스 실행
    demo.launch(
        server_name="0.0.0.0",
        server_port=8082,
        share=True,
        debug=True
    )


if __name__ == "__main__":
    main()