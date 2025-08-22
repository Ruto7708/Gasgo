#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Change "portfolio" to your Django project folder name (where wsgi.py lives)
gunicorn Gasgo.wsgi:application --bind 0.0.0.0:8000
