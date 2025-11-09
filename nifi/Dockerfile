# docker build --network host -t nifi:2.6.0 .

FROM ubuntu:24.04 AS nifi_build

RUN apt update -y
RUN apt upgrade -y
RUN apt dist-upgrade -y
RUN apt install unzip curl -y 
RUN curl https://dlcdn.apache.org/nifi/2.6.0/nifi-2.6.0-bin.zip -o /nifi-2.6.0-bin.zip
RUN mkdir -p /opt/apache/nifi
WORKDIR /opt/apache/nifi
RUN unzip /nifi-2.6.0-bin.zip
WORKDIR /opt/apache/nifi/nifi-2.6.0/bin

FROM ubuntu:24.04

RUN apt update -y
RUN apt upgrade -y
RUN apt dist-upgrade -y
RUN apt install openjdk-25-jre-headless net-tools -y
RUN mkdir -p /opt/apache
COPY --from=nifi_build /opt/apache /opt/apache
ADD login-identity-providers.xml /opt/apache/nifi/nifi-2.6.0/conf/login-identity-providers.xml
ADD nifi.properties /opt/apache/nifi/nifi-2.6.0/conf/nifi.properties

ADD entrypoint.sh /
RUN chmod 755 /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
