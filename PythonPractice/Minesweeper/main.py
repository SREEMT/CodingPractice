'''
Author: SREEMT
Date: 7-23-2025
Version: 1.0

Minesweeper program using Tkinter for the GUI.
Proogram is meant for coding practice.
'''

# import sys
# import threading    # Switch to multiprocessing for smoother experience
import time
# import tkinter as tk
# import random
# import grid
import minesweeper_tkinter


# Main
def main():
    # playGrid = grid.Grid(size_x=9, size_y=9, bomb_count=10)
    
    # Thread to have timer run while grid ui is running.
    # timer_thread = threading.Thread(target=minesweeper_tkinter.time_track, args=(), daemon=True)
    # timer_thread.start()

    # Generates the grid UI
    #minesweeper_tkinter.GridUi(playGrid)

    minesweeper_tkinter.GridUi(size_x = 9, size_y = 9, bomb_count = 10)

main()