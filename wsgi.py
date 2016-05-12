#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

from api import init
init()

from api import app as application
