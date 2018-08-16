# Flask demo app

[![pipeline status](https://gitlab.com/hamsterwheel/hello-world/badges/master/pipeline.svg)](https://gitlab.com/hamsterwheel/hello-world/commits/master) [![coverage report](https://gitlab.com/hamsterwheel/hello-world/badges/master/coverage.svg)](https://gitlab.com/hamsterwheel/hello-world/commits/master) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

This is a small sandbox Flask app to experiment with deployment best-practices and automated deployments
of non-trivial applications.

Features:
* Sandbox app
	* Requirement management using `pipenv`
	* JSON API build with Flask & GUnicorn
	* SQLAlchemy ORM interfacing with SQLLITE (dev) and PostgreSQL (prod)
	* Web UI
* Deployments
	* Makefile that gets you up & developing fast!
	* Database management via flask-migrate & Alembic
	* Gitlab CI pipleine (test, build Docker image, CD to staging, manual deployment to production)
	* Configured via environment variables (env file, Config Map, etc.)

## Development

### Local development
1. Use `pipenv install` to create a virtualenv with requirements.
2. Create a local database with `make database`.
3. Start Flask server using `make run`.

To run unit tests, add root dir to your PYTHONPATH (`export PYTHONPATH=".:$PYTHONPATH"`) and run tests with `py.test`.

### Local deployment testing
1. Run Hello World using gunicorn + Flask with `make run-gunicorn`.
2. Sanity check app!

## Deployment

You can build the Docker image using `make build` or by running the Docker command directly:

> docker build -t hello-world .

You can run the Docker image using the following Docker command:

> docker run -it -p PORT:5000 --env-file [ENV FILE] --name hello-world --rm  hello-world:latest

Arguments:
* PORT - Target port.
* ENV FILE - Text file with environment variables in VAR=VAL form (i.e. standard Docker env file format).  This lets you configure your app!

For example:
> docker run -it -p 5000:5000 --env-file envfile.txt --name hello-world --rm  hello-world:latest

## Configuration

The following environment variables can be configured:

### General
* FLASK_CONFIG - Environment for app (development, staging, production)
* LOG_LEVEL - Log level (DEUG, INFO, etc.)
* LOG_FORMATTER - TEXT for text logs, JSON for ELK-friendly logs.

### Production / General

Postgres configuration:
* DB_USER
* DB_PASS
* DB_HOST
* DB_PORT
* DB_NAME

### Development
* APP_DATABASE_URI (mandatory): points to the backing database.

## API

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/1523535/RWTmtHSP)

## Database
### Install
1. To bootstrap a database, set up the appropriate configuration (i.e. via a source file).
2. Go to the `./app` folder.
3. Run `python manage.py db upgrade`

### Creating a change set.
1. Make appropriate changes to your DB models.
2. Run `python manage.py db migrate`

# License

This code is licensed under the MIT License.
