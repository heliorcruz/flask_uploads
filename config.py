# -*- coding: UTF-8 -*-
#!/usr/bin/python

DEVELOPMENT   = True
SERVER_LOCAL  = True
SECRET_KEY = 'the quick brown fox jumps over the lazy dog'
CORS_HEADERS= 'Content-Type'
CORS_ORIGINS = [] # or '*'
UPLOAD_FOLDER = 'root-path/uploas'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])
MAX_CONTENT_LENGTH =  16 * 1024 * 1024


if DEVELOPMENT:
    ENV = 'development'
    DEBUG = True
    if SERVER_LOCAL:
        SERVER_NAME = '127.0.0.1:8080'
    else:
        SERVER_NAME = 'host:port'
else:
    SERVER_NAME = 'host:port'
