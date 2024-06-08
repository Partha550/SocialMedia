#!/bin/bash

# Exit the script on any error
set -e

# Run database migrations
python manage.py migrate

# Collect static files (if needed)
# python manage.py collectstatic --noinput

# Start the Django server
exec "$@"
