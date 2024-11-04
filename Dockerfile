# syntax=docker/dockerfile:1
FROM python:3.10-alpine3.18

WORKDIR /flask

# Install necessary packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements and install them
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt

# Copy the entire application code
COPY . .

# Set permissions for database files and the 'data' directory
RUN chmod -R 777 /flask

# Initialize the database
RUN python -m flask --app board init-db || true

# Expose the port and run the Flask app
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "board", "run", "--host=0.0.0.0"]
