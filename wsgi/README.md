# wsgi

docker build --network host -t wsgi:latest .

docker run -it --rm -p 9000:9000 wsgi:latest
