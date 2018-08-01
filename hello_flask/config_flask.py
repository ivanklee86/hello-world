import os


CONFIG_NAME_MAPPER = {
    'development': 'hello_flask.config.DevelopmentConfig',
    'production': 'config.ProductionConfig',
    'staging': 'config.StagingConfig'
}

def config_flask(app):
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    if not env_flask_config_name:
        env_flask_config_name = 'development'
    try:
        app.config.from_object(CONFIG_NAME_MAPPER[env_flask_config_name])
    except ImportError:
        raise