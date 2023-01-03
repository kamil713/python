import customtkinter
import main
import json

# print(json.dumps(main.newData[0], indent=2))

test123 = []
for data in main.newData:
    test123.append(data['category'])
    category_of_quiz = data['category']

print(category_of_quiz)
print(test123)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("900x600")


def initialize_question_labes():
    questions = []

    for data in main.newData:
        questions.append(customtkinter.CTkLabel(master=frame, text=data['question'], font=("Roboto", 16)))

    for i in range(len(questions)):
        questions[i].pack(pady=12, padx=10)

    return questions


def initialize_quiz():
    questions = []
    answers = []
    quiz_boxes = []

    for data in main.newData:
        if answers:
            quiz_boxes.append(customtkinter.CTkComboBox(frame, values=answers))
        answers.clear()
        quiz_boxes.append(customtkinter.CTkLabel(master=frame, text=data['question'], font=("Roboto", 14)))
        for answer in data['answers']:
            answers.append(answer['answer'])

    quiz_boxes.append(customtkinter.CTkComboBox(frame, values=answers))

    for i in range(len(quiz_boxes)):
        print()
        quiz_boxes[i].pack(pady=12, padx=10)

    return quiz_boxes


def login():
    print('dupa')


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# TYTUŁ
title = customtkinter.CTkLabel(master=frame, text="QUIZ GAME", font=("Roboto", 36))
title.pack(pady=12, padx=10)

# KATEGORIA
category = customtkinter.CTkLabel(master=frame, text=category_of_quiz, font=("Roboto", 16))
category.place(x=600, y=25)

# QUIZ
initialize_quiz()

button = customtkinter.CTkButton(master=frame, text="Check answers", command=login)
button.pack(pady=12, padx=10)

root.mainloop()
