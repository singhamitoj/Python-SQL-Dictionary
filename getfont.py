import tkinter as tk
import tkinter.font as tkfont

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Get the list of available fonts
available_fonts = list(tkfont.families())

# Print the list of fonts
for font in available_fonts:
    print(font)

# Destroy the root window after retrieving the fonts
root.destroy()
