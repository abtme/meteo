# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install SQLite3
RUN apt-get update && \
    apt-get install -y sqlite3

# Install any needed dependencies specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install pysnmp

# Copy the current directory contents into the container at /app
COPY . /app

# Command to create SQLite database if not present and keep the container running
CMD /bin/sh -c "cd /app/db && if [ ! -f snmp_data.db ]; then sqlite3 snmp_data.db ''; fi && tail -f /dev/null"
