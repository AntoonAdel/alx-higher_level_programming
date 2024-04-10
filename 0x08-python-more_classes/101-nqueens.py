#!/usr/bin/python3
"""
N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP)
"""
import sys


class NQueen:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        """ Global Variables """
        self.n = n
        self.x = [0 for test2 in range(n + 1)]
        self.result = []

    def place(self, k, test2):
        """
        Checks if k Queen can be placed in test2 column (True)
        or if the are attacking queens in row or diagonal (False)
        """

        # test1 checks from 1 to k - 1 (Up to previous Queen)
        for test1 in range(1, k):
            # There is already a Queen in column
            # or a Queen in same diagonal
            if self.x[test1] == test2 or \
               abs(self.x[test1] - test2) == abs(test1 - k):
                return 0
        return 1

    def nQueen(self, k):
        """
        Tries to place every Queen in the board
        Args:
            k: starting Queen from which to evaluate (should be 1)
        """
        # test2 goes from column 1 to column n (1st column is 1st index)
        for test2 in range(1, self.n + 1):
            if self.place(k, test2):
                # Queen can be placed in test2 column
                self.x[k] = test2
                if k == self.n:
                    # Placed all 4 Queens (A the_solution was found)
                    the_solution = []
                    for test2 in range(1, self.n + 1):
                        the_solution.append([test2 - 1, self.x[test2] - 1])
                    self.result.append(the_solution)
                else:
                    # Need to place more Queens
                    self.nQueen(k + 1)
        return self.result


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except Exception:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

Queen = NQueen(N)
result = Queen.nQueen(1)

for test2 in result:
    print(test2)
