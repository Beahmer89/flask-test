import requests


def get_credit_lines():
    response = requests.get('https://www.randomnumberapi.com/api/v1.0/random')
    response.raise_for_status()
    return response.json()
