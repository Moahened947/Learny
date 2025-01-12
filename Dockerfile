# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Learny.settings

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create static and media directories
RUN mkdir -p /app/static /app/media

# Set permissions
RUN chmod -R 755 /app/static /app/media

# Collect static files
RUN python manage.py collectstatic --noinput --clear

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Learny.wsgi:application"]
