from tkinter import *

root = Tk()
root.title("Filetto")
root.geometry("700x700")

my_entries = []

z = input("Inserisci il valore: ")
w = int(z)


def b_click(b):
    pass


def buttons():
    entry_list = ''

    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'

    print(my_entries[24].get())


# Row Loop
for y in range(w):
    # Column Loop
    for x in range(w):
        my_entry = Button(root, text="ciao", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                          command=lambda: b_click(my_entry))
        my_entry.grid(row=y, column=x)
        my_entries.append(my_entry)

root.mainloop()
