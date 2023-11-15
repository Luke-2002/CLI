# Start with the Alpine base image
FROM alpine

# Install Python and pip
RUN apk add --no-cache python3 python3-dev py3-pip

# Copy the application files into the container
COPY . /app
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
ENTRYPOINT ["python3", "cli.py"]
