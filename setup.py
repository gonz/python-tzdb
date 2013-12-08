# -*- coding: utf-8 -*-
"""
tzdb
----

tzdb provides sqlalchemy models, import and update utils for the timezone
database data provided by timezonedb.com.

Links
`````

* `Source code <http://github.com/gonz/python-tzdb/>`_

"""
from setuptools import setup


setup(
    name='tzdb',
    version='0.1-dev',
    url='http://github.com/gonz/python-tzdb/',
    license='MIT',
    author='Gonzalo Saavedra',
    author_email='gonz@talduken.com',
    description='A python/sqlalchemy wrapper for the timezone '
                'database (timezonedb.com).',
    long_description=__doc__,
    packages=['tzdb'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'psycopg2',
        'SQLAlchemy==0.8.3',
        'mako',
        'requests',
        'docopt',
        'schema',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Database',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'tzdb = tzdb.scripts.tzdb_:main',
        ]
    },
)
