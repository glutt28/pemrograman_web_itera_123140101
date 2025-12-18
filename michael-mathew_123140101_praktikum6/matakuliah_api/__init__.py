from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import (
    DBSession,
    Base,
)


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_tm')
    
    # CORS handler manual (karena pyramid-cors tidak tersedia)
    from pyramid.events import NewResponse
    from pyramid.events import subscriber
    
    @subscriber(NewResponse)
    def add_cors_headers(event):
        """Add CORS headers to all responses"""
        event.response.headerlist.extend((
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'),
            ('Access-Control-Allow-Headers', 'Content-Type, Authorization'),
        ))
    
    # Database setup
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    
    # Register Zope transaction extension
    from zope.sqlalchemy import register
    register(DBSession)
    
    # Include routes
    config.include('.routes')
    
    # Scan for views
    config.scan('.views')
    
    return config.make_wsgi_app()

