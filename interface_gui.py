import customtkinter
import main
import json

# print(json.dumps(main.newData[0], indent=2))

test123 = []
for data in main.newData:
    test123.append(data['category'])
    category_of_quiz = data['category']

#print(category_of_quiz)
#print(test123)
#print(json.dumps(main.newData, indent=2))

#tu zrobic tablice

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("900x600")

user_answers = []
def value_changed(choice):
    user_answers.append(choice)
    print(user_answers)


quiz_boxes = []
def initialize_quiz():
    answers = []

    # state='disabled'
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
        #print(quiz_boxes[i])
        #if isinstance(quiz_boxes[i], customtkinter.CTkComboBox):
            #quiz_boxes[i].bind('<Leave>', value_changed)


    return quiz_boxes

def change_state():
    if button.cget("state") == 'normal':
        button.configure(state='disabled')
    else:
        button.configure(state='normal')

def finish_game():
    result = customtkinter.CTkLabel(master=frame, text="Your scorred 0/3 correct answers", font=("Roboto", 16))
    error = customtkinter.CTkLabel(master=frame, text="Something went wrong", text_color='red', font=("Roboto", 16))

    if len(user_answers) == 3:
        result.pack(pady=12, padx=10)
        change_state()
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
