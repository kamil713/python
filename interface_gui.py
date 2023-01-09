import customtkinter   # moduł do tworzenia interfejsów graficznych
import main

ids = []
category_of_quiz = ''
for data in main.newData:
    category_of_quiz = data['category']
    ids.append(data['id'])

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()   # tworzymy okienko
root.geometry("900x600")    # rozmiar naszego okna

user_answers = []
answers_handler = []
# value_changed odpowiada za rejstrowanie tego czy uzytkownik wybral/zmienil odpowiedz
# po czym kompletuje te dane do powyzej zadeklarowanych tablic dzieki czemu
# mozemy je wykorzystac do takich funkcjonalnosci jak sprwadzenie poprawnosci odpowiedzi
# lub czy uzytkownik zaznaczyl wszystkie odpowiedzi zanim chce podejrzec ich poprawnosc
def value_changed(choice):
    global answers_handler
    user_answers.clear()
    count = 0

    answers_handler = [combobox_1.get(), combobox_2.get(), combobox_3.get()]

    for id in ids:
        user_answers.append([id, answers_handler[count]])
        count += 1


quiz_boxes = []
combobox_1 = customtkinter.StringVar(value="Choose correct answer...")
combobox_2 = customtkinter.StringVar(value="Choose correct answer...")
combobox_3 = customtkinter.StringVar(value="Choose correct answer...")
# initialize_quiz inicjalizuje widgety naszego quizu rozszerzajac je o odpowiednie dane z main
# gdzie main.newData zwraca nam przerobione dane pod quiz
# mozemy zauwazyc tutaj labelki ktore zwracaja pytanie oraz combobox ktore
# zwracaja nam rozwijana liste odpowiedzi do wyboru
# finalnie initialize_quiz zwraca nam liste (tablice) 'quiz_boxes'
# na ktorej bedziemy pozniej operowac i dodawac do niej funkcjonalnosci
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


# change_state zmienia status naszego buttona 'check answers' na nieklikany
# w momencie w ktorym sprawdzimy poprawnosc naszych odpowiedzi
def change_state():
    if button.cget("state") == 'normal':
        button.configure(state='disabled')
    else:
        button.configure(state='normal')


score = 0
correct_answers = [None] * 3

# check_answers sprawdza poprawnosc odpowiedzi oraz przypisuje punkty uzytkowniki
def check_answers():
    global score
    counter = 0

    for data in main.newData:
        if data['id'] == user_answers[counter][0]:
            for answer in data['answers']:
                if answer['answer'] == user_answers[counter][1] and answer['correct']:
                    score += 1
                    correct_answers[counter] = True
                elif answer['answer'] == user_answers[counter][1] and not answer['correct']:
                    correct_answers[counter] = False

        if counter != 3:
            counter += 1


# change_styles zmienai wizualnie stan aplikacji w momencie w ktorym uzytkownik
# sprawdzi porawnosc swoich odpowiedzi
def change_styles():
    counter = 0

    for i in range(len(quiz_boxes)):
        if isinstance(quiz_boxes[i], customtkinter.CTkComboBox):
            if correct_answers[counter]:
                quiz_boxes[i].configure(border_width=2, border_color='green')
            else:
                quiz_boxes[i].configure(border_width=2, border_color='red', state='disabled')
            counter += 1


# finish_game jak mowi nazwa konczy gre czyli po kliknieciu przycisku check_answers
# JESLI uzytkownik zaznaczyl wszystkie odpowiedzi wywoluja sie powyzsze funkcje
# zmieniaja kolory quizu, wylaczaja przycisk i pokazuja wynik uzytkownikowi
# w przeciwnym wypadku informuje uzytkownika o niezaznaczeniu odpowiedzi
def finish_game():
    error = customtkinter.CTkLabel(master=frame, text="Something went wrong", text_color='red', font=("Roboto", 16))

    checker = 0
    for a in answers_handler:
        if a != 'Choose correct answer...':
            checker += 1

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

# PRZYCISK CHECK_ANSWER
button = customtkinter.CTkButton(master=frame, text="Check answers", command=finish_game)
button.pack(pady=12, padx=10)

root.mainloop() # metoda mainloop blokuje okienko przed zamknieciem

'''
3
Z interface_gui uruchamiamy nasz quiz.

Tutaj mamy clou całego programu czyli interfejs naszego quizu
uzywamy tutaj przerobionych juz danych, wczesniej pobranych z API
oraz bilioteki customtkinter, która udostepnia nam gotowe widgety, motywy i tryby wyglądu.
Korzystajac z gotowych widgetow oraz iteracji po przygotowanych danych dajemy uzytkownikowi
gotowy quiz rozbudowujac jego funkcjonalnosc dzieki zdefiniowaniu powyzej konkretnych funkcji.
Funkcje maja nadane nazwy w zaleznosci od tego czym sie zajmuja i komentarze.
'''