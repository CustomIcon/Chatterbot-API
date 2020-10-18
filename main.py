from fastapi import FastAPI
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time

app = FastAPI()
cb = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(cb)

trainer.train(
    'chatterbot.corpus.french',
    'chatterbot.corpus.english',
    'chatterbot.corpus.portuguese',
    'chatterbot.corpus.german',
    'chatterbot.corpus.spanish',
    'chatterbot.corpus.italian'
)

@app.post('/bot')
async def chatbot_api(query: str):
    start = time.time()
    return {
        'response': int(200),
        'query' : query,
        'bot_response': str(
                cb.get_response(query)
            ),
        'time_taken': str(
                f'{(round((time.time() - start)* 1000, 3))}ms'
            )
        }