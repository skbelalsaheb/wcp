FROM python:3.12-bookworm

# Set working directory
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
# Copy application code
COPY . .
# Environment optimizations
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose Django port
EXPOSE 8000

# Run Django app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "WifiCaptivePortal.wsgi:application"]
