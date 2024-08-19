import tkinter as tk
from tkinter import ttk

'''
This is an experimental implementation of a simple UI. Currently, it allows the user to type in a census code or geoname, and it will create an autofill box where a selection can be made. More features are yet to be added, as it has no functionality or integration yet.

'''
def on_keyrelease(event, entry, items, listbox):
    value = entry.get().lower()
    listbox.delete(0, tk.END)
    if value == "":
        matches = []
    else:
        matches = [item for item in items if value in str(item).lower()]
    for match in matches:
        listbox.insert(tk.END, match)

def on_select(event, entry, listbox, callback):
    if not listbox.curselection():
        return
    index = listbox.curselection()[0]
    selected_item = listbox.get(index)
    entry.delete(0, tk.END)
    entry.insert(0, selected_item)
    callback(selected_item)

def create_autocomplete_box(master, items, callback, row, col):
    frame = tk.Frame(master)
    frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

    master.grid_columnconfigure(col, weight=1)
    master.grid_rowconfigure(row, weight=1)

    entry_var = tk.StringVar()
    entry = tk.Entry(frame, textvariable=entry_var)
    entry.pack(fill=tk.X, pady=10)
    entry.bind("<KeyRelease>", lambda event: on_keyrelease(event, entry, items, listbox))

    listbox = tk.Listbox(frame)
    listbox.pack(fill=tk.BOTH, expand=True, pady=10)
    listbox.bind("<<ListboxSelect>>", lambda event: on_select(event, entry, listbox, callback))

def item_selected_1(selected_item):
    print(f"Selected in Box 1: {selected_item}")

def item_selected_2(selected_item):
    print(f"Selected in Box 2: {selected_item}")

def main(df):
    root = tk.Tk()
    root.title("Main Window with AutoComplete Boxes")
    root.geometry("600x400")

    # Configure grid layout
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    items1 = list(set(df.iloc[:, -2].tolist()))
    create_autocomplete_box(root, items1, item_selected_1, 0, 0)
    # Items for the second AutoCompleteBox
    items2 = list(set(df.iloc[:, 2].tolist()))
    create_autocomplete_box(root, items2, item_selected_2, 0, 1)

    root.mainloop()
