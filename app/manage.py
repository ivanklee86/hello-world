# pylint: disable=unused-import
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app
from app.extensions import db
import app.modules.books.models

APP = create_app()
MIGRATE = Migrate(APP, db)

MANAGER = Manager(APP)
MANAGER.add_command('db', MigrateCommand)

if __name__ == '__main__':
    MANAGER.run()
