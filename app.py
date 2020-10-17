from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

app = Flask(__name__)
cb = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(cb)

trainer.train(
    'chatterbot.corpus.english'
)

@app.route('/bot', methods=['POST'])
def chatbot_api():
    return jsonify(
        {'user_message' : request.args.get('message'),
        'bot_response': str(cb.get_response(request.args.get('message'))),
        'response': 200}
    )

if __name__ == '__main__':
    app.run(debug=True, port=8090)