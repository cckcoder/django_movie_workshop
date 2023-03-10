FROM python:3.8.16-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN  pip install -U pip

RUN  pip install -r requirements.txt

COPY . .
