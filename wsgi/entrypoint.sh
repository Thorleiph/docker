#!/bin/bash

uwsgi --uid uwsgi --http :9000 --wsgi-file python_file.py
