from . import status
from . import books
from . import frontend

def init_app(app, **kwargs):
    modules = [
        status,
        books,
        frontend
    ]

    for module in modules:
        module.init_app(app)
