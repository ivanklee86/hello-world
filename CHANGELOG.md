CHANGES IN VERSION 0.3=4.0 (from 0.3.0)
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