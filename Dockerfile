FROM python:3.7-buster

ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

WORKDIR /app/

RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y \
    sudo \
    && rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp

# Pypi package Repo upgrade
RUN pip3 install --upgrade pip setuptools

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

ENV ENV true

RUN sudo python3 -m spacy download en

# Starting Worker
CMD ["python3","app.py"]

EXPOSE 8090