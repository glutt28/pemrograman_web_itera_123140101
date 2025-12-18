from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from zope.sqlalchemy import register

# Base class untuk models
Base = declarative_base()

# Database session
DBSession = scoped_session(sessionmaker())


def initialize_sql(settings):
    """Initialize database connection"""
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    return engine

