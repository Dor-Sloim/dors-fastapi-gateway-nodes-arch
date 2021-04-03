FROM python:3.7

RUN pip install fastapi uvicorn httpx
COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ../common /common
COPY ../gateway /gateway

EXPOSE 3000

CMD ["uvicorn", "gateway.main:app", "--host", "0.0.0.0", "--port", "3000"]