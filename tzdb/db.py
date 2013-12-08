# -*- coding: utf-8 -*-
import logging

from time import strptime, mktime
from datetime import date
from os.path import join

import zipfile
import requests
from mako.lookup import TemplateLookup
from sqlalchemy import create_engine, sessionmaker

from tzdb.models import Base
from tzdb.config import (
    UPSTREAM_DATE_URL, UPSTREAM_DUMP_URL, TEMPLATE_DIR,
    DOWNLOAD_DIR, DATABASE_URI)


logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)

templateLookup = TemplateLookup(directories=[TEMPLATE_DIR])


def get_engine():
    return create_engine(DATABASE_URI)


def create_schema(engine=None):
    """
    Create all tables

    """
    if not engine:
        engine = get_engine()
    metadata = Base.metadata
    metadata.bind = engine
    metadata.create_all()


def drop_schema(engine=None):
    """
    Drop all tables

    """
    if not engine:
        engine = get_engine()
    metadata = Base.metadata
    metadata.bind = engine
    metadata.drop_all()


def get_upstream_date():
    """
    Query the latest update date from timezonedb.com

    """
    log.info('Fetching last update date from {0}'.format(UPSTREAM_DATE_URL))
    date_str = requests.get(UPSTREAM_DATE_URL).text.strip()
    return date.fromtimestamp(mktime(strptime(date_str, '%Y-%m-%d')))


def download_data(engine=None):
    r = requests.get(UPSTREAM_DUMP_URL, stream=True)
    dump_filename = join(DOWNLOAD_DIR, 'tzdb_dump.zip')
    with open(dump_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    with zipfile.ZipFile(dump_filename, 'r') as z:
        z.extractall(DOWNLOAD_DIR)


def load_data(engine=None):
    if not engine:
        engine = get_engine()
    sql = templateLookup.get_template('load_data.sql').render(
        dumps_dir=DOWNLOAD_DIR,
        date_version=unicode(get_upstream_date())
    )
    engine.execute(sql)
