# -*- coding: utf-8 -*-
from sqlalchemy import Column, Date, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Version(Base):
    __tablename__ = 'tz_version'

    version_date = Column(Date, primary_key=True)

    def __repr__(self):
        return "<Version(version_date='{0}')>".format(self.version_date)


class Country(Base):
    __tablename__ = 'tz_country'

    code = Column(String(2), primary_key=True)
    name = Column(String(45), nullable=False)

    def __repr__(self):
        return "<Country(code='{0}', name='{1}')>".format([self.code,
                                                           self.name])


class Timezone(Base):
    __tablename__ = 'tz_timezone'

    zone_id = Column(Integer, primary_key=True)
    abbreviation = Column(String(6), nullable=False)
    time_start = Column(Integer, primary_key=True)
    gmt_offset = Column(Integer, nullable=False)
    dst = Column(String(1), nullable=False)

    def __repr__(self):
        return ("<Timezone(zone_id={0}, abbreviation='{1}',"
                " time_start='{2}', gmt_offset='{3}', dst='{4}')>".format(
                    [self.zone_id, self.abbreviation, self.time_start,
                     self.gmt_offset, self.dst]))


class Zone(Base):
    __tablename__ = 'tz_zone'

    id = Column(Integer, primary_key=True)
    country_code = Column(String(2), nullable=False)
    name = Column(String(35), nullable=False)

    def __repr__(self):
        return ("<Timezone(zone_id={0}, abbreviation='{1}',"
                " time_start='{2}')>".format(
                    [self.id, self.country_code, self.name]))
