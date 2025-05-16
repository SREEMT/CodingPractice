'''
Author: SREEMT
Date: 5-16-2025
Version: 1.0

Minesweeper program using Tkinter for the GUI.
Proogram is meant for coding practice.
'''

import tkinter as tk

window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()


button = tk.Button(text="My simple app.")
button.bind("<Button-1>", handle_button_press)
button.pack()

# Start the event loop.
window.mainloop()