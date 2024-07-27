import sqlite3
import tkinter as tk

# Connect to the SQLite database
english = sqlite3.connect("englishlanguage.db")
crsr = english.cursor()

# Set up the main window
window = tk.Tk()
window.title("English Dictionary")
window.geometry("640x480")
window.configure(bg="lightblue")

# Create a label and a text widget
dictdesc = tk.Label(window, text="Enter a word and get the definition!", bg="lightblue")
T = tk.Text(window, height=1, width=20)

# Function to search for the word and display the definition
def search():
    inputword = T.get(1.0, "end-1c").strip()  # Get the input word and strip any extra whitespace
    crsr.execute("SELECT field3 FROM english_dictionary WHERE field1=?", (inputword,))
    result = crsr.fetchone()
    if result:
        TAns.config(text=result[0])
    else:
        TAns.config(text="Word not found")

# Create a button to trigger the search function
inputtxt = tk.Button(window, text="Enter the word:", bg="white", command=search)

# Create a label to display the answer
TAns = tk.Label(window, text="", bg="lightblue")

# Pack the widgets to display them in the window
dictdesc.pack()
T.pack()
inputtxt.pack()
TAns.pack()

# Run the main loop
window.mainloop()
