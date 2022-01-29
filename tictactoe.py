"""
Tic Tac Toe Player
"""

import math
import random
import sys
sys.setrecursionlimit(10**2)
print(f'Recursion limit: {sys.getrecursionlimit()}')

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

    # else:
    #     raise Exception('Illegal move has been made!')


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Possible actions are EMPTY tiles in the board
    available = set()
    i = 0
    for row in board:
        j = 0
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
    # Find out current player
    current_player = player(board)

    # Add action of last player to board
    i = action[0]
    j = action[1]
    board[i][j] = current_player

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
    # Terminal if winner exists
    winner_exists = winner(board)

    if winner_exists == X or winner_exists == O:
        return True

    # Terminal if board is full
    game = []
    for i in range(3):
        for j in range(3):
            game.append(board[i][j])

    if EMPTY not in game:
        return True

    # Otherwise, not terminal
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Identify winner
    get_winner = winner(board)

    # Return appropriate result
    if get_winner == X:
        return 1
    elif get_winner == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print(f'minimax board argument: {board}')
    chosen_action = None

    if terminal(board):
        return None

    if board == initial_state():
        return random.choice(tuple(actions(board)))

    print(f'player: {player(board)}')
    if player(board) == X:
        best_score = -math.inf
        for action in actions(board):
            v = min_value(result(board, action))
            print(f'minimax X v: {v}')
            if v > best_score:
                best_score = v
                chosen_action = action
                print(f'minimax X chosen_action: {chosen_action}')
        print(f'X player chosen_action: {chosen_action}')
        return chosen_action
    else: # Player is O
        best_score = math.inf
        for action in actions(board):
            v = max_value(result(board, action))
            print(f'minimax O v: {v}')
            if v < best_score:
                best_score = v
                chosen_action = action
                print(f'minimax O chosen_action: {chosen_action}')
        print(f'O player chosen_action: {chosen_action}')
        return chosen_action


def max_value(board):
    print('Inside max_value')
    if terminal(board):
        print('max_value terminal')
        print(f'max_value utility: {utility(board)}')
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    print('Inside min_value')
    if terminal(board):
        print('min_value terminal')
        print(f'min_value utility: {utility(board)}')
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v