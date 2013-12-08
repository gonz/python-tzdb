# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tzdb.models import Version
from tzdb.config import DATABASE_URI


_session = None


def get_session():
    if not _session:
        Session = sessionmaker(bind=create_engine(DATABASE_URI))
        return Session()
    return _session


def get_version_date(session=None):
    """
    Query the local db to get the current last update date.

    """
    if not session:
        session = get_session()
    return session.query(Version).first().version_date
