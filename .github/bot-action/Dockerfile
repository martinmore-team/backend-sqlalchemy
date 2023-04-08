FROM python:3.10-alpine

RUN pip install httpx==0.23.1


COPY . /action

ENTRYPOINT ["python", "/action/main.py"]
