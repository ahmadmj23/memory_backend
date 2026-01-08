FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port (Cloud Run defaults to 8080)
EXPOSE 8080

CMD sh -c "python manage.py makemigrations && \
           python manage.py migrate && \
           python manage.py runserver 0.0.0.0:8080"
