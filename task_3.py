# # *Задача №3(необязательная)
# Самый важный сайт для программистов это [stackoverflow](https://stackoverflow.com/). И у него тоже есть [API](https://api.stackexchange.com/docs) Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг 'Python'. Для этого задания токен не требуется.

import requests
from pprint import pprint

def python_questions(fromdate):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': fromdate, "order": "desc", 'sort': 'activity', "tagged": "python", "site": "stackoverflow"}
    responce = requests.get(url, params=params).json()
    pprint(responce)

if __name__ == "__main__":
    python_questions(1720887504)