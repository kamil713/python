import connect_to_api
import nanoid
import html
import json

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

# print(type(newData))
# print(newData)

#print(json.dumps(newData, indent=2))
