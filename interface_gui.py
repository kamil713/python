import tkinter  # moduł do tworzenia interfejsów graficznych

root = tkinter.Tk()  # tworzymy okienko
root.geometry('880x480') # rozmiar okna naszej aplikacji

# dostawiamy etykiete do okienka root, drugi argument odpowiada za to co przedstawia etykieta
# przypisujemy do zmiennej bo będziemy używać wiecej etykiet (czytelnosc itd.)
l = tkinter.Label(root, text='Aplikacja')
# funkcja pack aby etykieta pojawila sie w naszym okienku
l.pack()

def funkcjaPrzycisku():
    print('Wcisnieto przycisk')

# jak wyzej tylko dostawiamy przycisk zamiast etykiety do okna naszej aplikacji
# command wywoluje konkretna funkcje po wcisnieciu przycisku
# parametry jak width, bg, fg styluja nasz przycisk
b = tkinter.Button(root, text='Jestem Przyciskiem', width=20, bg='red', fg='blue', command=funkcjaPrzycisku)
# jak wyzej, side ustawia przycisk na konkretnej pozycji
#b.pack(side=tkinter.RIGHT)
# ustawiamy element naszej aplikacji wedlug konkretnych wspolrzednych
b.place(x=230, y=230)

root.mainloop()  # metoda mainloop blokuje okienko przed zamknieciem


