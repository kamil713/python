import connect_to_api
import nanoid
import html

def setting_answers(answers, correct_answer):
    answers_list = []
    for answer in answers:
        d = dict()
        d['answer'] = answer
        d['correct'] = True if answer == correct_answer else False
        answers_list.append(d)
    return answers_list


newData = []
for item in connect_to_api.data['results']:
    d = dict()
    d['id'] = nanoid.generate(size=10)
    d['category'] = item['category']
    d['question'] = html.unescape(item['question'])
    all_answers = html.unescape(item['incorrect_answers']) + [html.unescape(item['correct_answer'])]
    all_answers.sort()
    d['answers'] = setting_answers(all_answers, html.unescape(item['correct_answer']))
    newData.append(d)

'''
2
Zaciagamy dane z connect_to_api.py wrzucamy je w petle 
aby utworzyc nowych komplet danych tylko tych ktorych konkretnie potrzebujemy
do wykorzystania w quizie a zarazem ktore chcemy przerobic dla ulatwienia pozniejszej logiki.
Dla przykladu tworzymy obiekt answers ktory bedzie zawierac
odpowiedzi z podzialem na prawidlowe nieprawidlowe
zamiast pobierac wszystko pojedynczno i pisac dodatkowo logike w pozniejszych etapach
zalatwiamy to jedna funkcja setting_answers.
Dodatkowo kazdy zestaw dostaje unikatowe id dzieki bibliotece 'nanoid' co ulatwi nam prace z danymi
rowniez w pozniejszym etapie gdy bedziemy sprawdzac czy odp jest prawidlowa.
Korzystamy tutaj jeszcze z jednej biblioteki mianowicie 'html' co jest rowniez powodem
czemu iterujemy po danych i tworzymy nowe poniewez API zwraca nam dane ktore zawieraja odwolania
do znakow jak &#039; - odpowiednik 'apostrofu' a my zamieniamy je na znaki Unicode.
'''