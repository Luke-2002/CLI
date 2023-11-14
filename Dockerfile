FROM python:3.9-alpine

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your project files into the container
COPY cli.py .

CMD ["python", "cli.py"]
