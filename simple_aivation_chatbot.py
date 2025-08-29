from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# AviationVectorDatabase 임포트
from vector_database import AviationVectorDatabase

# LLM 설정
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    top_p=0.9,
)

advanced_template = """당신은 항공분야 전문가 AI입니다. 주어진 컨텍스트를 바탕으로 정확하고 유용한 답변을 제공하세요.

## 답변 지침
- 컨텍스트에 있는 정보만을 사용하여 답변하세요
- 확실하지 않은 정보는 "명확하지 않습니다"라고 명시하세요
- 답변은 논리적이고 구조화된 형태로 제공하세요
- 가능한 경우 구체적인 예시나 수치를 포함하세요

<컨텍스트>
{context}
</컨텍스트>

<질문>
{question}
</질문>

## 답변 형식
**핵심 답변:** (질문에 대한 직접적인 답변)

**세부 설명:** (추가적인 설명이나 배경 정보)

**관련 정보:** (컨텍스트에서 발견된 연관 정보)
"""

advanced_prompt = ChatPromptTemplate.from_template(advanced_template)

# 템플릿 출력
advanced_prompt.pretty_print()

# AviationVectorDatabase 초기화 및 retriever 설정
aviation_db = AviationVectorDatabase()
aviation_db.load_vector_store()
retriever = aviation_db.vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 10}
)

# 문서 포맷팅
def format_docs(docs):
    return "\n\n".join([f"{doc.page_content}" for doc in docs])

# RAG 체인 생성
rag_chain = (
    RunnableParallel(
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
    )
    | advanced_prompt
    | llm
    | StrOutputParser()
)

# 체인 실행
query = "RKSM공항의 착륙 절차에 대해서 설명해주세요"
output = rag_chain.invoke(query)

print(f"쿼리: {query}")
print("답변:")
print(output)