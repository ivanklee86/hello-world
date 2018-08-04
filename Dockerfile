
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

# Start flask
# ---------------------------------------------------------------------- #
ENTRYPOINT ["python"]
CMD ["app"]