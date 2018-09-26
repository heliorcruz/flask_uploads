#!/usr/bin/python
import sys
import logging
import os
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))

from webservice.py import app as application

application.config.from_pyfile('config.py')

if __name__ == '__main__':
    application.run()
