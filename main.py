import sqlite3
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

conn = sqlite3.connect('subscriptions.db')

#s
c = conn.cursor()


c.execute('''
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        expiration DATE NOT NULL,
        type TEXT NOT NULL
    )
''')

def insert_subscription():
    name = name_entry.get()
    expiration = expiration_entry.get()
    subscription_type = type_var.get()

    c.execute('''
        INSERT INTO subscriptions (name, expiration, type)
        VALUES (?, ?, ?)
    ''', (name, expiration, subscription_type))
    conn.commit()


    name_entry.delete(0, tk.END)
    expiration_entry.delete(0, tk.END)


def get_subscriptions():
    c.execute('SELECT * FROM subscriptions')
    subscriptions = c.fetchall()


    listbox.delete(0, tk.END)


    for subscription in subscriptions:
        listbox.insert(tk.END, subscription)


window = tk.Tk()

window.title('Subscription Database')


style = ttk.Style()

style.theme_use('clam')


name_label = ttk.Label(window, text='Name:')

name_label.grid(row=0, column=0)

name_entry = ttk.Entry(window)

name_entry.grid(row=0, column=1)


expiration_label = ttk.Label(window, text='Expiration:')

expiration_label.grid(row=1, column=0)

expiration_entry = DateEntry(window, width=12, background='white', foreground='black', borderwidth=2)

expiration_entry.grid(row=1, column=1)


type_var = tk.StringVar()

ttk.Radiobutton(window, text='Basic', variable=type_var, value='basic').grid(row=2, column=0)

ttk.Radiobutton(window, text='Premium', variable=type_var, value='premium').grid(row=2, column=1)


insert_button = ttk.Button(window, text='Insert', command=insert_subscription)

insert_button.grid(row=3, column=0)


listbox = tk.Listbox(window)

listbox.grid(row=4, column=0, rowspan=2, columnspan=2)


get_subscriptions_button = ttk.Button(window, text='Get Subscriptions', command=get_subscriptions)

get_subscriptions_button.grid(row=3, column=1)


window.mainloop()


conn.close()