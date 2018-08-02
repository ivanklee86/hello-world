from . import status
from . import entries

def init_app(app, **kwargs):
    modules = [
            status,
            entries
            ]

    for module in modules:
        module.init_app(app)
