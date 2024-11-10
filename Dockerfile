# Use a lightweight Python image as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
