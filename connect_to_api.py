import requests
import json

#categories = ['General Knowledge', 'Sport', 'Animals',
#              'Entertainment: Video Games', 'Science: Computers']
#print(categories)
#selectCategory = input('Select category: ')

URL = f'https://opentdb.com/api.php?amount=3&category=9&difficulty=easy&type=multiple'

response = requests.get(URL)

if response.status_code != requests.codes.ok:
    print('Coś poszło nie tak')
else:
    data = response.json()


#print(json.dumps(response.json(), indent=4))
