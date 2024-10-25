
**Описание проекта: Посчитайте клики по ссылкам**

Это консольное приложение, разработанное на Python, которое позволяет пользователям сокращать URL-адреса и отслеживать количество переходов по уже сокращённым ссылкам с помощью VK ID API.

**Функциональность проекта:**
- Принимает от пользователя полный URL-адрес.
- Использует VK ID API для преобразования введённого URL в сокращённую ссылку.
- Если пользователь вводит уже сокращённую ссылку, приложение возвращает количество переходов по ней.

**Требования:**
- Python 3.x
- Библиотека `requests` для работы с HTTP-запросами

**Установка:**
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Evgeny1337/CounterClick.git
   cd CounterClick
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # на macOS/Linux
   myenv\Scripts\activate     # на Windows
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r req.txts
   ```
   4. Сохраните токен VK ID API в переменные окружения:
Внутри вашего venv создайте файл .env и добавьте туда переменную TOKEN='Ваш API ключ'.

**Использование:**
Запустите приложение:
```bash
python script.py
```
Следуйте указаниям на экране:
- Введите полный URL-адрес для его сокращения.
- Если вы хотите узнать количество переходов по уже существующей сокращённой ссылке, просто введите её.
**Примечания:**
- Убедитесь, что у вас есть доступ к VK ID API и необходимые токены.
```