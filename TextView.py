"""
Course: CSE 311
Date: 14 March 2020
ConnectFour
Purpose: This class serves as a View (Text) in an MVC ConnectFour
         program. Its functions can be called upon to display the
         current state of the game, alert the player of each COM
         move, prompt user input, and display the winner of a game,
         all in a textual view/terminal window.
"""
import sys


class TextView:
    def display_results(self, winner):
        """
        This function prints the winner of a game when one is found.
        :param winner: The player (USER or COM) who has four in a row
        """
        print(winner + ' WINS!\n')
        input('Press ENTER to exit...')
        sys.exit()

    def prompt_user(self):
        """
        This function prompts the user to enter a column to drop their next piece into.
        The user may enter 'exit' or 's' to terminate the program or prompt a switch to
        a different view, respectively. An input out of range [1,7] will cause a reprompt.
        :return: Valid user input
        """
        print('\nChoose column (\'exit\' to quit or \'s\' to switch views):', end=' ')
        # Loop until user provides valid input
        while 1:
            col = input()
            if col == 'exit':
                sys.exit()
            elif col == 's':
                print('\nSWITCHING VIEW...\n')
                return col
            else:
                try:
                    if 0 < int(col) < 8:
                        return col
                    else:
                        print('Enter a number (1-7):', end=' ')
                except ValueError:
                    print('Enter a number (1-7):', end=' ')

    def print_grid(self, grid):
        """
        This function prints a formatted version of the provided grid.
        :param grid: The provided grid
        :return: 0 when the grid is printed
        """
        print(' 1   2   3   4   5   6   7 ')
        for row in range(6):
            for col in range(7):
                if grid[col][row]:
                    print('[' + grid[col][row] + ']', end=' ')
                else:
                    print('[ ]', end=' ')
            print()
        return 0

    def illegal_move(self):
        """
        This function alerts the user when they have attempted an illegal move.
        :return: 0 when the grid is printed
        """
        print('Illegal Move', end='\n')
        return 0

    def print_com_move(self, column_number):
        """
        This function alerts the user of the COM's move.
        :param column_number: The column number that the COM dropped their game piece in
        :return: 0 when the grid is printed
        """
        print('COM move: ' + str(column_number), end='\n')
        return 0
