from requests import post as p
from chatterbotAPI import PORT, config

username = input('Enter a username: ')

while True:
    query = input(f'{username}: ')
    r = p(f'http://0.0.0.0:{PORT or config.get("server", "port")}?query={query}')
    print('Bot:', r.json()['response']['bot'])
