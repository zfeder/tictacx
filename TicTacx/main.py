import tkinter as tk
import numpy as np
from tkinter import messagebox, DISABLED

root = tk.Tk()
root.title('Filetto')


# --- functions ---
def disable_button(widget):
    for y in range(nLato):
        for x in range(nLato):
            button = tk.Button(root, text="0", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
            button.grid(row=y, column=x)
            button.config(state=DISABLED)


def on_click(widget, x, y):
    global parziale
    global turnoInt
    if A[x][y] == 0:
        if parziale != nGiocatori:
            widget['text'] = nGiocatori - (parziale - 1)
            A[x][y] = nGiocatori - (parziale - 1)
            b = nGiocatori - (parziale - 1)
            print(A)
            print("Giocatore", b + 1, "è il tuo turno")
            turno = nGiocatori - (parziale - 1)
            parziale = parziale - 1
        if parziale == nGiocatori:
            widget['text'] = 1
            A[x][y] = 1
            print(A)
            print("Giocatore 2 è il tuo turno")
            parziale = parziale - 1
            turno = 1
        if parziale == 0:
            widget['text'] = nGiocatori
            A[x][y] = nGiocatori
            print(A)
            print("Giocatore 1 è il tuo turno")
            parziale = nGiocatori
            turno = nGiocatori

        turnoInt = int(turno)
        consecutivi = check_row(x, y, turnoInt)
        print(consecutivi)

        if consecutivi == 3:
            punteggi[turnoInt - 1] = punteggi[turnoInt - 1] + 2
        if consecutivi == 4:
            punteggi[turnoInt - 1] = (punteggi[turnoInt - 1] - 2) + 10
        if consecutivi == 5:
            punteggi[turnoInt - 1] = (punteggi[turnoInt - 1] - 10) + 50
        print(punteggi[turnoInt - 1])
        if punteggi[turnoInt - 1] == 50:
            s = "Ha vinto il giocatore " + str(turnoInt)
            messagebox.showinfo("CONGRATULAZIONI!", s)
            disable_button(widget)

    else:
        print('Casella già occupata')


def check_row(x, y, move):
    flag = True
    counter = 0
    i = 0
    while (i + y >= 0) and flag:
        if A[x][y + i] != move:
            flag = False
        else:
            counter = counter + 1
        i = i - 1
    flag = True
    i = 1
    while (i + y < nLato) and flag:
        if A[x][y + i] != move:
            flag = False
        else:
            counter = counter + 1
        i = i + 1
    return counter


def set_move(x, y, move):
    A[x][y] = move
    return move


# --- main ---
lato = input('Inserisci la grandezza della griglia: ')
print(lato)
nLato = int(lato)
Giocatori = input('Inserisci il numero di giocatori: ')
nGiocatori = int(Giocatori)
print(nGiocatori)
parziale = nGiocatori

A = np.zeros((nLato, nLato))

for y in range(nLato):
    for x in range(nLato):
        button = tk.Button(root, text="0", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
        button['command'] = lambda x=x, y=y, arg=button: on_click(arg, y, x)
        button.grid(row=y, column=x)

print("Giocatore 1 è il tuo turno")
punteggi = np.zeros(nGiocatori)


def reset():
    for y in range(nLato):
        for x in range(nLato):
            A[x][y] = 0

    for h in range(nGiocatori):
        punteggi[h] = 0

    global parziale
    parziale = nGiocatori
    global turnoInt
    turnoInt = 0

    for y in range(nLato):
        for x in range(nLato):
            button = tk.Button(root, text="0", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
            button['command'] = lambda x=x, y=y, arg=button: on_click(arg, y, x)
            button.grid(row=y, column=x)

    print("Giocatore 1 è il tuo turno")


# Create menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)


root.mainloop()
