
import numpy as np
import pygame
import math

ROWS=6
COLUMNS=7

board=np.zeros((ROWS,COLUMNS))

game_over=False
turn=0

SLOT=100
width=COLUMNS*SLOT
height=(ROWS+1)*SLOT
size=(width,height)

BACKGROUND=(58,56,57)
FRAME=(11,223,255)
PLAYER1=(255, 111, 11)
PLAYER2=(50, 42, 255)

OFFSET=100
RADIUS=int(SLOT/2-5)

def draw_board(board):
    pygame.draw.rect(window,BACKGROUND,(0,0,width,SLOT))
    for c in range(COLUMNS):
        for r in range(ROWS):
            rect=(c*SLOT,r*SLOT+OFFSET,SLOT,SLOT)
            c1=(int(c*SLOT+SLOT/2),int(r*SLOT+OFFSET+SLOT/2))
            pygame.draw.rect(window,FRAME,rect)
            pygame.draw.circle(window,BACKGROUND,c1,RADIUS)
    
    for c in range(COLUMNS):
        for r in range(ROWS):
            c2=(int(c*SLOT+SLOT/2),height-int(r*SLOT+SLOT/2))
            if board[r][c]==1:
                pygame.draw.circle(window,PLAYER1,c2,RADIUS)
            elif board[r][c]==2:
                pygame.draw.circle(window,PLAYER2,c2,RADIUS)

    pygame.display.update()


def is_valid_column(board,col):
    return board[ROWS-1][col]==0

def drop_piece(board,col,piece):
    for r in range(ROWS):
        if board[r][col]==0:
            row=r
            break
    board[row][col]=piece

def display_msg(msg,color):
    font = pygame.font.Font('freesansbold.ttf', 48)
    text = font.render(msg, True, BACKGROUND, color)
    textRect = text.get_rect()    
    textRect.center = (width/2,height/2)
    window.blit(text, textRect)

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

pygame.init()
window=pygame.display.set_mode(size)
pygame.display.set_caption("CodeRunner Connect 4")  
draw_board(board)    


while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(window,BACKGROUND,(0,0,width,SLOT))
            posx=event.pos[0]
            if turn%2==0:
                pygame.draw.circle(window,PLAYER1,(posx,int(SLOT/2)),RADIUS)
            else:
                pygame.draw.circle(window,PLAYER2,(posx,int(SLOT/2)),RADIUS)
            pygame.display.update()
        
        if event.type==pygame.MOUSEBUTTONDOWN:

            if turn%2==0:
                #Player 1
                col=math.floor(event.pos[0]/SLOT)
                
                if is_valid_column(board,col):
                    drop_piece(board,col,1)
                    if is_winning_move(board,1):
                        winner="Orange won"
                        color=PLAYER1
                        game_over=True
                else:
                    turn-=1

            else:
                #Player 2
                col=math.floor(event.pos[0]/SLOT)
                if is_valid_column(board,col):
                    drop_piece(board,col,2)
                    if is_winning_move(board,2):
                        winner="Blue won"
                        color=PLAYER2
                        game_over=True
                else:
                    turn-=1


            turn+=1
            draw_board(board)
    if game_over==True:
        display_msg(winner,color)
        pygame.display.update()
        pygame.time.wait(1000)
        display_msg("Game over!!!",color)
        pygame.display.update()
        pygame.time.wait(1000)
        display_msg("Starting new game...",color)
        pygame.display.update()
        pygame.time.wait(1000)
        board.fill(0)
        window.fill(BACKGROUND)
        draw_board(board)
        game_over=False
        pygame.display.update()

