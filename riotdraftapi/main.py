import json
import requests

api_key = 'RGAPI-b11fbdee-a6e5-4a74-91d2-2042ee53d2e5'

def get_newest_version():
    version_request = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()
    return version_request[0]


def get_champions():
    champions_request = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{get_newest_version()}/data/en_US/champion.json').json()
    return champions_request


def get_champion_icon(champion):
    url = f'http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/{champion}_0.jpg'
    return url

#
# champions = get_champions()
#
# # for champion, attributes in champions['data']:
# #     print(champion, champions['data'][champion]['id'], champions['data'][champion]['name'])
#
#
# for champion, attributes in champions['data'].items():
#     print(champion, attributes['id'], attributes['name'])


queue_id = 420  # solo queue


def get_match_by_id(matchId):
    match_id_endpoint = f'https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={api_key}'
    response = requests.get(match_id_endpoint).json()
    return response

