FROM python:3.6-jessie

LABEL author="Rodrigo L. Gil"

COPY requirements.txt /code/requirements.txt

RUN apt-get update && pip install -r /code/requirements.txt

COPY data/ /code/data/
COPY dw/ /code/dw/
COPY util/ /code/util
COPY definitions.py /code/definitions.py
COPY main.py /code/main.py

WORKDIR /code/
