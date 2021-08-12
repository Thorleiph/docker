FROM ubuntu:20.04

MAINTAINER Magnus Lindgren "github@sm0tnt.com"

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade

RUN apt -y install build-essential python-dev pip nano

RUN pip install uwsgi

RUN useradd --system uwsgi

WORKDIR /opt/wsgi
ADD python_file.py .

WORKDIR /

ADD entrypoint.sh /
run chmod 755 /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
