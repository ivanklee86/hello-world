CHANGES IN VERSION 1.0.2 (from 1.0.0)
===================================

#### General
* Added gevent as worker class.

CHANGES IN VERSION 1.0.1 (from 1.0.0)
===================================

#### General
* Reorganized Makefile.
* Added Alembic migration to local db creation.

CHANGES IN VERSION 1.0.0 (from 0.4.2)
===================================

#### General
* Re-formatted app to a "favorite books" theme.
* Implemented Alembic (via flask-manifest) for database management.
* Cleanup for public fork.

CHANGES IN VERSION 0.4.2 (from 0.4.0)
===================================

#### General
* Fixed logging in staging/prod.
* Implemented Marshmallow schema on top of SQLAlchemy ORM.

CHANGES IN VERSION 0.4.0 (from 0.3.0)
===================================

#### General
* Now with more pipenv!

CHANGES IN VERSION 0.3.0 (from 0.2.1)
===================================

#### General
* Added `frontend` module to serve PoC frontend.
* Implemented Foundation styling.
* Added gunicorn WSGI configuration.

#### Build
* Added `make` commands for:
    * Running flask with gunicorn
    * Building docker image locally
    * Running flask in a docker container
* Pylint to CI