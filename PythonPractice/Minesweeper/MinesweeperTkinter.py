'''
Author: SREEMT
Date: 5-16-2025
Version: 1.0

Minesweeper program using Tkinter for the GUI.
Proogram is meant for coding practice.
'''

import time
import tkinter as tk
import random

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
class Grid:
    clockwise_offsets = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1)
    ]

    def __init__(self, size_x, size_y, bomb_count):
        self.size_x = size_x
        self.size_y = size_y
        self.bomb_count = bomb_count

        self.grid = []
        self.revealed = []
        self.flags = []
        self.game_end = False
        self.cells_remaining = 0

        self.generate_grid()

        # Generates a grid based on given parameters and stores all data an the Grid class
    def generate_grid(self):
        self.grid = [[0 for _ in range(self.size_x)] for _ in range(self.size_y)]
        positions = [(x, y) for y in range(self.size_y) for x in range(self.size_x)]    # Generates an array of all possible positions in a given grid size
        bomb_positions = random.sample(positions, self.bomb_count)      # Generates bomb positions based on the positions values
    
        # Test
        print(bomb_positions)

        # Appends '*' to any postition where a bomb is placed
        for (x, y) in bomb_positions:
            self.grid[y][x] = '*'
        
        # Test clockwise offset values
        #for (x, y) in self.clockwise_offsets:
        #    print(x, y)

        # Adding numbers to the surrounding positions from the bomb
        for (x, y) in bomb_positions:
            for (a, b) in self.clockwise_offsets:
                nx = x + a
                ny = y + b
                if nx > -1 and nx < self.size_x and ny > -1 and ny < self.size_y and self.grid[ny][nx] != '*':
                    self.grid[ny][nx] += 1

        # Test
        for row in self.grid:
            print(" ".join(str(cell)for cell in row))


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

def main():
    grid = Grid(size_x=9, size_y=9, bomb_count=10)
    time_track()

main()