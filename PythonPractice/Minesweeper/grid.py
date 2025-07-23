'''
Author: SREEMT
Date: 7-23-2025
Version: 1.0

Class that stores grid properties
Properties Stored:
    size x, size y, bomb count, grid, revealed, flags, game state, and cells remaining.
'''

import random

class Grid:
    # Offset coordinate values to determine the coordinates around a bomb
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

    # Stores grid attributes to determine size and bomb count
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