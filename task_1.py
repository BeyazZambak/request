import requests

def smartest_hero(heroes):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()

    max_intelligence = 0
    smartest_hero = None
    
    for superheroe in response:
        if superheroe['name'] in heroes:
            intelligence = superheroe['powerstats']['intelligence']
            if intelligence > max_intelligence:
                max_intelligence = intelligence
                smartest_hero = superheroe['name']

    print(smartest_hero)


if __name__ == "__main__":
    smartest_hero(["Hulk", "Captain America", "Thanos"])