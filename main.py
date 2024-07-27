# Made by GamerSinghKing. The database was taken from https://github.com/benjihillard/English-Dictionary-Database.
# The font used is called Scratchy Lemon. https://www.dafont.com/scratchy-lemon.font

import sqlite3
import tkinter as tk
from tkinter import font as tkfont
import os

# Connect to the SQLite database
english = sqlite3.connect("englishlanguage.db")
crsr = english.cursor()

# Set up the main window
window = tk.Tk()
window.title("English Dictionary")
window.geometry("640x480")
window.configure(bg="lightblue")

custom_font_path = os.path.abspath("CustomFont.ttf")

if os.path.exists(custom_font_path):
    window.tk.call('font', 'create', 'CustomFont', '-family', 'Scratchy Lemon', '-size', 25)
    custom_font = tkfont.Font(family="Scratchy Lemon", size=25)
else:
    print("Custom font file not found.")
    custom_font = tkfont.Font(family="Helvetica", size=25)

# Create a label and a text widget
dictdesc = tk.Label(window, text="Enter a word and get the definition!", bg="lightblue", font=custom_font)
T = tk.Text(window, height=5, width=35)

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
TAns = tk.Text(window, height=10, width=40, bg="lightblue", wrap="word", font=custom_font, yscrollcommand=scrollbar.set)
scrollbar.config(command=TAns.yview)

# Function to search for the word and display the definition
def search(event=None):
    inputword = T.get(1.0, "end-1c").strip()  # Get the input word and strip any extra whitespace
    inputword_capitalized = inputword.capitalize()
    crsr.execute("SELECT field3 FROM english_dictionary WHERE field1=?", (inputword_capitalized,))
    result = crsr.fetchone()
    TAns.config(state=tk.NORMAL)
    TAns.delete(1.0, tk.END)

    if result:
        #TAns.config(text=result[0])
        TAns.insert(tk.END, result)
    else:
        TAns.config(text="Word not found")

def on_enter_key(event):
    search()
    return "break" # Prevent the textbox from creating new lines.

# Bind the Enter key to the custom event handler
T.bind("<Return>", on_enter_key)

# Create a button to trigger the search function
inputtxt = tk.Button(window, text="Enter the word:", bg="white", command=search, font=custom_font)

# Create a label to display the answer
#TAns = tk.Label(window, text="", bg="lightblue", font=custom_font)
TAns = tk.Text(window, height=10, width=40, bg="lightblue", wrap="word", font=custom_font, yscrollcommand=scrollbar.set)
TAns.config(state=tk.DISABLED)

# Pack the widgets to display them in the window
dictdesc.pack()
T.pack()
inputtxt.pack()
TAns.pack()

# Run the main loop
window.mainloop()