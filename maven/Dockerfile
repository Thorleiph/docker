#
# My own cusom docker image for maven as we need to do some more stuff than what is available in the official maven image
#

FROM ubuntu:22.04

RUN apt -y update
RUN apt -y install ca-certificates git maven curl iputils-ping iproute2

COPY sm0tnt.com.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates

WORKDIR /root
RUN mkdir .m2 | true
