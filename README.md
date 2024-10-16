Ця річ із вірогідністю у 50% (за замовчуванням) видає тему для власного висловлення із
заздалегідь сформованного списку, або ж видає три слова англійською, для побудови речення
з ними.

щоб запустити це з docker compose:
docker-compose up --build --remove-orphans
docker-compose run app --chance 0.7
docker-compose down (для зупинення роботи контейнеру)

щоб запустити з docker:
docker build -t essay_topic_app .
docker run essay_topic_app --chance 0.7

щоб запустити з make:
make d-homework-i-run CHANCE=0.7
