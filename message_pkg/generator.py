
import random
from faker import Faker

# Инициализируем Faker для генерации случайных данных
fake = Faker()

# Список сообщений
messages = [
    "Підтримайте або спростуйте думку, висловлену Г. С. Сковородою: «Багатством живиться лише тіло. А душу звеселяє споріднена праця».",
    "Підтримайте або спростуйте думку: «Ми – не безліч стандартних “я”, а безліч всесвітів різних».",
    "Підтримайте або спростуйте думку: «Поразка – це наука. Ніяка перемога так не вчить…».",
    "Підтримайте або спростуйте думку: «Потрібно цінувати те, що маєш, а не те, про що мрієш».",
    "Підтримайте або спростуйте думку: «Будь-яка проблема – це можливість стати кращим».",
    "Добро завжди має перемагати – це ми знаємо з дитинства. Але ж відомо, що будь-яка перемога пов’язана з певним насильством. Як добро має перемагати в нашому недоброму світі?",
    "Чи потрібно людині шукати відповідь на питання про доцільність підкорення природи й володарювання над нею?",
    "До кого ж приходить успіх у житті?",
    ', '.join(fake.words(nb=3)),  # Генерация 3 случайных слов через Faker
    ', '.join(fake.words(nb=3)),
]

def get_random_message(chance: float) -> str:
    """Повертає випадкову тему з заданою вірогідністю"""
    print("В залежності від введеного вами шансу випадіння вам може видатись тема для власного висловлення")
    print("або ж кілька слів англійською, з яких треба укласти речення.")
    if random.random() < chance:
        return random.choice(messages)
    else:
        return "Цього разу не повезло."

# Пример использования
print(get_random_message(0.7))
