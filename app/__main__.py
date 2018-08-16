from app import create_app
from app.extensions.sqlalchemy import create_db

if __name__ == '__main__':
    APP = create_app()
    create_db.create_db(APP)
    APP.run(host='0.0.0.0')
