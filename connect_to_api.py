import random
import requests

category_numbers = [0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

URL = f'https://opentdb.com/api.php?amount=3&category={random.choice(category_numbers)}&difficulty=easy&type=multiple'

response = requests.get(URL)

if response.status_code != requests.codes.ok:
    print('Coś poszło nie tak')
else:
    data = response.json()
