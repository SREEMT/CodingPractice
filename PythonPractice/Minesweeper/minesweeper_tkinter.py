'''
Author: SREEMT
Date: 5-16-2025
Version: 1.0

# Optimization Resources:
#   https://noobtomaster.com/python-gui-tkinter/optimizing-performance-and-responsiveness/
#   https://medium.com/tomtalkspython/tkinter-best-practices-optimizing-performance-and-code-structure-c49d1919fbb4

GUI module for Minesweeper
Includes timer function as well
'''

# Tkinter Test
'''
window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()


button = tk.Button(text="My simple app.")
button.bind("<Button-1>", handle_button_press)
button.pack()

# Start the event loop.
window.mainloop()
'''

'''
Class that stores grid properties
Properties Stored:
    size x, size y, bomb count, grid, revealed, flags, game state, and cells remaining.
'''

import sys
import threading
import time
import tkinter as tk
from functools import partial
import grid


class GridUi:
    def __init__(self, size_x, size_y, bomb_count):
        self.size_x = size_x
        self.size_y = size_y
        self.bomb_count = bomb_count
        self.generated_grid = None

        self.first_click = True
        self.buttons =[]

        self.sec = 0
        self.timer_running = True
        self.root = tk.Tk()
        self.gridUi()

    # Formats time for time_track
    def time_format(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60

        return "{0}:{1}:{2}".format(int(hours),int(mins),int(sec))

    # Updates timer on the GUI
    def update_timer(self):
        if self.timer_running:
            self.timer_label.config(text = f"Time: {self.time_format(self.sec)}")
            self.sec += 1
            self.root.after(1000, self.update_timer)


    # Creates the UI for the Game
    def gridUi(self):
        # root = tk.Tk()
        self.root.title("Grid Display Test")

        info_frame = tk.Frame(self.root)
        info_frame.pack(pady = 5)

        # Timer display label
        self.timer_label = tk.Label(info_frame, text = "Time: 00:00:00", font = ("Helvetica", 14))
        self.timer_label.pack()

        # Use a frame for the grid
        grid_frame = tk.Frame(self.root)
        grid_frame.pack()

        # Generates the grid UI
        for row in range(self.size_y):
            button_row = []
            for col in range(self.size_x):
                btn = tk.Button(grid_frame, text="", relief=tk.RAISED, width=2, height=1, bg='azure1')
                btn.grid(row=row, column=col)
                btn.bind("<Button-1>", partial(self.on_cell_click, row, col))
                button_row.append(btn)
            self.buttons.append(button_row)

        # Button Test for exit game button, kills program
        exit_button = tk.Button(text="Grid Display Test")
        exit_button.bind("<Button-1>", lambda e: self.quit_game())
        exit_button.pack(pady=10)

        # Start timer
        self.update_timer()

        self.root.mainloop()
    
    # Handles game events when cells are clicked
    def on_cell_click(self, row, col, event):
        if self.first_click:
            self.generated_grid = grid.Grid(self.size_x, self.size_y, self.bomb_count)
            self.generated_grid.generate_grid(exclude_x = col, exclude_y = row)
            self.first_click = False
        
        value = self.generated_grid.grid[row][col]
        button = self.buttons[row][col]

        if value =="*":
            button.config(text = "*", bg = 'crimson')
            self.timer_running = False
            self.reveal_all()
        else:
            button.config(text=str(value), bg = "aquamarine2")
            button.config(state = 'disabled')

    # Reveals all cell data based on game state
    def reveal_all(self):
        for row in range(self.size_y):
            for col in range(self.size_x):
                value = self.generated_grid.grid[row][col]
                button = self.buttons[row][col]
                button.config(text = str(value))
                if value == "*":
                    button.config(bg = 'crimson')
                else:
                    button.config(bg = 'lightgrey')
                button.config(state = 'disabled')

    # Quit game function
    def quit_game(self):
        self.timer_running = False
        self.root.destroy()