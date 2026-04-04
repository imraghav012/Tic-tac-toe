import random

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
board = [row1, row2, row3]
print(board[0][1])





def display_board(board):
    print('+-------' * 3 + '+')
    for i in range(3):
        print('        |       |       ')
        print('    ' + str(board[i][0]) + '   |   ' + str(board[i][1]) + '   |   ' + str(board[i][2]))
        print('        |       |       ')
        if i != 2:
            print('+-------'*3+'+')

def enter_move(board):
    uMove = input('Enter your move:')
    if uMove in '123456789':
        uMove = int(uMove)
        for i in range(3):
            for j in range(3):
                if board[i][j] == uMove:
                    board[i][j] = 'X'

    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
'''
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

def draw_move(board):
    # The function draws the computer's move and updates the board.
'''
display_board(board)
enter_move(board)
