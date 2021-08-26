import os

from django.contrib import admin
from django.urls import path

import django

'''
SERVER_SOFTWARE
SERVER_NAME
SERVER_PROTOCOL
SERVER_PORT
REQUEST_METHOD
PATH_INFO
SCRIPT_NAME
QUERY_STRING
REMOTE_HOST
REMOTE_ADDR
HTTP_COOKIE
'''

def application(env, start_response):
	start_response('200 OK', [('Content-Type','text/html')])

	# print("cookie:\t" + env.get("HTTP_COOKIE", ""))
	# print("query:\t" + env.get("QUERY_STRING", ""))
	# print("path:\t" + env.get("PATH_INFO", ""))
	# print("remote:\t" + env.get("REMOTE_ADDR", ""))

	path = env.get("PATH_INFO")
	tmp = path.split("/")

	path_parts = []

	for p in tmp:
		if p != None and len(p)>0:
			path_parts.append(p)
	
	if len(path_parts) == 3:
		print("path:\t" + str(path_parts))

	return [b"Ok"]

print("hello")
