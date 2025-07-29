import os
os.environ["OPENAI_API_KEY"] = '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'

from langchain.schema import SystemMessage, HumanMessage
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# 파일 경로
pdf_path = "C:/Users/SKAX/Desktop/경력기술서_홍길동.pdf"

# 1. PDF 로딩
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# 2. 텍스트 분할 (길이 제한 고려)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
split_docs = text_splitter.split_documents(documents)

llm = ChatOpenAI(
    model="gpt-4o",          # LLM 모델명
    top_p=0.7,               # 확률 분포 Cut-off
    temperature=1.4,         # 창의성
    max_tokens=10000,        # 응답 길이 제한
    streaming=True           # 스트리밍 활성화
)

# 대화 메시지 구성
messages = [
    SystemMessage(content="당신은 프로페셔널 면접관이자, 경력 10년 이상의 채용 전문가입니다."),
    HumanMessage(content= "경력서 파일이 업로드 되면 경력서를 분석하여 검토 의견을 장, 단점 각각 3개로 요약해서 서술하시오. 채용을 위한 하기 정보를 참고하세요."
                 "#회사 정보: 당사는 고객과 함께 성장하며, 전문적인 Domain 지식과 Biz. Consultancy를 바탕으로 최고의 AI전환 파트너로 거듭나고 있습니다"
                 "#채용 포지션: Enterprise 업무 데이터와 기존 Legacy 데이터를 통합하고 분석과 시각화를 통한 고객의 니즈에 맞는 최적의 의사결정을 돕는 Insight를 도출하기 위함"
                 "#인재상: Passionate: 120% 정신으로 업무에 열정적으로 몰입합니다. 자신의 능력에 한계를 두지 않고 새로운 일에 끊임없이 도전하기 '할 수 있다는 자신감'과 '포기하지 않는 열망' 가지기고객의 Pain Point를 해결하기 위해 치열하게 고민하기" 
                 "Proactive: 올바른 방향으로 자신의 일을 능동적으로 이끌어 갑니다.지시를 받지 않아도 내 일을 선제적으로 고민하기,나의 일과 관련이 있으면 주도적으로 실행하기 더 좋은 방법이나 아이디어가 있으면 Speak-out 하기" \
                 "Professional: 맡은 업무에서 최고 수준의 전문가가 됩니다. 꾸준한 학습으로 다양한 Skill을 갖추기 위해 노력하기 주변 동료에게 기술/역량을 전이하고 함께 성장하기 누구에게나 인정받는 Role Model로 당당하게 고객을 리딩하기" \
                 "People: 우리 모두의 행복, 함께하는 공동체를 이룹니다.모두의 행복을 위해 이타심 갖기동료의 노력과 성과를 진심으로 응원하고 축하하기 겸손하고 열린 마음으로 소통하고 협력하기"
                )
]

qa_chain = load_qa_chain(llm, chain_type="stuff")  # stuff: 전체 텍스트 다 넣는 방식

# 4. 질문
result = qa_chain.run(input_documents=split_docs, question=messages)
print(result)
# line = ""
# for chunk in llm.stream(messages):
#    line += chunk.content
#    print(chunk.content, end="", flush=True)
#    if len(line) > 100:  # 100자마다 줄바꿈
#        print()
#        line = ""