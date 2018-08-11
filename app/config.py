import os


class BaseConfig():
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

    LOG_LEVEL = os.getenv('LOG_LEVEL')
    LOG_FORMATTER = os.getenv('LOG_FORMATTER')


class ProductionConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    LOG_LEVEL = "DEBUG"
    LOG_FORMATTER = "TEXT"

    SQLALCHEMY_DATABASE_URI = os.getenv('APP_DATABASE_URI')
