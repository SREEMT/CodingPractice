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
import grid


class GridUi:
    def __init__(self, generated_grid):
        self.generated_grid = generated_grid
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

        # Data for game grid
        data_array = self.generated_grid.grid

        # Use a frame for the grid
        grid_frame = tk.Frame(self.root)
        grid_frame.pack()

        # Event function to display cell information once clicked
        def show_cell_button(event):
            button = event.widget
            if button.stored_text == '*':
                button.config(text=button.stored_text, bg = 'crimson')
                # self.timer_running = False
            else:
                button.config(text=button.stored_text, bg = 'aquamarine2')

        def flag_cell(event):
            button = event.widget
            button.config(bg = 'chartreuse')

        # Generates all necessary cells to display in a gui.
        for row_index, row_data in enumerate(data_array):
            for col_index, cell_data in enumerate(row_data):

                cell = tk.Button(grid_frame, text="", relief=tk.RAISED, borderwidth=1, width=2, height=1, bg = 'azure1')
                cell.stored_text = cell_data

                # Bind actions to buttons
                cell.bind("<Button-1>", show_cell_button)
                cell.bind("<Button-3>", flag_cell)
                cell.grid(row=row_index, column=col_index)

        # Seperate frame for button
        def handle_button_press(event):
            self.timer_running = False
            self.root.destroy()
            exit()

        # Button Test for exit game button, kills program
        exit_button = tk.Button(text="Grid Display Test")
        exit_button.bind("<Button-1>", handle_button_press)
        exit_button.pack(pady=10)

        # Start timer
        self.update_timer()

        self.root.mainloop()