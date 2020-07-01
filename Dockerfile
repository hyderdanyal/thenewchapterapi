FROM ubuntu:18.04

FROM python:3.8

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD python /app/app.py


# FROM tiangolo/uwsgi-nginx-flask:python3.8
# WORKDIR /app/
# COPY requirements.txt /app/
# RUN pip install -r ./requirements.txt
# ENV ENVIRONMENT production
# COPY app.py /app/
# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]
