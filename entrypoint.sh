#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Starting Django..."
exec "$@"