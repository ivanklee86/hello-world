
# ====================================================================== #
# Python CI Docker Image
# ====================================================================== #

# Base image
# ---------------------------------------------------------------------- #
FROM python:3.7.0-stretch
LABEL MAINTAINER="Ivan Lee"

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

# Config app
# ---------------------------------------------------------------------- #
ENV FLASK_CONFIG staging

ENV DB_USER cnpnldjb
ENV DB_PASS Yc4MicwfIrewPagGM5bQOoXQ_UMZahxn
ENV DB_HOST elmer.db.elephantsql.com
ENV DB_PORT 5432
ENV DB_NAME cnpnldjb

# Start flask
# ---------------------------------------------------------------------- #
ENTRYPOINT ["python"]
CMD ["app"]