##FROM ubuntu:latest
##LABEL authors="Lenovo"
##
##ENTRYPOINT ["top", "-b"]
#
#FROM python:3.12-slim
#
#WORKDIR /app
#
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#
#COPY . .
#
#ENTRYPOINT ["python", "main.py"]

# Исходный образ
FROM python:3.9-slim

# Установка зависимостей
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Установка pre-commit, ruff, mypy
RUN pip install pre-commit ruff mypy

# Копирование всего проекта
COPY . /app
WORKDIR /app

# Инициализация pre-commit
RUN pre-commit install

# Команда по умолчанию (если потребуется)
CMD ["python", "main.py"]
