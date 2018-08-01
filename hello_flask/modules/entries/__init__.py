def init_app(app, **kwargs):
    from . import resources
    from .modules import Entry

    app.register_blueprint(resources.entries_blueprint)