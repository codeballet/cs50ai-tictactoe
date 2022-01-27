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
    # Possible actions are EMPTY tiles in the board
    available = set()
    i = 0
    j = 0
    for row in board:
        for tile in row:
            if tile == EMPTY:
                available.add((i, j))
            j += 1
        i += 1

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Find out who just played
    last_player = None
    next_player = player(board)
    if next_player == X:
        last_player = O
    else:
        last_player = X

    # Add action of last player to board
    board[action[0]][action[1]] = last_player

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        row = []
        for j in range(3):
            row.append(board[i][j])
        if row == ["X", "X", "X"]:
            return X
        elif row == ["O", "O", "O"]:
            return O

    # Check columns
    for j in range(3):
        column = []
        for i in range(3):
            column.append(board[i][j])
        if column == ["X", "X", "X"]:
            return X
        elif column == ["O", "O", "O"]:
            return O

    # Check diagonals
    d1 = []
    for i in range(3):
        j = i
        d1.append(board[i][j])
    if d1 == ["X", "X", "X"]:
        return X
    elif d1 == ["O", "O", "O"]:
        return O

    d2 = []
    for i, j in zip(range(3), range(2, -1, -1)):
        d2.append(board[i][j])
    if d2 == ["X", "X", "X"]:
        return X
    elif d2 == ["O", "O", "O"]:
        return O

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If no EMPTY, game is over
    game = []
    for i in range(3):
        for j in range(3):
            game.append(board[i][j])

    if EMPTY not in game:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Identify winner
    winner = winner(board)

    # Return appropriate result
    if winner == X:
        return 1
    elif winner == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Get current player
    player = player(board)

    # Call max_value/min_value function for player
    if player == X:
        return max_value(board)
    elif player == O:
        return min_value(board)


def max_value(board):
    # Return the max value
    if terminal(board):
        return utility(board)

    v = -10
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v


def min_value(board):
    # Return the min value
    if terminal(board):
        return utility(board)
    
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v