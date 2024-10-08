# syntax=docker/dockerfile:1
FROM python:3.9

WORKDIR /app
ENV app=run.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "uvicorn","run:app", "--reload", "--host", "0.0.0.0"]


