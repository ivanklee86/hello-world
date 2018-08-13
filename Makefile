SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DB_NAME := test.db

# Runs Hello World via Flask (for testing only!)
run:
	export PYTHONPATH='.'; \
	export FLASK_CONFIG='development'; \
	export FLASK_ENV='development'; \
	export APP_DATABASE_URI=sqlite:///${ROOT_DIR}/${DB_NAME}; \
	flask run; \

# Run Hello World via gunicorn (pre-Docker testing)
run-gunicorn:
	export PYTHONPATH='.'; \
	export FLASK_CONFIG='development'; \
	export FLASK_ENV='development'; \
	export APP_DATABASE_URI=sqlite:///${ROOT_DIR}/${DB_NAME}; \
	gunicorn --config gunicorn_config.py wsgi; \

# Run service in Docker.
run-docker:
	docker run -it -p 5000:5000 --env-file envfile.txt --name hello-world --rm  hello-world:latest

# Build Docker container
build:
	docker build -t hello-world .

database: delete-db create-db

clean: delete-db

create-db:
	# Create empty Sqlite database
	sqlite3 ${DB_NAME} "create table aTable(field1 int); drop table aTable;"

delete-db:
	rm -rf ${DB_NAME}