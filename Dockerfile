FROM python:3.10-slim

# Allow Python to import from /app
ENV PYTHONPATH=/app

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Start uvicorn only (no wait script, no init script)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
