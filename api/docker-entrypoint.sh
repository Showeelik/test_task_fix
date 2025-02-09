#!/bin/sh

echo "Apply database migrations"
# Дождаться доступности базы данных
python3 manage.py wait_for_db

# Применить миграции
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata users/fixtures/auth.json

exec "$@"