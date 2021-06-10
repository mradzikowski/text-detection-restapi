FROM python:3.9.5-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get clean

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py run -h 0.0.0.0