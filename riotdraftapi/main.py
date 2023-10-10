import json
import requests
import random
import time

api_keys = ['your', 'api', 'keys']


def random_key():
    return random.choice(api_keys)


api_key = random_key()


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


def get_players_in_division(region, queue='RANKED_SOLO_5x5', tier='CHALLENGER', division='I'):
    endpoint = f'https://{region}.api.riotgames.com/lol/league-exp/v4/entries/{queue}/{tier}/{division}?page=1&api_key={api_key}'
    response = requests.get(endpoint).json()
    return response


def summonerid_to_puuid(region, summonerId):
    endpoint = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{summonerId}?api_key={api_key}'
    response = requests.get(endpoint).json()
    return response['puuid']


def get_player_history(region: str, puuid: str, count=20):
    endpoint = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&count={count}&api_key={api_key}'
    response = requests.get(endpoint).json()
    return response


def get_match_by_id(region: str, matchId: str):
    match_id_endpoint = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={random_key()}'
    response = requests.get(match_id_endpoint).json()
    return response


# EUW1, KR, NA1
# asia, europe, americas
def feed_backend(region='asia', server='kr'):
    matches_done = []
    player_list = get_players_in_division(server)
    headers = {'Content-Type': 'application/json'}
    for player in player_list:
        puuid = summonerid_to_puuid(server, player['summonerId'])
        match_history = get_player_history(region, puuid, 5)
        for match in match_history:
            if match not in matches_done:
                match_json = get_match_by_id(region, match)
                requests.post('http://192.168.15.115:8000/recive-match-data/', data=json.dumps(match_json), headers=headers)
                matches_done.append(match)
                time.sleep(0.5)
                print(match, 'added.')
            else:
                print(match, 'skipped.')


feed_backend('asia', 'kr')
