from . import status
from . import entries
from . import frontend

def init_app(app, **kwargs):
    modules = [
        status,
        entries,
        frontend
    ]

    for module in modules:
        module.init_app(app)
