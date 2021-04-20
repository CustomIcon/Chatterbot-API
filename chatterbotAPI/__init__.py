from fastapi import FastAPI
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
from os import environ
from configparser import ConfigParser

DB_URL = environ.get('DB_URL', None)
PORT = environ.get('PORT', None)

app = FastAPI()

config_file = f"chatbot.ini"
config = ConfigParser()
config.read(config_file)

adapters = [
    'BestMatch',
    'LogicAdapter',
    'UnitConversion',
    'TimeLogicAdapter',
    'MathematicalEvaluation',
    'SpecificResponseAdapter',
]

_adapters = []
for adapter in adapters:
    _adapters.append({'import_path', f'chatterbot.logic.{adapter}'})

cb = ChatBot(
    'Bot',
    logic_adapers=_adapters,   
    # storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    # database_uri=DB_URL or config.get('database', 'mongo_url'),
)

trainer = ChatterBotCorpusTrainer(cb)

trainer.train(
    # Uncomment each line to train from chatterbot's corpus
    # 'chatterbot.corpus.french',
    'chatterbot.corpus.english',
    # 'chatterbot.corpus.portuguese',
    # 'chatterbot.corpus.german',
    # 'chatterbot.corpus.spanish',
    # 'chatterbot.corpus.italian'
)
