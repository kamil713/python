import requests
import random

category_numbers = [0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

URL = f'https://opentdb.com/api.php?amount=3&category={random.choice(category_numbers)}&difficulty=easy&type=multiple'

response = requests.get(URL)

if response.status_code != requests.codes.ok:
    print('Coś poszło nie tak')
else:
    data = response.json()

'''
1
Używamy biblioteki requests do wykonania zapytania 'get' do API
w zapytaniu uzylem biblioteki random aby kazde zapytanie losowalo inna kategorie quizu
to co zwroci nam get przpisujemy do zmiennej response.
Chcemy się upewnić że zapytanie się powiodło przy pomocy status_code stad ten if...
'''
