from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Picture(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    filename = Column(Text)
    image_effect = Column(Text)
    exposure_mode = Column(Text)
    awb_mode = Column(Text)
    resolution = Column(Text)
    ISO = Column(Integer)
    exposure_time = Column(Text)
    date = Column(Text)
    timestamp = Column(Text)
    filesize = Column(Integer)

class Settings(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    image_width = Column(Integer)
    image_height = Column(Integer)
    timelapse_interval = Column(Integer)
    timelapse_time = Column(Integer)
    exposure_mode = Column(Text)
    image_effect = Column(Text)
    awb_mode = Column(Text)
    image_ISO = Column(Text)
    image_rotation = Column(Text)

class Timelapse(Base):
    __tablename__ = 'timelapse'
    id = Column(Integer, primary_key=True)
    filename = Column(Text)
    timeStart = Column(Text)
    image_effect = Column(Text)
    exposure_mode = Column(Text)
    awb_mode = Column(Text)
    timeEnd = Column(Text)

Index('my_index', Picture.filename, unique=True, mysql_length=255)
