FROM python:3.6-slim-stretch

ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

WORKDIR /root/

# Pypi package Repo upgrade
RUN pip3 install --upgrade pip setuptools

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

ENV ENV true

RUN python3 -m spacy download en

# Starting Worker
CMD ["python3","app.py"]

EXPOSE 8090