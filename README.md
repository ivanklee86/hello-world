# Flask demo app

[![pipeline status](https://gitlab.com/hamsterwheel/hello-world/badges/master/pipeline.svg)](https://gitlab.com/hamsterwheel/hello-world/commits/master) [![coverage report](https://gitlab.com/hamsterwheel/hello-world/badges/master/coverage.svg)](https://gitlab.com/hamsterwheel/hello-world/commits/master) [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/602ebf2c53d3cea6b560)

This is a small demo app created in Flask created to exercise automated deployments
of non-trivial applications.

* Configuration based on environment variables
* Database-backed entries
* JSON API
* Stateless
* Support for X-Request-ID header for request tracking
* Logging with JSON to stdout

## Model

The only model defined for the application is the model of an `Entry`.

An `Entry` is composed by the following fields:
* id: unique identifier for an entry. This field is generated automatically 
	and	cannot be modified.
* description: a description for the `Entry`. 
* comment: a comment over the `Entry`. 

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

## Deployment

The requirements for the application are listed in `requirements.txt`.

## API

The following endpoints are offered:

* /api/v1/entries
	* parameters: none
	* methods: GET
	* description: list all entries in the database
	* accepts: all formats
	* returns: application/json

* /api/v1/entries
	* parameters: JSON object representing an `Entry`
	* methods: POST
	* description: create a new entry
	* accepts: application/json
	* returns: application/json

* /api/v1/entries/<id>
	* parameters: JSON object representing an `Entry`
	* methods: POST
	* description: update an existing `Entry`
	* accepts: application/json
	* returns: application/json

* /api/v1/entries/<id>
	* parameters: entry id
	* methods: DELETE
	* description: remove an entry from the database
	* accepts: all formats
	* returns: application/json

* /api/v1/status
	* parameters: none
	* methods: GET
	* description: return "OK" if the application is reachable
	* accepts: all formats
	* returns: application/json

# License

This code is licensed under the MIT License.
