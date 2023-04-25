def printboard(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r']+'|')
    print('-'+'+'+'-'+'+'+'-'+'+')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r']+'|')
    print('-'+'+'+'-'+'+'+'-'+'+')
    print(board['low-l']+'|'+board['low-m']+'|'+board['low-r']+'|')
    print('-'+'+'+'-'+'+'+'-'+'+')
def play(board):
    turn='X'
    for i in range(9):
        move=input()
        if board[move] in 'XO':
            print('Select another position')
        board[move]=turn
        printboard(board)
        if turn == 'X':
            turn='O'
        else:
            turn='X'
        if i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
            if ((board['top-l'] == 'X' and board['top-m'] == 'X' and board['top-r'] == 'X') or (board['mid-l'] == 'X' and board['mid-m'] == 'X' and board['mid-r'] == 'X') or (board['low-l'] == 'X' and board['low-m'] == 'X' and board['low-r'] == 'X') or (board['top-l'] == 'X' and board['mid-m'] == 'X' and board['low-r'] == 'X') or (board['top-r'] == 'X' and board['mid-m'] == 'X' and board['low-l'] == 'X') or (board['top-l']=='X' and board['mid-l']=='X' and board['low-l']=='X') or (board['top-m']=='X' and board['mid-m']=='X' and board['low-m']=='X') or (board['top-r']=='X' and board['mid-r']=='X' and board['low-r']=='X')):
                print('X is the Winner')
                break
            elif ((board['top-l'] == 'O' and board['top-m'] == 'O' and board['top-r'] == 'O') or (board['mid-l'] == 'O' and board['mid-m'] == 'O' and board['mid-r'] == 'O') or (board['low-l'] == 'O' and board['low-m'] == 'O' and board['low-r'] == 'O') or (board['top-l'] == 'O' and board['mid-m'] == 'O' and board['low-r'] == 'O') or (board['top-r'] == 'O' and board['mid-m'] == 'O' and board['low-l'] == 'O')or (board['top-l']=='O' and board['mid-l']=='O' and board['low-l']=='O') or (board['top-m']=='O' and board['mid-m']=='O' and board['low-m']=='O') or (board['top-r']=='O' and board['mid-r']=='O' and board['low-r']=='O')):
                print('O is the Winner')
                break
            else:
                continue
    else:
        print('Match Draw')
board={'top-l':' ','top-m':' ','top-r':' ','mid-l':' ','mid-m':' ','mid-r':' ','low-l':' ','low-m':' ','low-r':' '}
printboard(board)
play(board)
