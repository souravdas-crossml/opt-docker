# Stage 1: Builder stage
FROM python:3.8.10-slim as builder

WORKDIR /app

# Copy just the requirements file first to leverage Docker caching
COPY ./requirements.txt .

# Install necessary system dependencies for some Python packages,
# upgrade pip, and install Python dependencies in one step
RUN apt-get update \
    && apt-get install -y build-essential \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --default-timeout=1000 -r requirements.txt \
    && pip install uvicorn \
    && rm -rf /var/lib/apt/lists/* 

# Stage 2: Production stage
FROM python:3.8.10-slim

WORKDIR /app

# Copy installed Python packages including uvicorn from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# Copy uvicorn executable from the builder stage
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# Copy the application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
