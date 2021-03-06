# -*- coding: utf-8 -*-
"""
Description:
  Manage the tzdb data.

Usage:
  pydb upstream-date [--log-level=<log_level>]
  pydb update [--force] [--log-level=<log_level>]
  pydb create-schema [--log-level=<log_level>]
  pydb drop-schema [--log-level=<log_level>]

Options:
  -h --help                Show this screen
  --log-level=<log_level>  Set the logging/ouput level [default: WARNING]
  --force                  Force the data update
"""
from __future__ import (
    print_function, unicode_literals, division, absolute_import)
import logging

from docopt import docopt
from schema import Schema, SchemaError, Use, And

from tzdb.db import (
    get_upstream_date, load_data, download_data, create_schema, drop_schema)
from tzdb.queries import get_version_date as get_local_date


logging.basicConfig(format='%(message)s')
log = logging.getLogger('tzdb')


def validate_data(args):
    schema = Schema({
        '--log-level': And(
            Use(unicode),
            Use(lambda l: l.upper()),
            lambda l: l in ('ERROR', 'WARNING', 'INFO', 'DEBUG'),
            error='Invalid log level'
        ),
        '--force': Use(bool),
        'upstream-date': Use(bool),
        'update': Use(bool),
        'drop-schema': Use(bool),
        'create-schema': Use(bool),
    })

    try:
        return schema.validate(args)
    except SchemaError as e:
        exit(e)


def cmd_upstream_date(args):
    print(get_upstream_date())


def cmd_update(args):
    force = args['--force']

    if not force and get_local_date() >= get_upstream_date():
        log.info('Local database is up to date.')
        return

    log.info('Downloading data...')
    download_data()

    log.info('Loading data...')
    load_data()


def cmd_create_schema(args):
    create_schema()


def cmd_drop_schema(args):
    drop_schema()


def main():
    args = validate_data(docopt(__doc__, help=True))

    log.setLevel(args['--log-level'])

    if args['update']:
        cmd_update(args)
    elif args['upstream-date']:
        cmd_upstream_date(args)
    elif args['create-schema']:
        cmd_create_schema(args)
    elif args['drop-schema']:
        cmd_drop_schema(args)


if __name__ == '__main__':
    main()
