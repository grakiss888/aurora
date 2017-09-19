FROM ubuntu:16.04
MAINTAINER leo wang

RUN apt-get update
RUN apt-get install -y python-pip git

RUN pip install --upgrade pip
RUN pip install gunicorn flask

ENV HOME /home
WORKDIR /home

RUN git clone http://github.com/grakiss888/aurora

WORKDIR /home/aurora/aurora

CMD ["bash", "start-server.sh"]


