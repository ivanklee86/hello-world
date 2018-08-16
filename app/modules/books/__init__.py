# pylint: disable=unused-variable
def init_app(app, **kwargs):
    from . import resources
    from .models import Book

    app.register_blueprint(resources.books_blueprint)
