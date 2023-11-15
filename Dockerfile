# Use Python 3.10 on Alpine as the base image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the CLI script into the container
COPY cli.py /app/cli

# Make the CLI script executable
RUN chmod +x /app/cli

# Set the entry point to the CLI script
ENTRYPOINT ["/app/cli"]
