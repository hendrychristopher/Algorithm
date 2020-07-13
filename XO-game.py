print('XO - game!!')
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
current_player = 'X'
still_going = True

def play_game():
    global current_player
    display_board()
    while still_going:
        handle_turn(current_player)
        check_gameover()
        change_player()


def display_board():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])

def handle_turn(current_player):
    already_entered = True
    while already_entered:
        position_valid = True
        while position_valid:
            print(current_player +"'s turn...")
            position = input('Enter the position in between 1-9: ')
            if position not in ['1','2','3','4','5','6','7','8','9']:
                print('"INVALID" **** Enter the position in between 1-9: ')
            else:
                position_valid = False

        if board[int(position)-1] == '-':
            board[int(position) - 1] = current_player
            already_entered = False
        else:
            print("Already entered in this position. Try some other position")

    display_board()

def check_gameover():
    global still_going,current_player

    if check_winner():
        still_going = False
        print(current_player,' won the game!!')
    elif check_tie():
        still_going = False


def check_winner():
    global board

    # checking rows
    if board[0] == board[1] == board[2] != '-':
        return True
    elif board[3] == board[4] == board[5] != '-':
        return True
    elif board[6] == board[7] == board[8] != '-':
        return True

    # checking columns
    elif board[0] == board[3] == board[6] != '-':
        return True
    elif board[1] == board[4] == board[7] != '-':
        return True
    elif board[2] == board[5] == board[8] != '-':
        return True

    # checking diagonals
    elif board[0] == board[4] == board[8] != '-':
        return True
    elif board[2] == board[4] == board[6] != '-':
        return True

def check_tie():
    global still_going
    if '-' not in board:
        still_going = False
        print("it's tie.")

def change_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

play_game()