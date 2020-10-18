from requests import post as p

username = input('Enter a username: ')

while True:
    query = input(f'{username}: ')
    r = p(f'http://127.0.0.1:8000/bot?query={query}')
    print('Bot:', r.json()['bot_response'])
