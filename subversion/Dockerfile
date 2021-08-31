# docker build --network host -t subversion:latest .
# docker run -it --rm --network host --name subversion subversion:latest

FROM httpd:alpine3.14

VOLUME /svn

ENV SVN_ROOT=/svn

RUN apk --no-cache add apache2 apache2-utils apache2-webdav mod_dav_svn subversion

RUN mkdir -p /run/apache2

RUN echo $'\n\
LoadModule dav_svn_module /usr/lib/apache2/mod_dav_svn.so\n\
LoadModule authz_svn_module /usr/lib/apache2/mod_authz_svn.so\n\
\n\
<Location /svn>\n\
    DAV svn\n\
    SVNParentPath /svn\n\
    SVNListParentPath on\n\
    SVNAutoversioning on\n\
    AuthType Basic\n\
    AuthName "Subversion"\n\
    AuthUserFile /etc/apache2/conf.d/htpasswd\n\
    Order deny,allow\n\
    Require valid-user\n\
</Location>' > /etc/apache2/conf.d/davsvn.conf

# guest/guest <- this is for testing purposes only!
RUN echo 'guest:$apr1$1lJuhAH0$gB3nlmwXvcCuV5jSJzqod.' > /etc/apache2/conf.d/htpasswd

# There is a "problem" with SIGWINCH if run with -it, it terminates httpd if the terminal is resized. This is by design.

RUN echo $'#!/bin/sh\n\
\n\
case "$1" in\n\
    add)\n\
        echo "Adding repo $2 $3 $4 $5 $6 $7 $8 $9"\n\
        ;;\n\
    *)\n\
        httpd -f /etc/apache2/httpd.conf -D FOREGROUND\n\
        ;;\n\
esac\n\
' > /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 80

WORKDIR /

# Writes log messages to the console instead of log files inside the container.
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

ENTRYPOINT [ "/entrypoint.sh" ]
