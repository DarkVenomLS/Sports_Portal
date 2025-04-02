#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
if [[ $CREATE_SUPERUSER == "True" && -n "$DJANGO_SUPERUSER_USERNAME" && -n "$DJANGO_SUPERUSER_EMAIL" && -n "$DJANGO_SUPERUSER_PASSWORD" ]]; then
    python manage.py createsuperuser --no-input --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL" || true
fi

