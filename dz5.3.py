# Крестики-нолики

board = list(range(1,10))

def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

def choice(gamer):
    valid = False
    while not valid:
        gamer_index = input(f'Xод {gamer}, выберите ячейку:')
        try:
            gamer_index =int(gamer_index)
        except:
            print('Некорректный ввод')
            continue
        if gamer_index >= 1 and gamer_index <= 9:
            if(str(board[gamer_index-1]) not in 'XO'):
                board[gamer_index-1] = gamer
                valid = True
            else:
                print('Ячейка занята')
        else:
            print('Еще раз попробуй')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    counter =0
    vic = False
    while not vic:
        design_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('O')
        counter +=1
        if counter > 4:
            winner = victory_check(board)
            if winner:
                print(winner,'Победа')
                vic = True
                break
            if counter == 9:
                print('Ничья)')
        design_board(board)
game(board)