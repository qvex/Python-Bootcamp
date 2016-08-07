gameBoard = {'top-L': '', 'top-M': '', 'top-R': '',
             'mid-L': '', 'mid-M': '', 'mid-R': '',
             'low-L': '', 'low-M': '', 'low-R': ''}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|')
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|')

turn = 'x'
for i in range(9):
    printBoard(gameBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    gameBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print(gameBoard)
