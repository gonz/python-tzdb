# -*- coding: utf-8 -*-
"""
Description:
  Manage the tzdb data.

Usage:
  pydb upstream-date [--log-level=<log_level>]

Options:
  -h --help                Show this screen.
  --log-level=<log_level>  Set the logging/ouput level [default: WARNING]
"""
from __future__ import (
    print_function, unicode_literals, division, absolute_import)
import logging

from docopt import docopt
from schema import Schema, SchemaError, Use, And

from tzdb.db import get_upstream_date


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
        'upstream-date': Use(bool),
    })

    try:
        return schema.validate(args)
    except SchemaError as e:
        exit(e)


def cmd_upstream_date():
    print(get_upstream_date())


def main():
    args = validate_data(docopt(__doc__, help=True))

    log.setLevel(args['--log-level'])

    if args['upstream-date']:
        cmd_upstream_date()


if __name__ == '__main__':
    main()
