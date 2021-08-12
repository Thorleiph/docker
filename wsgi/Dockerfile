FROM ubuntu:20.04

MAINTAINER Magnus Lindgren "maintainer@sm0tnt.com"

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade

RUN apt -y install build-essential python-dev pip nano

RUN pip install uwsgi

RUN useradd --system uwsgi

WORKDIR /opt/uWSGI

