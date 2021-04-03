FROM python:3.7

COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ../common /common
COPY ../gateway /gateway

ARG PORT
ENV PORT $PORT
ARG MODULE_NAME
ENV MODULE_NAME $MODULE_NAME

CMD uvicorn gateway.main:app --host 0.0.0.0 --port=${PORT}