
# ====================================================================== #
# Python CI Docker Image
# ====================================================================== #

# Base image
# ---------------------------------------------------------------------- #
FROM python:3.9
LABEL MAINTAINER="Ivan Lee"

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y sqlite3 libsqlite3-dev

# Container settings
# ---------------------------------------------------------------------- #
WORKDIR /app

ENV LC_ALL C.UTF-8
ENV LANG =C.UTF-8
EXPOSE 5000

# Install app
# ---------------------------------------------------------------------- #
COPY . /app
RUN pip install -r requirements.txt
ENV PYTHONPATH /app

# Start flask
# ---------------------------------------------------------------------- #
CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi"]