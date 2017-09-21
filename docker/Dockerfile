FROM ubuntu:16.04
MAINTAINER leo wang

RUN apt-get update
RUN apt-get install -y python-pip git

RUN pip install --upgrade pip
RUN pip install gunicorn flask flask-admin flask-login

ENV HOME /home
WORKDIR /home

RUN git clone http://github.com/grakiss888/aurora
RUN mkdir -p /var/log/gunicorn

WORKDIR /home/aurora/aurora

ADD start-server.sh .

CMD ["bash", "start-server.sh"]


