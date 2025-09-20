# Dockerfile for Whisper Agent

FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and application files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
