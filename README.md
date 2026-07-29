PRAKTIKA2026
Описание
Проект представляет собой REST API для работы с категориями и книгами с использованием FastAPI и PostgreSQL.

Запуск проекта
Клонировать репозиторий:
git clone <ссылка_на_репозиторий>
cd PRAKTIKA2026
Создать виртуальное окружение:
python3 -m venv venv
Активировать его:
source venv/bin/activate
Установить зависимости:
pip install -r requirements.txt
Создать файл .env:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bashkirtsev_db
DB_USER=bashkirtsev
DB_PASSWORD=12345
Создать таблицы и заполнить базу:
python3 -m app.init_db
Запустить проект:
uvicorn app.main:app --reload
После запуска открыть:

http://127.0.0.1:8000/docs
