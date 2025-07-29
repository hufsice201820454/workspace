from langchain import PromptTemplate

template = "You are a {role}. Answer the following qustion clearly: {question}"

prompt = PromptTemplate(
    input_variables=["role", "question"], template=template)

print(prompt.format(role="data scientist", question="What is overfitting?"))

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


# # LLM 객체생성
# # llm = ChatOpenAI(
# #     model="gpt-4o",          # LLM 모델명
# #     top_p=0.7,               # 확률 분포 Cut-off
# #     temperature=1.4,         # 창의성
# #     max_tokens=500,          # 응답 길이 제한 보통 10000정도
# #     # ,api_key=''            # 환경변수 OPENAI_API_KEY를 기본값으로 읽어옴
# # )

# # # 대화 메시지 구성
# # messages = [
# #     SystemMessage(content="You are a helpful assistant that answers in Korean."),
# #     HumanMessage(content="생성형 AI가 무엇인지 쉽게 설명해줘.")
# # ]

# # # 응답 생성
# # # invoke() : LangChain에서 모델을 한 번 호출할 때 사용하는 메서드 - 동기식(Sync)으로 입력 → 응답을 바로 반환
# # # ainvoke() : 비동기(Asynchronous) 호출 - 작업을 시작해두고, 끝나길 기다리는 동안 다른 작업을 병행
# # response = llm.invoke(messages)
# # print(response.content)

# from langchain_openai import ChatOpenAI
# from langchain.schema import SystemMessage, HumanMessage


# # LLM 객체생성
# llm = ChatOpenAI(
#     model="gpt-4o",          # LLM 모델명
#     top_p=0.7,               # 확률 분포 Cut-off
#     temperature=1.4,         # 창의성
#     max_tokens=500,          # 응답 길이 제한
#     streaming=True           # 스트리밍 활성화
# )

# # 대화 메시지 구성
# messages = [
#     SystemMessage(content="You are a helpful assistant that answers in Korean."),
#     HumanMessage(content="생성형 AI가 무엇인지 설명해줘.")
# ]

# # 스트리밍 응답 생성
# # flush=True: 버퍼링 없이 즉시 출력, 토큰이 들어오는 즉시 바로바로 화면에 출력
# #   -> print()는 버퍼에 쌓아뒀다가 한 번에 출력할 수 있음
# # end="" : 줄바꿈(\n)없이 바로 이어붙임
# for chunk in llm.stream(messages):
#     print(chunk.content, end="", flush=True)  # 토큰 단위 출력


# # Tip: 출력응답 편하게 보기
# #line = ""
# #for chunk in llm.stream(messages):
# #    line += chunk.content
# #    print(chunk.content, end="", flush=True)
# #    if len(line) > 100:  # 100자마다 줄바꿈
# #        print()
# #        line = ""

# from openai import OpenAI
# import os
# from getpass import getpass

# # API 키를 안전하게 입력받기(화면에 노출안됨)
# api_key = getpass("OpenAI API 키를 입력하세요: ")

# # os.environ : 운영체제(OS)에 등록된 환경변수를 파이썬에서 읽거나 쓸 수 있게 해주는 인터페이스
# # OpenAI API KEY는 코드 안에 하드코딩하지 않고 환경변수로 저장해두고 읽어오는 방식이 보안상 안전
# os.environ['OPENAI_API_KEY'] = api_key

# def create_chat_completion(system_input, user_input, model="gpt-4o-mini", temperature=1.2, top_p=0.7, max_tokens=5000):
#     try:

#         messages = [
#             {"role": "system", "content": system_input},
#             {"role": "user", "content": user_input}
#         ]

#         response = OpenAI().chat.completions.create(
#             model=model,                  # LLM모델
#             messages=messages,
#             temperature=temperature,      # 창의성
#             top_p=top_p,                  # 확률 분포 Cut-off
#             max_tokens=max_tokens         # 최대 토큰 수
#         )

#         # 생성된 응답을 반환해요
#         return response
#     except Exception as e:
#         return f"Error: {str(e)}"

## LLM function call

# 메시지
# system_input = "You are a helpful assistant that answers in Korean."
# user_input = "생성형 AI가 무엇인지 쉽게 설명해줘."

# # Sampling Control
# temperature=1.5
# top_p=0.5

# # 응답 생성
# responses = create_chat_completion(system_input, user_input, temperature = temperature, top_p =top_p )
# print(responses)
# print(responses.choices[0].message.content)