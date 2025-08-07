#!/bin/bash
NAME=sk072
IMAGE_NAME = "webserver"
VERSION="1.0.0"
CPU_PLATFORM=amd64

docker build \
    --tag ${NAME}-${IMAGE_NAME}:${VERSION} \
    --file Dockerfile \
    --platform linux/${CPU_PLATFORM} \
    ${IS_CACHE} .

    