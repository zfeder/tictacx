from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Filetto")
root.geometry("700x700")

clicked = True
count = 0

my_entries = []

z = input("Inserisci il valore: ")
w = int(z)


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")


def buttons():
    global clicked, count
    clicked = True
    count = 0

    entry_list = ''

    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'

    print(my_entries[24].get())


# Row Loop

for y in range(w):
    # Column Loop
    for x in range(w):
        my_entry = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                          command=lambda: b_click(my_entry))
        my_entry.grid(row=y, column=x)
        my_entries.append(my_entry)

root.mainloop()
