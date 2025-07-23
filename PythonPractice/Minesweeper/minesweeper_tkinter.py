'''
Author: SREEMT
Date: 5-16-2025
Version: 1.0

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


# Formats time for time_track
def time_format(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))

# Tracks time and displays it based on the gem_end condition
def time_track():

    # Test condition, value will change to true if game ends stopping the timer
    game_end = False

    start_time = time.time()
    prev_sec = -1

    while not game_end:
        end_time = time.time()
        time_lapsed = end_time - start_time
        curr_sec = int(time_lapsed)

        if curr_sec != prev_sec:
            prev_sec = curr_sec
            time_format(curr_sec)

class GridUi:
    def __init__(self, generated_grid):
        self.generated_grid = generated_grid
        self.gridUi()

    # Creates the UI for the Game
    def gridUi(self):
        root = tk.Tk()
        root.title("Grid Display Test")
        data_array = self.generated_grid.grid

        # Use a frame for the grid
        grid_frame = tk.Frame(root)
        grid_frame.pack()

        # Event function to display cell information once clicked
        def show_cell_button(event):
            button = event.widget
            if button.stored_text == '*':
                button.config(text=button.stored_text, bg = 'crimson')
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
            root.destroy()
            exit()

        # Button Test for exit game button, kills program
        button = tk.Button(text="Grid Display Test")
        button.bind("<Button-1>", handle_button_press)
        button.pack(pady=10)

        root.mainloop()