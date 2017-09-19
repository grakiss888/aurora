FROM ubuntu:16.04
MAINTAINER leo wang

RUN apt-get update
RUN apt-get install python-dev python-pip python-virtualenv git

RUN pip install gunicorn

ENV HOME /home
WORKDIR /home

RUN git clone http://github.com/grakiss888/aurora

WORKDIR /home/aurora/aurora

CMD ["bash", "start-server.sh"]


