# PRAKTIKA2026

## Описание

Проект представляет собой REST API для работы с категориями и книгами с использованием FastAPI и PostgreSQL.

## Запуск проекта

1. Клонировать репозиторий:

```bash
git clone <ссылка_на_репозиторий>
cd PRAKTIKA2026
```

2. Создать виртуальное окружение:

```bash
python3 -m venv venv
```

3. Активировать его:

```bash
source venv/bin/activate
```

4. Установить зависимости:

```bash
pip install -r requirements.txt
```

5. Создать файл `.env`:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bashkirtsev_db
DB_USER=bashkirtsev
DB_PASSWORD=12345
```

6. Создать таблицы и заполнить базу:

```bash
python3 -m app.init_db
```

7. Запустить проект:

```bash
uvicorn app.main:app --reload
```

После запуска открыть:

```
http://127.0.0.1:8000/docs
```
