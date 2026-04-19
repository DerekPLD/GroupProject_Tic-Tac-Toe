import pygame
import random
from pygame.locals import *


RED=(255,0,0)
MARKX='X'
MARKO='O'
BOARD=['','','','','','','','','']
WIN=-1


def resetBoard(board):
    for i in range(9):
        board[i]=''

def displayX(position,rect):
    font=pygame.font.Font(None, 80)
    x=font.render(MARKX,True,RED)
    xpos=x.get_rect()
    xpos.centerx=rect.centerx
    xpos.centery=rect.centery
    screen.blit(x,xpos)


def displayO(position,rect):
    font=pygame.font.Font(None, 80)
    o=font.render(MARKO,True,RED)
    opos=o.get_rect()
    opos.centerx=rect.centerx
    opos.centery=rect.centery
    screen.blit(o,opos)


def makeX(position,board,rect):
    if board[position]=='':
        board[position]='X'
        displayX(position,rect)

def makeO(position,board,rect):
    if board[position]=='':
        board[position]='O'
        displayO(position,rect)

def drawline(screen,first_point,second_point):
    pygame.draw.line(screen,RED,first_point,second_point,3)
    pygame.display.update()


def winner(board,t):
    win=False
    if board[0]==board[1]==board[2]=='O' or board[0]==board[1]==board[2]=='X':

        point1=[0,50]
        point2=[300,50]
        win=True

    elif board[3]==board[4]==board[5]=='O' or board[3]==board[4]==board[5]=='X':

        point1=[0,150]
        point2=[300,150]
        win=True
    elif board[6]==board[7]==board[8]=='O' or board[6]==board[7]==board[8]=='X':

        point1=[0,250]
        point2=[300,250]
        win=True
    elif board[0]==board[3]==board[6]=='O' or board[0]==board[3]==board[6]=='X':

        point1=[50,0]
        point2=[50,300]
        win=True
    elif board[1]==board[4]==board[7]=='O' or board[1]==board[4]==board[7]=='X':

        point1=[150,0]
        point2=[150,300]
        win=True
    elif board[2]==board[5]==board[8]=='O' or board[2]==board[5]==board[8]=='X':

        point1=[250,0]
        point2=[250,300]
        win=True
    elif board[0]==board[4]==board[8]=='O' or board[0]==board[4]==board[8]=='X':

        point1=[0,0]
        point2=[300,300]
        win=True
    elif board[2]==board[4]==board[6]=='O' or board[2]==board[4]==board[6]=='X':

        point1=[300,0]
        point2=[0,300]
        win=True

    if t==1 and win:
        drawline(screen,point1,point2)
    return win


def BoardisEmpty(board):
    check = True
    for i in range(9):
        if board[i] !='':
            check = False
    return check

def BoardisFull(board):
    check = True
    for i in range(9):
        if board[i] =='':
            check = False
    return check

def Boxisempty(board,box):
    if board[box]=="":
        return True
    return False

def getComputerMove(board):
    box=-1
    rect=-1

    for n in range(9):
        boardcopy=board.copy()
        if boardcopy[n]=="":
            boardcopy[n]=MARKX
            if winner(boardcopy,0):
                box=n
                rect=rect_list[n]

    if board[4]=="":
        box=4
        rect=rect_list[4]
    elif board[0]=="" or board[2]=="" or board[6]=="" or board[8]=="":

        while box==-1:
            test=random.randrange(0,9,2)
            if board[test]=="":
                box=test
                rect=rect_list[box]

    for n in range(9):
        boardcopy=board.copy()
        if boardcopy[n]=="":
            boardcopy[n]=MARKO
            if winner(boardcopy,0):
                box=n
                rect=rect_list[n]

    if box==-1:
        for n in range(9):
            boardcopy=board.copy()
            if boardcopy[n]=="":
                box=n
                rect=rect_list[n]

    return box, rect

def getUserMove(pos):
    for i in range(9):
        if rect_list[i].collidepoint(pos):
            box=i
            rect=rect_list[i]
    return box, rect


def main():
    global screen,background
    global rect_list
    MOVE=0 # 0 is user, 1 is computer
    pygame.init()
    screen=pygame.display.set_mode((300,300))
    pygame.display.set_caption("tictactoe")

    #fill background
    background=pygame.Surface(screen.get_size())
    background=background.convert()
    background.fill((0,0,0))
    #draw board
    pygame.draw.line(background, RED, [0,100], [300,100], 3)
    pygame.draw.line(background, RED, [0,200], [300,200], 3)
    pygame.draw.line(background, RED, [100,0], [100,300], 3)
    pygame.draw.line(background, RED, [200,0], [200,300], 3)
    rect1 = pygame.Rect(0,0,100,100)
    rect2 = pygame.Rect(100,0,100,100)
    rect3 = pygame.Rect(200,0,100,100)
    rect4 = pygame.Rect(0,100,100,100)
    rect5 = pygame.Rect(100,100,100,100)
    rect6 = pygame.Rect(200,100,100,100)
    rect7 = pygame.Rect(0,200,100,100)
    rect8 = pygame.Rect(100,200,100,100)
    rect9 = pygame.Rect(200,200,100,100)
    rect_list=[rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9]
    #bilt to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    box = -1
    t = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                #decide user click which space
                box,u_rect=getUserMove(pos)
                if Boxisempty(BOARD,box):
                    useract=1


        if not winner(BOARD,t) and box !=-1:

            if MOVE==0 and useract==1:
                makeX(box,BOARD,u_rect)
                MOVE=1
                useract=0
            elif MOVE==1:
                box,u_rect=getComputerMove(BOARD)
                pygame.time.wait(300)
                makeO(box,BOARD,u_rect)
                MOVE=0
        elif winner(BOARD,t) and MOVE==0:
            print("winner is computer")
            winner(BOARD,t)
            #refresh the game board
            pygame.time.wait(1000)
            screen.blit(background, (0, 0))
            resetBoard(BOARD)
            MOVE=0
            box = -1
        elif winner(BOARD,t) and MOVE==1:
            print("winner is user")
            winner(BOARD,t)
            #refresh the game board
            pygame.time.wait(1000)
            screen.blit(background, (0, 0))
            resetBoard(BOARD)
            MOVE=0
            box = -1
        elif BoardisFull(BOARD):
            print("tie!!!!")
            pygame.time.wait(1000)
            screen.blit(background, (0, 0))
            resetBoard(BOARD)
            MOVE=0
            box = -1

        pygame.display.update()

if __name__ == '__main__': main()
