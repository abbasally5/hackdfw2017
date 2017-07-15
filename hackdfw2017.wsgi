#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/earthack/")

from hackdfw2017.app import app as application
application.secret_key = 'secret'
