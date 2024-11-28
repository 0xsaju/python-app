#!/bin/bash

# Apply database migrations
flask db upgrade

# Start the application with Gunicorn
exec gunicorn \
    --bind 0.0.0.0:5000 \
    --workers 4 \
    --access-logfile - \
    "app:create_app()"