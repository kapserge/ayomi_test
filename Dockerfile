# Dockerfile

# pull the official docker image
FROM python:3.11

# set work directory
WORKDIR /app

# set env variables
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8002"]