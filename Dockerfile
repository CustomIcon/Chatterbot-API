FROM python:3.6-slim-stretch

ENV PIP_NO_CACHE_DIR 1

# Pypi package Repo upgrade
RUN pip3 install --upgrade pip setuptools

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .
RUN python3 -m spacy download en \
    && python3 -m spacy download fr \
    && python3 -m spacy download pt \
    && python3 -m spacy download de \
    && python3 -m spacy download es \
    && python3 -m spacy download it_core_news_sm

# Starting Worker
CMD ["python3","-m","chatterbotAPI"]

EXPOSE 8000