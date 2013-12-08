python-tzdb
===========

python-tzdb provides sqlalchemy models and utils to manage timezone data
from timezonedb.com.


Installation
------------

(As usual, using virtualenv is recommended)

This package is not available in pypi yet, install it using distutils:

    git clone git@github.com:gonz/python-tzdb.git
    cd python-tzdb
    python setup.py install


Models
------

Checkout the provided models in [pydb/models](https://github.com/gonz/python-tzdb/blob/master/tzdb/models.py)


Commands
--------

python-tzdb provides a tzdb command for the command line interface which
aims to help keeping the database upto date.


### tzdb upstream-date ###

Outputs the latest data update on timezonedb.com.


### tzdb update ###

Downloads and updates the database data if necesary.


### Usage ###

    Description:
      Manage the tzdb data.

    Usage:
      pydb upstream-date [--log-level=<log_level>]
      pydb update [--force] [--log-level=<log_level>]

    Options:
      -h --help                Show this screen.
      --log-level=<log_level>  Set the logging/ouput level [default: WARNING]


About timezonedb
----------------

From timezonedb.com:

    TimeZoneDB provides free time zone database for cities of the world.
    The database is licensed under Creative Commons Attribution 3.0 License.
    It contains countries name, time zones, abbreviation, GMT offset,
    and Daylight Saving Time (DST). The data is available in CSV and SQL format.

For more info visit [timezonedb.com](http://timezonedb.com/).
