# -*- coding: utf-8 -*-

import tkinter as tk


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
    data = [['A', '13'],
            ['B', '2'],
            ['C', '47'],
            ['D', '24']
            ]
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
    app.mainloop()