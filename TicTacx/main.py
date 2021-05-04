import tkinter as tk
from tkinter import font as tkFont
import numpy as np

root = tk.Tk()
root.title('Filetto')


# --- functions ---
def on_click(widget, x, y):
    global parziale
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
        prova = checkRiga(x, y, turnoInt)
        print(prova)

    else:
        print('Casella già occupata')


def checkRiga(x, y, move):
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
    return counter


def setMove(x, y, move):
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
root.mainloop()
