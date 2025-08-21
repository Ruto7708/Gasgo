# Use a small Python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps for psycopg2 and pillow (if you use images)
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Ensure entrypoint is executable
RUN chmod +x /app/entrypoint.sh

# Expose port (Vercel will route traffic here)
EXPOSE 8000

# Start
CMD ["./entrypoint.sh"]
