"""
Tic Tac Toe Player
"""

"""MOVING FORWARD IDEA: MAYBE IT WOULD BE MUCH MORE BENIFITIAL TO ALSO MAKE MY OWN PROJECTS WITH THE AIs, AND IMPLEMENT THEM INTO THINGS IM FAMILIAR WITH."""

import math
import copy

X = "X"
O = "O"
EMPTY = ""


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
    xCount = 0
    oCount = 0
    #player checks whos turn it is, if there is a X on the board, it will be O's turn, and if a O is on the board, it will be X's turn.
    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                xCount += 1
            elif board[row][col] == O:
                oCount += 1
    print(xCount, oCount, "X O")

    if xCount > oCount:
        return O
    elif xCount < oCount:
        return X
    else:
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
    print(action, "ACTION")
    if action is not None:
        print(action)
        if player(board) == X:
            
            print(board, "Xturn")
            newBoard = copy.deepcopy(board)
            newBoard[action[0]][action[1]] = X
            print("board after a move", newBoard)
            return newBoard
        elif player(board) == O:
            
            print(board, "Oturn")
            newBoard = copy.deepcopy(board)
            newBoard[action[0]][action[1]] = O
            print("board after a move", newBoard)
            return newBoard
    
    
    print("board is being dumb")


    
    


    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #Rapid Win/Lose Check
    #rowCheck

    #Charles diagonal Check
    print("diagonal check")
    print(board[0][0], board[1][1], board[2][2])
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
        
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    
    #other diagonal Check
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X

    #Side To Side check
    print("side to side check")
    print(board)
    for row in board:
        if row[0] == X and row[1] == X and row[2] == X:
            return X
        elif row[0] == O and row[1] == O and row[2] == O:
            return O
        
            

    #jimbo up and down check
    for row in range(3):
        if board[0][row] == X and board[1][row] == X and board[2][row] == X:
            return X
            
           
        if board[0][row] == O and board[1][row] == O and board[2][row] == O:
           return O
    
    
    
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    print("TERMAINAL CHECK BOARD", board)
    if winner(board) == X or winner(board) == O:
        return True
    elif actions(board) == None:
        return True
    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    print("UTILITY CHECK BOARD", board)
    if terminal(board):
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
    
    
    if player(board) == O:
        m,movee = min_value(board)
        return movee
    if player(board) == X:
        m,movee = max_value(board)
        return movee




def maxErValue(board):
    #returns max value of board/ and the optimal move
    if terminal(board):
        print("Board is filled")

        return None
    
    move = None
    v = float("-inf")
    for action in actions(board):
        actionPotential = minnerValue(result(board, action))
        print(utility(actionPotential), "UTIACTION")
        
        if utility(actionPotential) > v:
            move = action
            v = utility(actionPotential)
            if v == 1:
                return move 
            
    return move







def minnerValue(board):
    #returns max value of board/ and the optimal move
    if terminal(board):
        print("Board is filled")
        print(winner(board))

        return None
    move = None
    v = float("inf")
    for action in actions(board):
        #the entire board is solved before we even leave for loop
        actionPotential = maxErValue(result(board, action))
        print(utility(actionPotential), "UTIACTION")
        if utility(actionPotential) < v:
            
            move = action
            v = utility(actionPotential)
            if v == -1:
                return move 
    return move


   
#v is used to help store what the optimal value of the best move is. 
def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move



def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move


        
        


def playBestOnX(actionsToTest, CORRESPONDING_ACTIONS):
    print(actionsToTest, "ACTIONS\n", CORRESPONDING_ACTIONS, "GOOGLEd\n")
    moves_utilities = []
    for sendableAction in CORRESPONDING_ACTIONS:
        for move in actionsToTest:
            print("MOVE", move)
            print("ACTION", sendableAction)
            
            print(sendableAction, move, "gig")
            potentialUtil = utility(move)
            print("UTIL", potentialUtil)
            if potentialUtil == 1:
                print(sendableAction, "I PLAY THIS")
                return sendableAction
            
    #if all fails, play 0 move but always ignore bad move
    print("playing long game")
    for sendableAction in CORRESPONDING_ACTIONS:
        for move in actionsToTest:
            
            print(sendableAction, move, "gigidy")
            potentialUtil = utility(move)
            
            if potentialUtil == -1:
                return sendableAction
            else:
                return sendableAction
    
    
            
            

            
            
        
            


    
    











