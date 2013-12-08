# -*- coding: utf-8 -*-
import tempfile
from os.path import dirname, join, realpath
from os import getenv


UPSTREAM_DATE_URL = 'http://timezonedb.com/date.txt'
UPSTREAM_DUMP_URL = 'http://timezonedb.com/files/timezonedb.csv.zip'

TEMPLATE_DIR = join(dirname(realpath(__file__)), 'templates')

DOWNLOAD_DIR = getenv('TZDB_DOWNLOAD_DIR') or tempfile.gettempdir()
DATABASE_URI = getenv('TZDB_DATABASE_URI')
