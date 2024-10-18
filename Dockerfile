FROM python:3.12

WORKDIR /app

#Оновлюємо pip та встановлюємо необхідні залежності
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pre-commit ruff mypy

#Встановлюємо Git
RUN apt-get update && apt-get install -y git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

#Копіюємо проект у контейнер
COPY . .

#Ініціалізація pre-commit
RUN pre-commit install

#Вказуємо команду для запуску Python скрипта
ENTRYPOINT ["python", "main.py"]

#За замовчуванням передаємо пусті аргументи (дозволяє перезадати через командну строку)
CMD ["--chance", "0.5"]
