from fastapi import FastAPI
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
from os import environ
from configparser import ConfigParser

DB_URL = environ.get('DB_URL', None)

app = FastAPI()

config_file = f"chatbot.ini"
config = ConfigParser()
config.read(config_file)


cb = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri=DB_URL if DB_URL is not None else config.get('database', 'mongo_url'),
)

trainer = ChatterBotCorpusTrainer(cb)

trainer.train(
    # Uncomment each line to train from chatterbot's corpus
    # 'chatterbot.corpus.french',
    # 'chatterbot.corpus.english',
    # 'chatterbot.corpus.portuguese',
    # 'chatterbot.corpus.german',
    # 'chatterbot.corpus.spanish',
    # 'chatterbot.corpus.italian'
)