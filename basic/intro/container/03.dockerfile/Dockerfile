#Step 1: Base Image
FROM python:3.10
FROM alpine:latest

#Step 2: Register label
LABEL app=demo

#Step 3: Install jq and curl
RUN apk add --no-cache jq curl

#Step 4: ADD JSON DATA from URL
ADD https://springboot.skala25a.project.skala-al.com/swagger/swagger-docs /tmp/swagger-docs.JSON

#Step 5: Use EntryPoint to process and print JSON with jq
ENTRYPOINT ["sh", "-c"]

#Step 6: Print JSON DATA using jq
CMD["echo 'Formatted JSON output:' && jq'.'/tmp/swagger-docs.json"]