def init_app(app, **kwargs):
    from . import resources
    from .models import Entry

    app.register_blueprint(resources.entries_blueprint)