SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DB_NAME := test.db


run:
	export PYTHONPATH='.'; \
	export FLASK_CONFIG='development'; \
	export APP_DATABASE_URI=sqlite:///${ROOT_DIR}/${DB_NAME}; \
	flask run; \

database: delete-db create-db

clean: delete-db

create-db:
	# Create empty Sqlite database
	sqlite3 ${DB_NAME} "create table aTable(field1 int); drop table aTable;"

delete-db:
	rm -rf ${DB_NAME}