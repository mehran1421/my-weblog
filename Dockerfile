# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for Pillow, psycopg2, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    tcl-dev \
    tk-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list
COPY requirements.txt /app/

# Upgrade pip to avoid celery metadata bug
RUN pip install --upgrade pip==24.0

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files (optional, Django)
RUN python manage.py collectstatic --noinput || true

# Expose port 8000
EXPOSE 8000

# Run Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
