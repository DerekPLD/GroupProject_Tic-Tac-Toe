import random


def drawBoard(board):
     # Print the board


    # "board" is a list of length 10. For convenience, we ignore the first element board[0].


    print('\n\n\n\n')
    print('\t\t\t┌───┬───┬───┐')
    print(f'\t\t\t│ {board[7]} │ {board[8]} │ {board[9]} │   (7 8 9)')
    print('\t\t\t├───┼───┼───┤')
    print(f'\t\t\t│ {board[4]} │ {board[5]} │ {board[6]} │   (4 5 6)')
    print('\t\t\t├───┼───┼───┤')
    print(f'\t\t\t│ {board[1]} │ {board[2]} │ {board[3]} │   (1 2 3)')
    print('\t\t\t└───┴───┴───┘')


def inputPlayerLetter():
    # Let the player choose a letter
    # Return a list: first is the player’s letter, second is the computer’s
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()


    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly decide who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # Play again? Input yes or y returns True
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
     # Place a movement
    board[move] = letter


def isWinner(bo, le):
    # Check if the given letter has won
    # Parameters: board list and letter symbol
    # There are 8 possible winning combinations
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    # Make a copy of the board for computer move simulation
    dupeBoard = []


    for i in board:
        dupeBoard.append(i)


    return dupeBoard


def isSpaceFree(board, move):
    # Check if a position is free. Return True if empty
    return board[move] == ' '


def getPlayerMove(board):
    # Player movement
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Randomly return a move from the list if available
    # If none are free, return None
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)


    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Determine computer’s movement
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    # Tic Tac Toe AI core algorithm:
    # First, check if computer can win in one move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i


    # Block player if they could win next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i


    # Take a corner if available
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move


    # Take center if available
    if isSpaceFree(board, 5):
        return 5


   # Take a side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if the board is full
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True




print('Welcome to Tic Tac Toe!')


while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True


    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)


            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'


        else:
            # Computer’s turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)


            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'


    if not playAgain():
        break
