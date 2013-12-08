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

Then you'll need to create the database and set the `TZDB_DATABASE_URI`
env variable with the database uri string:

    export TZDB_DATABASE_URI='postgresql://gonz:secret@localhost/tzdb'

Create the schema:

    tzdb create-schema

And finally download the data and populate the database:

    tzdb update


Models
------

Checkout the provided models in [pydb/models](https://github.com/gonz/python-tzdb/blob/master/tzdb/models.py)


Commands
--------

python-tzdb provides a tzdb command for the command line interface which
aims to help keeping the database upto date.


### `tzdb upstream-date` ###

Outputs the latest data update on timezonedb.com.

### `tzdb update` ###

Downloads and updates the database data if necesary.

### `tzdb create-schema` ###

Creates the database tables.

### `tzdb drop-schema` ###

Drops all tables.

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


License
-------

    The MIT License (MIT)

    Copyright (c) 2013 Gonzalo Saavedra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
