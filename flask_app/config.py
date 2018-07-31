import os


class BaseConfig(object):
    # Load config settings from environment variables
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_PORT = os.getenv('DB_PORT')

    SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s:%s/%s" % (
        DB_USER,
        DB_PASS,
        DB_HOST,
        DB_PORT,
        DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
