import requests


# Get newest version of game
def get_newest_version():
    version_request = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()
    return version_request[0]


# Get list of champions from newest patch
def get_champions():
    champions_request = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{get_newest_version()}/data/en_US/champion.json').json()
    return champions_request
