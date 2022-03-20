#!/bin/sh

# evita error de permisos
chown -R app:app /app
chown -R app:app /home/app

exec su -m app -c 'python manage.py runserver 0.0.0.0:8000'
