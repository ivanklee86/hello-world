# pylint: disable=unused-variable
def init_app(app, **kwargs):
    from . import resources

    app.register_blueprint(resources.books_blueprint)
