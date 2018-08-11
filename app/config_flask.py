import os


CONFIG_NAME_MAPPER = {
    'development': 'app.config.DevelopmentConfig',
    'production': 'app.config.ProductionConfig',
    'staging': 'app.config.StagingConfig'
}

def config_flask(app):
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    if not env_flask_config_name:
        env_flask_config_name = 'development'

    try:
        print(env_flask_config_name)
        app.config.from_object(CONFIG_NAME_MAPPER[env_flask_config_name])
    except ImportError as exception:
        raise ImportError("Could not recognize environment configuration.  Error: %s" % exception)
