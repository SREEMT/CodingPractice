'''
Author: SREEMT
Date: 5-16-2025
Version: 1.0

# Optimization Resources:
#   https://noobtomaster.com/python-gui-tkinter/optimizing-performance-and-responsiveness/
#   https://medium.com/tomtalkspython/tkinter-best-practices-optimizing-performance-and-code-structure-c49d1919fbb4

Theme Used:
#   https://github.com/rdbende/Azure-ttk-theme

GUI module for Minesweeper
Includes timer function as well
'''

import os
import sys
import threading
import time
import tkinter as tk
from functools import partial
import grid


class GridUi:
    def __init__(self, size_x, size_y, bomb_count):
        # Game rules
        self.size_x = size_x
        self.size_y = size_y
        self.bomb_count = bomb_count
        self.generated_grid = None
        self.flags_left = self.bomb_count

        # Cell attributes
        self.first_click = True
        self.buttons =[]
        self.flags = [[False for _ in range(self.size_x)] for _ in range(self.size_y)]

        # Timer attributes
        self.sec = 0
        self.timer_running = True
        self.root = tk.Tk()

        # Using a theme
        script_dir = os.path.dirname(os.path.abspath(__file__))
        theme_path = os.path.join(script_dir, "azure.tcl") 
        self.root.tk.call("source", theme_path) 
        self.root.tk.call("set_theme", "dark")
        
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

        # Timer bar to manage the timer display
        timer_frame = tk.Frame(self.root)
        timer_frame.grid(row = 0, column = 0, columnspan = 2, sticky = "ew")

        # Timer label
        self.timer_label = tk.Label(timer_frame, text = "Time: 00:00:00", font = ("Helvetica", 14))
        self.timer_label.pack(pady = 5)

        info_frame = tk.Frame(self.root)
        # info_frame.pack(padx = 10, pady = 10)
        info_frame.grid(row = 1, column = 0, sticky = "w")

        # Grid placed on left
        grid_frame = tk.Frame(info_frame)
        grid_frame.grid(row = 0, column = 0)

        # Buttons on right
        side_panel = tk.Frame(info_frame)
        side_panel.grid(row = 0, column = 1, padx = 10, sticky = "n")

        # Flag counter
        self.flag_label = tk.Label(side_panel, text = f"🚩 Flags: {self.flags_left}", font = ("Helvetica", 12))
        self.flag_label.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = "w")


        # Use a frame for the grid (OLD FRAME)
        # grid_frame = tk.Frame(self.root)
        # grid_frame.pack()


        # Generates the grid UI
        for row in range(self.size_y):
            button_row = []
            for col in range(self.size_x):
                btn = tk.Button(grid_frame, text="", relief=tk.RAISED, width=2, height=1, bg='gray55', fg='black')
                btn.grid(row=row, column=col)
                btn.bind("<Button-1>", partial(self.on_cell_click, row, col))
                btn.bind("<Button-3>", partial(self.on_right_click, row, col))
                button_row.append(btn)
            self.buttons.append(button_row)

        # Button Test for exit game button, kills program
        exit_button = tk.Button(side_panel, text= "Quit Game")
        exit_button.bind("<Button-1>", lambda e: self.quit_game())
        # exit_button.pack(pady=10)
        exit_button.grid(row = 0, column = 1, padx = 5, sticky = "w")

        # Start timer
        self.update_timer()

        self.root.mainloop()
    
    # Handles game events when cells are clicked
    def on_cell_click(self, row, col, event):
        if self.flags[row][col]:
            return

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
        elif button["state"] == "disabled":
            return
        else:
            button.config(text=str(value), bg = "darkolivegreen", fg = 'black', disabledforeground = 'black')
            button.config(state = 'disabled')
            self.game_check()
    
    # Places flag on cell if right clicked
    def on_right_click(self, row, col, event):
        button = self.buttons[row][col]
        
        if button["state"] == "disabled":
            return
        
        if not self.flags[row][col]:
            if self.flags_left > 0:
                button.config(text="🚩", bg = "khaki", activebackground = "khaki", fg="red")
                self.flags[row][col] = True
                self.flags_left -= 1
                self.flag_label.config(text = f"🚩 Flags: {self.flags_left}")
        else:
            button.config(text="", bg="gray55", activebackground="gray55", fg="black")
            self.flags[row][col] = False
            self.flags_left += 1
            self.flag_label.config(text=f"🚩 Flags: {self.flags_left}")

    def game_check(self):
        for row in range(self.size_y):
            for col in range(self.size_x):
                value = self.generated_grid.grid[row][col]
                button = self.buttons[row][col]

                if value != "*" and button["state"] != "disabled":
                    return
        
        self.timer_running = False
        self.win_reveal()
        # Add win message

    # Reveals all cell data based on game state
    def reveal_all(self):
        for row in range(self.size_y):
            for col in range(self.size_x):
                value = self.generated_grid.grid[row][col]
                button = self.buttons[row][col]
                button.config(text = str(value))
                if value == "*":
                    button.config(bg = 'crimson', fg = 'white', disabledforeground = 'white')
                else:
                    button.config(bg = 'gray55', fg = 'black', disabledforeground = 'black')
                button.config(state = 'disabled')

    def win_reveal(self):
        for row in range(self.size_y):
            for col in range(self.size_x):
                value = self.generated_grid.grid[row][col]
                button = self.buttons[row][col]
                button.config(text = str(value))
                if value == "*":
                    button.config(bg = 'crimson', fg = 'white', disabledforeground = 'white')
                else:
                    button.config(bg = 'darkolivegreen', fg = 'black', disabledforeground = 'black')
                button.config(state = 'disabled')

        # Test win screen
        win_popup = tk.Toplevel(self.root)
        win_popup.title("You Win!")

        msg = tk.Label(win_popup, text="🎉 You won the game!", font=("Helvetica", 14))
        msg.pack(padx=20, pady=20)

        ok_btn = tk.Button(win_popup, text="OK", command=win_popup.destroy)
        ok_btn.pack(pady=10)

    # Quit game function
    def quit_game(self):
        self.timer_running = False
        self.root.destroy()