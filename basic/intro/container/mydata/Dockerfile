FROM python:3.11-alpine
RUN apk add --no-cache bash curl gcc musl -dev linux-headers jq
#FAST API 및 기타 라이브러리 설치

RUN apt-get update && apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn psutil python-multipart

Copy webserver.py webserver.py

CMD ["python3", "webserver.py"]