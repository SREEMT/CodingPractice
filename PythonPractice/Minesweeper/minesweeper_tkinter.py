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

# Creates the UI for the Game
def gridUi(generated_grid):
    root = tk.Tk()
    root.title("Grid Display Test")
    data_array = generated_grid.grid

    # Use a frame for the grid
    grid_frame = tk.Frame(root)
    grid_frame.pack()

    for row_index, row_data in enumerate(data_array):
        for col_index, cell_data in enumerate(row_data):
            label = tk.Label(grid_frame, text=cell_data, relief=tk.RAISED, borderwidth=1, width=2, height=1)
            label.grid(row=row_index, column=col_index)

    # Seperate frame for button
    def handle_button_press(event):
        root.destroy()
        exit()


    button = tk.Button(text="Grid Display Test")
    button.bind("<Button-1>", handle_button_press)
    button.pack(pady=10)

    root.mainloop()