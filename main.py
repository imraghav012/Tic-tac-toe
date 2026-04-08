import random

global row1, row2, row3, board, free_fields
row1 = [1, 2, 3]
row2 = [4, 'O', 6]
row3 = [7, 8, 9]
board = [row1, row2, row3]
free_fields = []
sign = False

def display_board(board):
    print('+-------' * 3 + '+')
    for i in range(3):
        print('|       |       |       |')
        print('|   ' + str(board[i][0]) + '   |   ' + str(board[i][1]) + '   |   ' + str(board[i][2]) + '   |')
        print('|       |       |       |')
        print('+-------'*3+'+')    

def enter_move(board):
    uMove = int(input('Enter your move: '))

    if uMove in [1,2,3,4,5,6,7,8,9]:
        for row in range(3):
            for column in range(3):
                if board[row][column] == uMove:
                    board[row][column] = 'X'

def make_list_of_free_fields(board):

    for i in range(9):
        if any(i in row for row in board):
            free_fields.append(i)
    return free_fields

winning_combinationsDone = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def victory_for(board, sign):
    if board[0][0] == 'X':
        if board[0][1] == 'X':
            if board[0][2] == 'X':
                return 'X'
        elif board[1][1] == 'X':
            if board[2][2] == 'X':
                return 'X'
        elif board[1][0] == 'X':
            if board[2][0] == 'X':
                return 'X'
    elif board[0][2] == 'X':
        if board[1][2] == 'X':
            if board[2][2] == 'X':
                return 'X'
        elif board[1][1] == 'X':
            if board[2][0] == 'X':
                return 'X'
    elif board[2][1] == 'X':
        if board[1][1] == 'X':
            if board[0][1] == 'X':
                return 'X'
        elif board[2][0] == 'X':
            if board[2][2] == 'X':
                return 'X'
    elif board [1][0] == 'X':
        if board[1][1] == 'X':
            if board[1][2] == 'X':
                return 'X'

    if board[0][0] == 'O':
        if board[0][1] == 'O':
            if board[0][2] == 'O':
                return 'O'
        elif board[1][1] == 'O':
            if board[2][2] == 'O':
                return 'O'
    elif board[0][2] == 'O':
        if board[1][2] == 'O':
            if board[2][2] == 'O':
                return 'O'
        elif board[1][1] == 'O':
            if board[2][0] == 'O':
                return 'O'
    elif board[2][1] == 'O':
        if board[1][1] == 'O':
            if board[0][1] == 'O':
                return 'O'
        elif board[2][0] == 'O':
            if board[2][2] == 'O':
                return 'O'
    elif board [1][0] == 'O':
        if board[1][1] == 'O':
            if board[1][2] == 'O':
                return 'O'
    return None

def draw_move(board):
    cMove = random.randrange(1, 10)
    while cMove not in make_list_of_free_fields(board):
        cMove = random.randrange(1, 10)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == cMove:
                board[i][j] = 'O' 

while sign == False:
    make_list_of_free_fields(board)
    display_board(board)
    enter_move(board)
    display_board(board)
    victory_for(board, sign)
    if victory_for(board, sign) == 'O':
        print('Computer wins!')
        break
    elif victory_for(board, sign) == 'X':
        print('You win!')
        break
    make_list_of_free_fields(board)
    draw_move(board)
    display_board(board)
    victory_for(board, sign)
    if victory_for(board, sign) == 'O':
        print('Computer wins!')
        break
    elif victory_for(board, sign) == 'X':
        print('You win!')
        break
