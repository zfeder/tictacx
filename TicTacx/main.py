import tkinter as tk
import numpy as np
import tksheet
from tkinter import messagebox, DISABLED

root = tk.Tk()
root.title('Filetto')


# --- functions ---
def disable_button(widget):
    for y in range(nLato):
        for x in range(nLato):
            button = tk.Button(root, text="End", font=("Helvetica", 20), height=1, width=5)
            button.grid(row=y, column=x, pady=2, padx=2)
            button.config(state=DISABLED)


def on_click(widget, x, y):
    global parziale
    global turnoInt
    if A[x][y] == 0:

        if nGiocatori == 2:
            if parziale == nGiocatori:
                widget['text'] = nomiGiocatori[0]
                A[x][y] = 1
                print(A)
                turnoGicoatore = ("Giocatore 2 è il tuo turno")
                parziale = parziale - 1
                turno = 1
            elif parziale == 1:
                widget['text'] = nomiGiocatori[nGiocatori - 1]
                A[x][y] = nGiocatori
                print(A)
                turnoGicoatore = ("Giocatore 1 è il tuo turno")
                parziale = nGiocatori
                turno = nGiocatori
        else:
            if parziale != nGiocatori:
                widget['text'] = nomiGiocatori[(nGiocatori - (parziale - 1)) - 1]
                A[x][y] = nGiocatori - (parziale - 1)
                b = nGiocatori - (parziale - 1)
                print(A)
                turnoGicoatore = ("Giocatore", b + 1, "è il tuo turno")
                turno = nGiocatori - (parziale - 1)
                parziale = parziale - 1
            if parziale == nGiocatori:
                widget['text'] = nomiGiocatori[0]
                A[x][y] = 1
                print(A)
                print("Giocatore 2 è il tuo turno")
                parziale = parziale - 1
                turno = 1
            if parziale == 0:
                widget['text'] = nomiGiocatori[nGiocatori - 1]
                A[x][y] = nGiocatori
                print(A)
                print("Giocatore 1 è il tuo turno")
                parziale = nGiocatori
                turno = nGiocatori

        turnoInt = int(turno)
        consecutiviRighe = check_row(x, y, turnoInt)
        print("Righe Consecutive: ", consecutiviRighe)
        consecutiviColonne = check_column(x, y, turnoInt)
        print("Colonne Consecutive: ", consecutiviColonne)
        consecutiviDiagonali = check_diagonal(x, y, turnoInt)
        print("Diagonali Consecutive: ", consecutiviDiagonali)
        consecutiviAntidiagonali = check_antidiagonal(x, y, turnoInt)
        print("Anti-Diagonali Consecutive: ", consecutiviAntidiagonali)
        check_punteggio(consecutiviDiagonali)
        check_punteggio(consecutiviColonne)
        check_punteggio(consecutiviRighe)
        check_punteggio(consecutiviAntidiagonali)
        print(punteggi[turnoInt - 1])
        print(turnoGicoatore)
        data[turnoInt - 1][1] = punteggi[turnoInt - 1]
        TableModel.Data.Tables.ReloadAllData()

        if punteggi[turnoInt - 1] > 49:
            s = "CONGRATULAZIONI! Ha vinto il giocatore " + str(turnoInt)
            messagebox.showinfo("Filetto", s)
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


def check_column(x, y, move):
    flag = True
    counter = 0
    i = 0
    while (i + x >= 0) and flag:
        if A[x + i][y] != move:
            flag = False
        else:
            counter = counter + 1
        i = i - 1
    flag = True
    i = 1
    while (i + x < nLato) and flag:
        if A[x + i][y] != move:
            flag = False
        else:
            counter = counter + 1
        i = i + 1
    return counter


def check_punteggio(x):
    if x == 3:
        punteggi[turnoInt - 1] = punteggi[turnoInt - 1] + 2
    if x == 4:
        if punteggi[turnoInt - 1] == 2:
            punteggi[turnoInt - 1] = (punteggi[turnoInt - 1] - 2) + 10
        else:
            punteggi[turnoInt - 1] = (punteggi[turnoInt - 1]) + 10
    if x == 5:
        if punteggi[turnoInt - 1] == 10:
            punteggi[turnoInt - 1] = (punteggi[turnoInt - 1] - 10) + 50
        else:
            punteggi[turnoInt - 1] = (punteggi[turnoInt - 1]) + 50


def check_diagonal(x, y, move):
    flag = True
    counter = 0
    i = 0
    while (i + x >= 0 and i + y >= 0) and flag:
        if A[x + i][y + i] != move:
            flag = False
        else:
            counter = counter + 1
        i = i - 1
    flag = True
    i = 1
    while (i + x < nLato and i + y < nLato) and flag:
        if A[x + i][y + i] != move:
            flag = False
        else:
            counter = counter + 1
        i = i + 1
    return counter


def check_antidiagonal(x, y, move):
    flag = True
    counter = 0
    i = 0
    while (x + i >= 0) and flag:
        if A[x - i][y + i] != move:
            flag = False
        else:
            counter = counter + 1
        i = i + 1
    flag = True
    i = 1
    while (i + x < nLato) and flag:
        if A[x + i][y - i] != move:
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
data = [["" for x in range(2)] for y in range(nGiocatori)]
nomiGiocatori = ["" for x in range(nGiocatori)]
for x in range(nGiocatori):
    s = "Giocatore " + str(x + 1) + " inserisci il tuo nome:"
    nomiGiocatori[x] = input(s)
    data[x][0] = nomiGiocatori[x]
parziale = nGiocatori

A = np.zeros((nLato, nLato))

for y in range(nLato):
    for x in range(nLato):
        button = tk.Button(root, text="", font=("Helvetica", 20), height=1, width=5)
        button['command'] = lambda x=x, y=y, arg=button: on_click(arg, y, x)
        button.grid(row=y, column=x, pady=2, padx=2)



print("Giocatore 1 è il tuo turno")
punteggi = np.zeros(nGiocatori)


class TableModel():
    '''
Modello base per contenimento dati, intestazioni e dimensionamento per
un oggetto "Table".
'''

    def __init__(self, geometry=None, headers=None, data=None):
        '''
"Costruttore" del modello di tabella.

Parametri :
    geometry - dizionario contenente le chiavi :
                minsizes : lista di interi, dimensioni minime delle colonne
                weights : lista di interi definente il proporzionamento al
                           resize, 0 = colonna fissa
    headers  - lista intestazioni delle colonne
    data     . lista di liste : valori nelle colonne

Note : mi piacerebbe aggiungere un "maxsize" alle colonne ma non mi sembra supportato

'''
        self.geometry = geometry
        self.headers = headers
        self.data = data


class Table(tk.Frame):
    '''
Elementare "Tabella" dati, crea una singola riga di etichette di intestazione
ed n righe di entry per i dati.
'''

    def __init__(self, master=None, model=None):
        '''
"Costruttore" della tabella

parametri :
    master : widget/finestra proprietaria
    model  : modello della tabella
'''
        super().__init__(master)
        # verifica il modello di tabella, se incoerente si auto-distrugge
        if not model.geometry or not model.headers:
            self.destroy()
            return
        self.model = model
        self.__populate()

    def __populate(self):
        ''' Popola la tabella con i dati memorizzati nel modello. '''
        # etichette
        self.labels = []
        h_bg = tk.Frame(self)
        h_bg.grid(row=0, column=0, sticky='ew', padx=0, pady=0)
        for i in range(len(self.model.headers)):
            lbl = tk.Label(h_bg)
            lbl.configure(text=self.model.headers[i], relief='raised')
            lbl.grid(row=0, column=i, sticky='ew')
            self.labels.append(lbl)
        # definizione sfondo delle celle dati
        cells_bg = tk.Frame(self)
        cells_bg.grid(row=1, column=0, sticky='nsew', padx=0, pady=0)
        # definizione delle celle dati
        self.cells = []
        for i in range(len(self.model.data)):
            row_cells = []
            for j in range(len(self.model.headers)):
                c = tk.Entry(cells_bg, relief='ridge', bg='white')
                c.grid(row=i, column=j, sticky='ew')
                c.insert(tk.END, self.model.data[i][j])
                c.bind('<FocusIn>', self.__cell_focus)
                row_cells.append(c)
            self.cells.append(row_cells)
        # scroolbar ... poi

        # proporzionamento colonne
        for i in range(len(self.model.geometry['minsizes'])):
            if self.model.geometry['minsizes'][i]:
                h_bg.grid_columnconfigure(i, minsize=self.model.geometry['minsizes'][i])
                cells_bg.grid_columnconfigure(i, minsize=self.model.geometry['minsizes'][i])
            if self.model.geometry['weights'][i]:
                h_bg.grid_columnconfigure(i, weight=self.model.geometry['weights'][i])
                cells_bg.grid_columnconfigure(i, weight=self.model.geometry['weights'][i])
        # definizione del "peso" di riga/colonna
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        # definizione riga corrente
        self.__curr_row = 0

    def __cell_focus(self, evt):
        row = evt.widget.grid_info()['row']
        if row != self.__curr_row:
            # "decolora" la vecchia riga selezionata
            for c in self.cells[self.__curr_row]:
                c.configure(bg='white')
            self.__curr_row = row
            # "colora" la nuova riga selezionata
            for c in self.cells[self.__curr_row]:
                c.configure(bg='#ffffc0')


# un primo test "al volo"
if __name__ == '__main__':
    # preparo le impostazioni per il "modello"
    g = {'minsizes': [0, 0],
         'weights': [1, 1]
         }
    h = ['Players', 'Score']

    model = TableModel(g, h, data)
    app = tk.Tk()
    f = tk.Frame(app)
    f.grid(row=0, column=0, sticky='nsew')
    t = Table(f, model)
    t.grid(row=0, column=0, sticky='nsew')
    b = tk.Button(f, text='Chiudi', command=app.destroy)
    b.grid(row=1, column=0, sticky='ew')
    f.grid_columnconfigure(0, weight=1)
    f.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)


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
            button = tk.Button(root, text="", font=("Helvetica", 20), height=1, width=5)
            button['command'] = lambda x=x, y=y, arg=button: on_click(arg, y, x)
            button.grid(row=y, column=x, pady=2, padx=2)

    print("Giocatore 1 è il tuo turno")


# Create menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)

root.mainloop()
