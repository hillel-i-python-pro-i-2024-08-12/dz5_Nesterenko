FROM python:3.12

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливаем необходимые зависимости
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Устанавливаем pre-commit, ruff и mypy
RUN pip install pre-commit ruff mypy

# Устанавливаем Git
RUN apt-get update && apt-get install -y git

# Копируем проект в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Инициализация pre-commit
RUN pre-commit install

# Указываем команду для запуска Python скрипта
ENTRYPOINT ["python", "main.py"]

# По умолчанию передаем пустые аргументы (позволяет переопределить через командную строку)
CMD ["--chance", "0.5"]
