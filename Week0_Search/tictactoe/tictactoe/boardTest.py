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
    

    
    
        
        
        
    
     

        

        

        
        
        



from tictactoe import minimax, result

          



X = "X"
O = "O"
EMPTY = ""

sampleboard = [[EMPTY, EMPTY, EMPTY,],
               [EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, X]
]

print(minimax(sampleboard))

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
      
print(actions(sampleboard), "empto")

print(sampleboard, "start state")

print(winner(sampleboard))




