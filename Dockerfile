#FROM ubuntu:latest
#LABEL authors="Lenovo"
#
#ENTRYPOINT ["top", "-b"]

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
