"""
Course: CSE 311
Date: 14 March 2020
ConnectFour
Purpose: This class serves to test the logic of the
         Connect Four MVC program. Because most of
         the program relies on user input and random
         number generation that ultimately gets
         assigned to variables that are inaccessible
         outside of their immediate functions and
         those that are passed said values, there
         is not much Unit Testing that can be done
         in that domain; however, extensive testing
         was done during development to ensure that
         all possible user inputs are accounted for.
"""
import unittest
import Controller


class TestGameLogic(unittest.TestCase):
    def new_grid(self):
        """
        This function returns a blank game grid.
        :return: A blank game grid
        """
        return [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]

    def test_empty_board_case(self):
        """
        This function tests to see that no win is found on a
        grid that does not have four of teh same pieces in a row.
        """
        self.assertEqual(Controller.Controller().model.check_for_win(), 0)

    def test_horizontal_cases(self):
        """
        This function tests if all possible horizontal win cases
        are accounted for and return the correct value.
        """
        m = Controller.Controller().model
        for p in ['O', 'X']:
            for i in range(0, 4):
                for j in range(5, -1, -1):
                    m.grid[i][j] = p
                    m.grid[i + 1][j] = p
                    m.grid[i + 2][j] = p
                    m.grid[i + 3][j] = p
                    # Uncomment the following line to see every possible horizontal win
                    # self.c.text_view.print_grid(m.grid)
                    self.assertEqual(m.check_for_win(), p)
                    m.grid = self.new_grid()

    def test_vertical_win(self):
        """
        This function tests if all possible vertical win cases
        are accounted for and return the correct value.
        """
        m = Controller.Controller().model
        for p in ['O', 'X']:
            for i in range(0, 7):
                for j in range(5, 2, -1):
                    m.grid[i][j] = p
                    m.grid[i][j - 1] = p
                    m.grid[i][j - 2] = p
                    m.grid[i][j - 3] = p
                    # Uncomment the following line to see every possible vertical win
                    # self.c.text_view.print_grid(m.grid)
                    self.assertEqual(m.check_for_win(), p)
                    m.grid = self.new_grid()

    def test_up_left_case(self):
        """
        This function tests if all possible up-left win cases
        are accounted for and return the correct value.
        """
        m = Controller.Controller().model
        for p in ['O', 'X']:
            for i in range(6, 2, -1):
                for j in range(5, 2, -1):
                    m.grid[i][j] = p
                    m.grid[i - 1][j - 1] = p
                    m.grid[i - 2][j - 2] = p
                    m.grid[i - 3][j - 3] = p
                    # Uncomment the following line to see every possible diagonal up-left win
                    # self.c.text_view.print_grid(m.grid)
                    self.assertEqual(m.check_for_win(), p)
                    m.grid = self.new_grid()

    def test_up_right_case(self):
        """
        This function tests if all possible up-right win cases
        are accounted for and return the correct value.
        """
        m = Controller.Controller().model
        for p in ['O', 'X']:
            for i in range(0, 4):
                for j in range(5, 2, -1):
                    m.grid[i][j] = p
                    m.grid[i + 1][j - 1] = p
                    m.grid[i + 2][j - 2] = p
                    m.grid[i + 3][j - 3] = p
                    # Uncomment the following line to see every possible diagonal up-right win
                    # self.c.text_view.print_grid(m.grid)
                    self.assertEqual(m.check_for_win(), p)
                    m.grid = self.new_grid()
