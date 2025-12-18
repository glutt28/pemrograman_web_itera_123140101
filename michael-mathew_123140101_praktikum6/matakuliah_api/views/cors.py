"""
CORS handler untuk aplikasi
"""
from pyramid.view import view_config
from pyramid.response import Response


@view_config(request_method='OPTIONS')
def options_view(request):
    """Handle OPTIONS preflight requests untuk CORS"""
    response = Response()
    response.headerlist.extend((
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'),
        ('Access-Control-Allow-Headers', 'Content-Type, Authorization'),
        ('Access-Control-Max-Age', '3600'),
    ))
    return response

