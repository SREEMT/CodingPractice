'''
Author: SREEMT
Date: 5-16-2025
Version: 1.0

Minesweeper program using Tkinter for the GUI.
Proogram is meant for coding practice.
'''

import time
import tkinter as tk

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

def time_format(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))

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

def main():
    time_track()

main()