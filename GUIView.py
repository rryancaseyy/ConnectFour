"""
Course: CSE 311
Date: 14 March 2020
ConnectFour
Purpose: This class serves as a View (GUI) in an MVC ConnectFour
         program. Its functions can be called upon to display the
         current state of the game, prompt user input, and display
         the winner of a game, all in a GUI window.
"""
import tkinter as tk
import sys


class GUIView:
    def __init__(self):
        self.window = None
        # This variable stores the most recent user input
        self.user_input = None
        # This variable is what alerts the view that there is a winner when the window is refreshed
        self.winner = None

    def display_results(self, winner):
        """
        This function declares the winner of a game when one is found.
        :param winner: The player (USER or COM) who has four in a row
        """
        self.winner = winner

    def prompt_user(self):
        """
        This function returns the value from the most recent user input.
        :return: The value from the most recent user input.
        """
        return self.user_input

    def get_return(self, val):
        """
        This function updates the variable that stores the most recent
        user input and terminates the program if prompted to do so.
        :param val:
        :return: The most recent user input
        """
        self.user_input = val
        if val == 'exit':
            sys.exit()
        return self.user_input

    def display_window(self, grid):
        """
        This function constructs a window and displays its necessary
        components based on the state of the game.
        :param grid: The game grid from the Model
        :return: 0 at the end of the function
        """
        self.window = tk.Tk()
        self.set_window_settings()

        if not self.winner:
            self.add_buttons()
        else:
            win_display = tk.Label(self.window, text=(self.winner + ' WINS!'), font=("Helvetica", 50), bg='white')
            win_display.grid(row=1, columnspan=8, sticky='nesw')

        self.print_grid(grid)

        self.window.mainloop()
        return 0

    def set_window_settings(self):
        """
        This function sets the settings of the window.
        :return: 0 at the end of the function
        """
        self.center_window()
        self.window.attributes("-topmost", True)
        self.window.resizable(False, False)
        self.window.protocol('WM_DELETE_WINDOW', self.get_return(exit))
        self.window.title('Connect Four')
        return 0

    def center_window(self):
        """
        This function centers the window on the screen.
        :return: 0 at the end of the function
        """
        window_width = self.window.winfo_reqwidth()
        window_height = self.window.winfo_reqheight()

        position_right = int(self.window.winfo_screenwidth() / 2.5 - window_width / 2)
        position_down = int(self.window.winfo_screenheight() / 2.5 - window_height / 2)

        self.window.geometry("+{}+{}".format(position_right, position_down))
        return 0

    def add_buttons(self):
        """
        This function adds a button to the window that allows the user to switch views.
        The other buttons that are added are the buttons that allow the user to choose
        which column to drop a game piece into when it is the user's turn.
        :return: 0 at the end of the function
        """
        b = tk.Button(self.window, height=2, text='Switch to Text View', bg='white', )
        b.config(command=lambda: self.get_return('s') and self.window.destroy())
        b.grid(row=9, columnspan=7, sticky='nesw')

        for i in range(1, 8):
            b = tk.Button(self.window, height=2, width=8, text=1, bg='white')
            if i == 1:
                b.config(text='1', command=lambda: self.get_return(1) and self.window.destroy())
                b.grid(row=1, column=0, sticky='nesw')
            elif i == 2:
                b.config(text='2', command=lambda: self.get_return(2) and self.window.destroy())
                b.grid(row=1, column=1, sticky='nesw')
            elif i == 3:
                b.config(text='3', command=lambda: self.get_return(3) and self.window.destroy())
                b.grid(row=1, column=2, sticky='nesw')
            elif i == 4:
                b.config(text='4', command=lambda: self.get_return(4) and self.window.destroy())
                b.grid(row=1, column=3, sticky='nesw')
            elif i == 5:
                b.config(text='5', command=lambda: self.get_return(5) and self.window.destroy())
                b.grid(row=1, column=4, sticky='nesw')
            elif i == 6:
                b.config(text='6', command=lambda: self.get_return(6) and self.window.destroy())
                b.grid(row=1, column=5, sticky='nesw')
            elif i == 7:
                b.config(text='7', command=lambda: self.get_return(7) and self.window.destroy())
                b.grid(row=1, column=6, sticky='nesw')

        return 0

    def print_grid(self, grid):
        """
        This function adds seven columns of six disabled buttons that
        represent the game grid and game pieces, based on their color.
        :param grid: The game grid from the Model
        :return: 0 at the end of the function
        """
        for row in range(2, 8):
            for col in range(0, 7):
                b = tk.Button(self.window, height=2, width=8, bg='orange', state='disabled')

                if grid[col][row-2] == 'O':
                    b.config(bg='black')
                elif grid[col][row-2] == 'X':
                    b.config(bg='red')

                b.grid(row=row, column=col, sticky='nesw')
        return 0
