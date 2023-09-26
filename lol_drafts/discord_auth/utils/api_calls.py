import requests
from ..secrets import client_id, client_secret


def auth_exchange_code(code: str):
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/oauth2/login/redirect',
        'scope': 'identify'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers).json()
    return response


def auth_get_user_data(token: str):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers).json()
    return response
