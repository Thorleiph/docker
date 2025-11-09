
## nginx reverse proxy config example with https to nifi

server {
        listen 443 ssl;
        http2 on;
        server_name  nifi.proxy.vn;
        ssl_certificate     /etc/nginx/certs/tls.crt;
        ssl_certificate_key /etc/nginx/certs/tls.key;
        ssl_client_certificate /etc/nginx/certs/nifi-cert.pem;
        #ssl_verify_client off;
        proxy_ssl_certificate /etc/nginx/certs/nifi-tls.crt;
        proxy_ssl_certificate_key /etc/nginx/certs/nifi-tls.key;
        proxy_ssl_trusted_certificate /etc/nginx/certs/nifi-cert.pem;
        location / {
            proxy_pass       https://xxxxx:9443;
            proxy_set_header X-ProxyScheme https;
            proxy_set_header X-ProxyHost nifi.proxy.vn;
            proxy_set_header X-ProxyPort 443;
            proxy_set_header X-ProxiedEntitiesChain "$ssl_client_s_dn";
        }
    }
