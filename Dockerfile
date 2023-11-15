FROM python:3.8-slim

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your project files into the container
COPY cli.py /app/cli.py

# Make the script executable
RUN chmod +x /app/cli.py

# Optionally, rename the script
RUN mv /app/cli.py /app/cli

# Set the entry point to your script
ENTRYPOINT ["/app/cli"]

CMD ["python", "cli.py"]
