SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DB_NAME := test.db

#-----------------------------------------------------------------------
# Rules of Rules : Grouped rules that _doathing_
#-----------------------------------------------------------------------

# Cleans up local DB and orphaned Docker resources
clean: delete-db clean-docker

# Creates a local DB with bootstraped database objects
database: delete-db create-db apply-db-ddl

# Run tests & linters
test: lint pytest

#-----------------------------------------------------------------------
# Testing & linting
#-----------------------------------------------------------------------

lint:
	export PYTHONPATH='${ROOT_DIR}' && \
	pylint app && \
	mypy app;

pytest:
	export PYTHONPATH='${ROOT_DIR}'; \
	py.test tests;

#-----------------------------------------------------------------------
# Run Rules
#-----------------------------------------------------------------------

# Runs Hello World
run:
	export PYTHONPATH='${ROOT_DIR}'; \
	export FLASK_CONFIG='development'; \
	export FLASK_ENV='development'; \
	export APP_DATABASE_URI=sqlite:///${ROOT_DIR}/${DB_NAME}; \
	flask run; \

# Run Hello World via gunicorn (pre-Docker testing)
run-gunicorn:
	export PYTHONPATH='${ROOT_DIR}'; \
	export FLASK_CONFIG='development'; \
	export FLASK_ENV='development'; \
	export APP_DATABASE_URI=sqlite:///${ROOT_DIR}/${DB_NAME}; \
	gunicorn --config gunicorn_config.py wsgi; \

# Run service in Docker.
run-docker:
	docker run -it -p 5000:5000 --env-file envfile.txt --name hello-world --rm  hello-world:latest

#-----------------------------------------------------------------------
# Docker Rules
#-----------------------------------------------------------------------

# Build Docker container
build:
	docker build -t hello-world .

# Deletes stopped containers, unused volumes, and unused networks.
clean-docker:
	docker system prune -a

#-----------------------------------------------------------------------
# Database Rules
#-----------------------------------------------------------------------

# Creates an empty sqlite db
create-db:
	# Create empty Sqlite database
	sqlite3 ${DB_NAME} "create table aTable(field1 int); drop table aTable;" \

# Runs Alembic database migration on local development database.
apply-db-ddl:
	export PYTHONPATH='${ROOT_DIR}'; \
	export FLASK_CONFIG='development'; \
	export FLASK_ENV='development'; \
	export APP_DATABASE_URI=sqlite:///${ROOT_DIR}/${DB_NAME}; \
	cd app; \
	python manage.py db upgrade

# Cleans database
delete-db:
	rm -rf ${DB_NAME}
