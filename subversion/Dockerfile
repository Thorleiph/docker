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

RUN echo $'#!/bin/sh\n\
\n\
httpd -f /etc/apache2/httpd.conf -D FOREGROUND\n\
' > /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 80

WORKDIR /

RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

ENTRYPOINT [ "/entrypoint.sh" ]
