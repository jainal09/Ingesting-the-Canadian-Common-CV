FROM ubuntu:18.04
FROM python:3.7
RUN apt-get update \
  && apt-get install -y python3.7-dev \
  && pip3 install --upgrade pip
RUN apt-get install -y sqlite3 libsqlite3-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /Ingesting_Common_CV
WORKDIR /Ingesting_Common_CV
ADD . /Ingesting_Common_CV/
RUN pip3 install -r requirements.txt