"""
Course: CSE 311
Date: 14 March 2020
ConnectFour
Purpose: This class serves as the Model in an MVC ConnectFour
         program. It can be used to store all moves in a grid,
         or list of lists that act as stacks, and can be used
         to determine if there is a winner.
"""


class Model:
    def __init__(self):
        # self.grid is the list of lists that acts as stacks to store each move
        self.grid = [[None for i in range(6)] for j in range(7)]

    def check_for_win(self):
        """
        This function checks to see if there are four matching game pieces in a
        row by checking all horizontal possibilities, all vertical possibilities,
        all left diagonal possibilities, and all right diagonal possibilities.
        :return: A string of the winning player ('O' for COM and 'X' for USER)
                 or 0 if there is no winner
        """
        horizontal = self.check_horizontal()
        vertical = self.check_vertical()
        up_left = self.check_up_left()
        up_right = self.check_up_right()
        if horizontal or vertical or up_left or up_right:
            return str(horizontal) + str(vertical) + str(up_left) + str(up_right)
        return 0

    def check_horizontal(self):
        """
        This function checks every possible combination of horizontal grid spots
        that could have four game pieces of the same player in a row.
        :return: A string of the winning player ('O' for COM and 'X' for USER)
                 if four in a row are found or '' if there is no winner
        """
        g = self.grid
        for col in range(0, 4):
            for row in range(5, -1, -1):
                if g[col][row] and g[col][row] == g[col + 1][row] == g[col + 2][row] == g[col + 3][row]:
                    return g[col][row]
        return ''

    def check_vertical(self):
        """
        This function checks every possible combination of vertical grid spots
        that could have four game pieces of the same player in a row.
        :return: A string of the winning player ('O' for COM and 'X' for USER)
                 if four in a row are found or'' if there is no winner
        """
        g = self.grid
        for col in range(0, 7):
            for row in range(5, 2, -1):
                if g[col][row] and g[col][row] == g[col][row - 1] == g[col][row - 2] == g[col][row - 3]:
                    return g[col][row]
        return ''

    def check_up_left(self):
        """
        This function checks every possible combination of up-left grid spots
        that could have four game pieces of the same player in a row.
        :return: A string of the winning player ('O' for COM and 'X' for USER)
                 if four in a row are found or'' if there is no winner
        """
        g = self.grid
        for col in range(3, 7):
            for row in range(5, 2, -1):
                if g[col][row] and g[col][row] == g[col - 1][row - 1] == g[col - 2][row - 2] == g[col - 3][row - 3]:
                    return g[col][row]
        return ''

    def check_up_right(self):
        """
        This function checks every possible combination of up-right grid spots
        that could have four game pieces of the same player in a row.
        :return: A string of the winning player ('O' for COM and 'X' for USER)
                 if four in a row are found or'' if there is no winner
        """
        g = self.grid
        for col in range(0, 4):
            for row in range(5, 2, -1):
                if g[col][row] and g[col][row] == g[col + 1][row - 1] == g[col + 2][row - 2] == g[col + 3][row - 3]:
                    return g[col][row]
        return ''
