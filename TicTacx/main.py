import tkinter as tk


# --- functions ---

def on_click(widget, y, x, A):
    print('clicked')
    widget['text'] = 1
    A[y][x] = "1"
    print(A)


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
print(lato);
nLato = int(lato);
Giocatori = input('Inserisci il numero di giocatori: ')
nGiocatori = int(Giocatori);
print(nGiocatori);

A = [[0 for x in range(nLato)], [0 for x in range(nLato)]]

for y in range(nLato):
    for x in range(nLato):
        button = tk.Button(root, text="0")
        button['command'] = lambda arg=button: on_click(arg, y, x, A)
        button.grid(row=y, column=x)

root.mainloop()
