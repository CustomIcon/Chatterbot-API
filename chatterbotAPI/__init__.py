from fastapi import FastAPI
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
from os import environ

DB_URL = environ.get('DB_URL', None)

app = FastAPI()
cb = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri=DB_URL
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