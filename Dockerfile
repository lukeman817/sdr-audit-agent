# Technical Debt: Running as root user - container security issue
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY templates/ templates/

# Expose port
EXPOSE 5000

# Run as root user (security vulnerability)
USER root

# Run the application
CMD ["python", "app.py"]
