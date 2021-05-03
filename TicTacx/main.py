import tkinter as tk
from tkinter import font as tkFont

# --- functions ---
import numpy as np
#riordinamento

def on_click(widget, x, y):
    print('clicked')
    global parziale
    if A[x][y] == 0:
        if parziale != nGiocatori:
            widget['text'] = nGiocatori - (parziale - 1)
            A[x][y] = nGiocatori - (parziale - 1)
            b = nGiocatori - (parziale - 1)
            print(A)
            print("Giocatore", b+1, "è il tuo turno")
            parziale = parziale - 1
        if parziale == nGiocatori:
            widget['text'] = 1
            A[x][y] = 1
            print(A)
            print("Giocatore 2 è il tuo turno")
            parziale = parziale - 1
        if parziale == 0:
            widget['text'] = nGiocatori
            A[x][y] = nGiocatori
            print(A)
            print("Giocatore 1 è il tuo turno")
            parziale = nGiocatori

    else:
        print('Casella già occupata')

    for y in range(nLato):
        for x in range(nLato):
            for n in range(1, nLato - x):
                if A[x][y] == A[x + n][y] and A[x][y] != 0:
                    print("Consecutivo", A[x][y], A[x+n][y])



def rigaCall():
    riga = input("Scegli la riga:");
    nRiga = int(riga);
    return nRiga;


def colonnaCall():
    colonna = input("Scegli la colonna:");
    nColonna = int(colonna);
    return nColonna;


# --- main ---


root = tk.Tk()
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
        helv36 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
        button = tk.Button(root, font=helv36, height=5, width=10, text="0")
        button['command'] = lambda x=x, y=y, arg=button: on_click(arg, y, x)
        button.grid(row=y, column=x)

print("Giocatore 1 è il tuo turno")
root.mainloop()
