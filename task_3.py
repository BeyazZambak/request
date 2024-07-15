import requests
from pprint import pprint

def python_questions(fromdate):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': fromdate, "order": "desc", 'sort': 'activity', "tagged": "python", "site": "stackoverflow"}
    responce = requests.get(url, params=params).json()
    pprint(responce)

if __name__ == "__main__":
    python_questions(1720887504)