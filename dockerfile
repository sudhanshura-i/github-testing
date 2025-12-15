# Stage 1: Build Stage - Use a specific version for stability and smaller size
FROM python:3.11-slim as builder

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
# Use --no-cache-dir to keep the image size down
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Image - A clean, smaller runtime environment
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy the application code
COPY main.py .

# Expose the default port for Uvicorn
EXPOSE 8000

# Command to run the application using Uvicorn
# --host 0.0.0.0 is necessary for container access
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]