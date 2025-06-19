"""
Tic Tac Toe Player
"""
import copy


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
    count = 0
    for i in board:
        for j in i:
            if j != EMPTY:
                count += 1

    if count %2 == 0:
        return X

    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    results = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                results.add((i,j))

    return results


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None or board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid move")

    current_board = copy.deepcopy(board)
    current_player = player(current_board)
    current_board[action[0]][action[1]] = current_player

    return current_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[i][0]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]



    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        best_value = float('-inf')
        best_action = None

        for action in actions(board):
            value = minvalue(result(board,action))

            if value > best_value:
                best_value = value
                best_action = action
        return best_action


    if player(board) == O:
        best_value = float('inf')
        best_action = None

        for action in actions(board):
            value = maxvalue(result(board,action))

            if value < best_value:
                best_value = value
                best_action = action
        return best_action


def maxvalue(board):
    if terminal(board):
        return utility(board)

    value = float('-inf')

    for action in actions(board):
        value = max(value, minvalue(result(board,action)))
    return value


def minvalue(board):
    if terminal(board):
        return utility(board)

    value = float('inf')

    for action in actions(board):
        value = min(value, maxvalue(result(board,action)))
    return value
