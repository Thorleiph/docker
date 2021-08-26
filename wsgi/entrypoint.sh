#!/bin/bash

uwsgi --uid uwsgi --http :9000 --wsgi-file /opt/wsgi/python_file.py --master --processes 4 --threads 2
