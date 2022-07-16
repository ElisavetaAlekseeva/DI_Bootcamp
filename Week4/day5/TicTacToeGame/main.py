# def display_board():
#     print('TIC TAC TOE')
#     board = ''
#     space = '\n'
#     for row in range(16):
#         horizontalTop = '*'
#         board += horizontalTop
#     for col in range(6):
#         vertical = "*"
#         board += vertical + ' '*15 + vertical + space
#     for row in range(17):
#         horizontalBottom = '*'
#         a = space * len(vertical)
#         board += horizontalBottom
#     print(board)
# display_board()

from xml.etree.ElementTree import TreeBuilder

def create_board():
    board = []
    for i in range(3):
        board.append([])
        for c in range(3):
            board[i].append('_')
    return board

def player_input(player, board):
    print(f"Player {player}'s turn...")
    row = input('Enter row: ')
    column = input('Enter column: ')
    board[int(row) - 1][int(column) - 1] = player


def check_win(board):
    row_len = len(board)
    column_len = len(board[0])
    x_array = ['X', 'X', 'X']
    o_array = ['O', 'O', 'O']
    for i in board:
        if o_array == i:
            print('Player O won!')
            return True
        elif x_array == i:
            print('Player X won!')
            return True
    column = []
    for i in range(len(board)):
        for c in board:
            column.append(c[i])
        if column == o_array:
            print('Player O won!')
            return True
        elif column == x_array:
            print('Player X won!')
            return True

    diagonal = []

    for i in range(len(board)):
        diagonal.append(board[i][i])
    
    if diagonal == x_array:
        print('Player X won!')
        return True
    elif diagonal == o_array:
        print('Player O won!')
        return True

    diagonal = []

    for i in range(len(board)):
        index = -i + len(board) - 1
        diagonal.append(board[index][index])

    if diagonal == x_array:
        print('Player X won!')
        return True
    elif diagonal == o_array:
        print('Player O won!')
        return True

def display_board(board):
    print('TIC TAC TOE')
    print("*****************")
    for i in range(len(board) * 2 - 1):
        if i % 2 == 0:
            print(f'*   {board[int(i/2)][0]} | {board[int(i/2)][1]} | {board[int(i/2)][2]}   *')
        else:
            print('*  ---|---|---  *')
    print("*****************")



def play():
    board = create_board()
    isX = True

    display_board(board)

    while True:
        if isX:
            player_input('X', board)
        else:
            player_input('O', board)
        
        isX = not isX

        display_board(board)

        isWin = check_win(board)

        if isWin:
            break

play()