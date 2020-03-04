"""
Course: CSE 311
Date: 14 March 2020
ConnectFour
Purpose: This class serves as the Controller in an MVC ConnectFour
         program. It handles the flow of a game and acts as a sort
         of mediator between the Model and the View components.
"""
import Model
import TextView
import GUIView
import random


class Controller:
    def __init__(self):
        # Initialize Model and Views
        self.model = Model.Model()
        self.text_view = TextView.TextView()
        self.gui_view = GUIView.GUIView()

    def launch_game(self):
        """
        This function starts the game by allowing the user to choose an initial view.
        Note: This function is set to always give the user the first move.
        :return: 0 at the end of the function
        """
        print('Choose the view you wish to play in.')
        current_view = None

        # While loop catches unexpected input
        while current_view != 't' and current_view != 'g':
            print('Enter \'t\' for Text View or \'g\' for GUI:', end=' ')
            current_view = input()

        self.determine_view([current_view, 'COM'])
        return 0

    def determine_view(self, args):
        """
        This is the driving function of the class that runs until a user is determined.
        Each loop funnels execution into the current view that has been chosen by the user.
        :param args: A list of string arguments:
                     arg[0] = current view and arg[1] = person who moved last ('COM' or 'USER')
        """
        need_initial_grid = True

        while 1:
            if args[0] is 't':
                # Show user current state of the grid on first call of text view
                if need_initial_grid:
                    self.text_view.print_grid(self.model.grid)
                need_initial_grid = False
            elif args[0] is 'g':
                # Reinitialize window to refresh grid
                self.gui_view.display_window(self.model.grid)

            args = self.view_controller(args[0], args[1])

    def view_controller(self, current_view, last_turn):
        """
        This function allows the Controller to pull input from the current_view.
        :param current_view: A string representing the current view ('t' or 'g')
        :param last_turn: A string representing the player who moved last ('COM' or 'USER')
        :return: A list of string arguments:
                 arg[0] = current view and arg[1] = person who moved last ('COM' or 'USER')
        """
        view = self.text_view if current_view == 't' else self.gui_view

        user_input = view.prompt_user()
        if user_input == 's':
            self.determine_view(['t', last_turn]) if current_view == 'g' else self.determine_view(['g', last_turn])
        response = self.get_move(user_input, last_turn)

        if current_view == 't':
            view.print_grid(self.model.grid)

        if response == 'COM' or response == 'USER':
            view.display_results(response)
        elif current_view == 't':
            view.illegal_move() if response is 'INVALID' else view.print_com_move(response)

        return [current_view, last_turn]

    def get_move(self, user_input, last_turn):
        """
        This function determines whose turn it is and either adds the user-chosen
        column to the grid or allows the COM to add a game piece to the board.
        :param user_input: The input pulled from the current_view
        :param last_turn: The person who added a game piece to the grid last
        :return: The number of the column the COM add a game piece to or the user_input
        """
        if last_turn == 'COM':
            user_input = self.get_user_move(user_input)

        return self.get_com_move() if user_input is 'VALID' else user_input

    def get_user_move(self, user_input):
        """
        This function adds a game piece to a column specified by the user
        and checks for a winner, or flags the user input as invalid.
        :param user_input: The input pulled from the current_view
        :return: The value returned from the check_for_win function
                 or 'INVALID' if the chosen grid column is full
        """
        if self.column_is_open(user_input):
            self.add_to_col('USER', user_input)
            return self.check_for_win('USER')
        else:
            return 'INVALID'

    def get_com_move(self):
        """
        This function allows the COM player to add a game piece to a
        randomly selected column in the grid.
        :return: The value returned from the check_for_win function
        """
        column_number = random.uniform(1, 8)
        # Choose another column if the one at col_num is full
        while not self.column_is_open(column_number):
            column_number = random.uniform(1, 8)
        com_move = self.add_to_col('COM', column_number)

        return self.check_for_win(com_move)

    def check_for_win(self, last_turn):
        """
        This function checks the model for a winner.
        :param last_turn: A string representing the player who moved last ('COM' or 'USER')
        :return: The winner; if there isn't one, return 'VALID' if the user moved last or
                 the value passed in last_turn
        """
        winner = self.model.check_for_win()
        if winner:
            return 'COM' if winner == 'O' else 'USER'
        else:
            return 'VALID' if last_turn == 'USER' else last_turn

    def column_is_open(self, column_number):
        """
        This function checks to see if the specified column in the grid is full.
        :param column_number: The number of the column in question
        :return: True if the column has at least one open space; else return false
        """
        num_used_spots = len(list(filter(lambda x: x is not None, self.model.grid[int(column_number) - 1])))
        return num_used_spots < 6

    def add_to_col(self, player, column_number):
        """
        This function adds a game piece to the grid at column_number for the specified player.
        :param player: The player who provided the column_number
        :param column_number: The number of the column that a game piece will be added to
        :return: The column number
        """
        column_number = int(column_number) - 1
        next_empty_spot = 5 - len(list(filter(lambda x: x is not None, self.model.grid[column_number])))
        self.model.grid[column_number][next_empty_spot] = 'X' if player == 'USER' else 'O'
        return column_number + 1
