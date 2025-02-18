# Use python base image
FROM python:3.10-slim-buster

# Update packages, install uuidgen, git and clean up
RUN apt-get update \
    && apt-get install -y uuid-runtime git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Get latest version of pip
RUN pip install --upgrade pip

# copy requirements.txt to working directory, install, upgrade dependencies & remove the file
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade -r requirements.txt 
RUN rm requirements.txt
    