"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Check the number of X and O entries
    xs = 0
    os = 0
    for row in board:
        for tile in row:
            if tile == X:
                xs += 1
            elif tile == O:
                os += 1

    # If board is all EMPTY, return X
    if xs == 0 and os == 0:
        return X

    # If board has more X than O, return O
    if xs > os:
        return O

    # If board has equal X to O, return X
    if xs != 0 and os != 0 and xs == os:
        return X

    else:
        raise Exception('Illegal move has been made!')


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check rows
    for i in range(3):
        row = []
        for j in range(3):
            row.append(board[i][j])
        if row == ["X", "X", "X"] or row == ["O", "O", "O"]:
            return True

    # Check columns
    for j in range(3):
        column = []
        for i in range(3):
            column.append(board[i][j])
        if column == ["X", "X", "X"] or column == ["O", "O", "O"]:
            return True

    # Check diagonals
    d1 = []
    for i in range(3):
        j = i
        d1.append(board[i][j])
    if d1 == ["X", "X", "X"] or d1 == ["O", "O", "O"]:
        return True

    d2 = []
    for i, j in zip(range(3), range(2, -1, -1)):
        d2.append(board[i][j])
    if d2 == ["X", "X", "X"] or d2 == ["O", "O", "O"]:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
