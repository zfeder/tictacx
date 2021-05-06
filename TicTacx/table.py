import tkinter as tk
from tkinter import ttk

def show():

    tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
    tempList.sort(key=lambda e: e[1], reverse=True)

    for i, (name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, name, score))

scores = tk.Tk()
label = tk.Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('Player', 'Score')
listBox = ttk.Treeview(scores, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

scores.mainloop()