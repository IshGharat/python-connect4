
import numpy as np

ROWS=6
COLUMNS=7

board=np.zeros((ROWS,COLUMNS))

game_over=False
turn=0

def is_valid_column(board,col):
    return board[ROWS-1][col]==0

def drop_piece(board,col,piece):
    for r in range(ROWS):
        if board[r][col]==0:
            row=r
            break
    board[row][col]=piece

def is_winning_move(board,piece):

    #Check horizontal location win
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    
    #Check vertical loaction win
    for r in range(ROWS-3):
        for c in range(COLUMNS):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
            
    #Check for positive diagonal win
    for c in range(COLUMNS-3):
        for c in range(ROWS-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    
    #Check for negative diagonal win
    for c in range(COLUMNS-3):
        for r in range(3,ROWS):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

            

print(board)
while not game_over:
    if turn%2==0:
        #Player 1
        col=int(input("Player 1: Select column (0-6): "))
        if (-1<col<7):
            if is_valid_column(board,col):
                drop_piece(board,col,1)
                if is_winning_move(board,1):
                    print("Player 1 won")
                    game_over=True
            else:
                turn-=1
        else:
            turn-=1

    else:
        #Player 2
        col=int(input("Player 2: Select column (0-6): "))
        if (-1<col<7):
            if is_valid_column(board,col):
                drop_piece(board,col,2)
                if is_winning_move(board,2):
                    print("Player 2 won")
                    game_over=True
            else:
                turn-=1
        else:
            turn-=1






    turn+=1
    print(np.flip(board,0))

