"""
Tic Tac Toe Player
"""

import math
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
    #player checks whos turn it is, if there is a X on the board, it will be O's turn, and if a O is on the board, it will be X's turn.
    if X in board:
        return O
    elif O in board:
        return X
    else:   #if no turn is on the board, return X's turn
        return X



    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    #test each row of the board
    for i in range(3):
        #test each column of the board
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j)) #each action is represted by a tuple (i, j), each (i, j) in the set is a position on the board (0,0) is the top left corner
    
    return actions




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is not None:
        newBoard = copy.deepcopy(board)
        newboard = newboard[action[0]][action[1]]
        return newboard


    else:
        raise Exception("Not a valid Action")
    


    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #Side To Side check
    for row in board:
        if row[0] == X and row[1] == X and row[2] == X:
            return X
        elif row[0] == O and row[1] == O and row[2] == O:
            return O
        
            

    #jimbo up and down check
    for col in range(3):
        if board[0][col] == X and board[1][col] == X and board[2][col] == X:
            return X
            
           
        if board[0][col] == O and board[1][col] == O and board[2][col] == O:
           return O
    
    #Charles diagonal Check
    if board[0][0] == X and board[1][1] == O and board[2][2] == X or board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
        
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O or board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    
    return None
    

    
    
        
        
 


    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
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



