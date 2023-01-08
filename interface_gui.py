import customtkinter
import main

ids = []
for data in main.newData:
    category_of_quiz = data['category']
    ids.append(data['id'])

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("900x600")

user_answers = []
answers_handler = []
def value_changed(choice):
    global answers_handler
    user_answers.clear()
    count = 0

    answers_handler = [combobox_1.get(), combobox_2.get(), combobox_3.get()]

    for id in ids:
        user_answers.append([id, answers_handler[count]])
        count += 1
    print(user_answers)


quiz_boxes = []
combobox_1 = customtkinter.StringVar(value="Choose correct answer...")
combobox_2 = customtkinter.StringVar(value="Choose correct answer...")
combobox_3 = customtkinter.StringVar(value="Choose correct answer...")
def initialize_quiz():
    answers = []

    for data in main.newData:
        if answers:
            quiz_boxes.append(customtkinter.CTkComboBox(frame, values=answers, command=value_changed))
        answers.clear()
        quiz_boxes.append(customtkinter.CTkLabel(master=frame, text=data['question'], font=("Roboto", 14)))
        for answer in data['answers']:
            answers.append(answer['answer'])

    quiz_boxes.append(customtkinter.CTkComboBox(frame, values=answers, command=value_changed))

    for i in range(len(quiz_boxes)):
        quiz_boxes[i].pack(pady=12, padx=10)

    quiz_boxes[1].configure(variable=combobox_1)
    quiz_boxes[3].configure(variable=combobox_2)
    quiz_boxes[5].configure(variable=combobox_3)

    return quiz_boxes


def change_state():
    if button.cget("state") == 'normal':
        button.configure(state='disabled')
    else:
        button.configure(state='normal')


score = 0
correct_answers = [None] * 3
def check_answers():
    global score
    counter = 0

    for data in main.newData:
        if data['id'] == user_answers[counter][0]:
            print(data['answers'])
            for answer in data['answers']:
                if answer['answer'] == user_answers[counter][1] and answer['correct']:
                    score += 1
                    correct_answers[counter] = True
                elif answer['answer'] == user_answers[counter][1] and not answer['correct']:
                    correct_answers[counter] = False

        if counter != 3:
            counter += 1
        print(correct_answers)

def change_styles():
    counter = 0

    for i in range(len(quiz_boxes)):
        if isinstance(quiz_boxes[i], customtkinter.CTkComboBox):
            print(counter)
            if correct_answers[counter]:
                quiz_boxes[i].configure(border_width=2, border_color='green')
            else:
                quiz_boxes[i].configure(border_width=2, border_color='red', state='disabled')
            counter += 1

def finish_game():
    error = customtkinter.CTkLabel(master=frame, text="Something went wrong", text_color='red', font=("Roboto", 16))

    checker = 0
    for a in answers_handler:
        print(a)
        if a != 'Choose correct answer...':
            checker += 1

    print(checker)
    if checker == 3:
        change_state()
        check_answers()
        change_styles()
        result = customtkinter.CTkLabel(master=frame, text=f"Your scorred {score}/3 correct answers",
                                        font=("Roboto", 16))
        result.pack(pady=12, padx=10)
        if score == 3:
            congratulations = customtkinter.CTkLabel(master=frame, text="Congratulations", text_color='green',
                                        font=("Roboto", 16))
            congratulations.pack(pady=12, padx=10)
    else:
        error.pack(pady=12, padx=10)
        error.after(1000, lambda: error.destroy())


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# TYTUŁ
title = customtkinter.CTkLabel(master=frame, text="QUIZ GAME", font=("Roboto", 36))
title.pack(pady=12, padx=10)

# KATEGORIA
category = customtkinter.CTkLabel(master=frame, text=category_of_quiz, font=("Roboto", 16))
category.place(x=550, y=22)

# QUIZ
initialize_quiz()

button = customtkinter.CTkButton(master=frame, text="Check answers", command=finish_game)
button.pack(pady=12, padx=10)

root.mainloop()
