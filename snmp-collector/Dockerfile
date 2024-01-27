# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install SQLite3
RUN apt-get update && \
    apt-get install -y sqlite3

# Install any needed dependencies specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install pysnmp

# Run snmp_collector.py when the container launches
CMD ["python", "./snmp_collector.py"]
