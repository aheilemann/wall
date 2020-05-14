FROM python:3.5.9-slim-buster

# Install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gcc && \
    apt-get clean

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory
RUN mkdir /code
WORKDIR /code

# Install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# Copy local code to the container image.
COPY . /code/

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run development server
CMD python ./manage.py runserver 0.0.0.0:$PORT
