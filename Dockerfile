FROM python:3.9-alpine

WORKDIR /app

COPY cli.py .

RUN pip install requests

CMD ["python", "cli.py"]
