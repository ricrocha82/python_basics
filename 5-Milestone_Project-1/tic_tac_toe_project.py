# tic_tac_toe_project.py
import random

board = ["-", "-", "-",
         "-","-","-",
         "-","-","-"]

current_player = "X"
winner = None
game_running = True

# printing the game board
def print_board(board):
    print("Here is the current board")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
def player_input(board):
    while True:
        if current_player == "X":
            inp = int(input(f"Enter a number 1-9 \033[1;34m Player (X) \033[0;0m : "))
        else:
            inp = int(input(f"Enter a number 1-9 \033[1;31m Player (0) \033[0;0m : "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = current_player
            break
        else:
            if current_player == "X":
                print(f"Oops! Try again! Player - \033[1;34m Player (X) \033[0;0m ! ")
            else:
                print(f"Oops! Try again! Player - \033[1;31m Player (0) \033[0;0m ! ")
            print_board(board)


# check for win or tie
def check_horizontal(board):
    global winner # if winner changges, winner will be modified in the entire file
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = current_player
        return True # if this funtion is TRUE, so we can stop the game
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = current_player
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = current_player
        return True
    
def check_vertical(board):
    global winner # if winner changges, winner will be modified in the entire file
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True # if this funtion is TRUE, so we can stop the game
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def check_cross(board):
    global winner # if winner changges, winner will be modified in the entire file
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True # if this funtion is TRUE, so we can stop the game
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print('It is a tie!!')
        game_running = False

# put all the win functions together
def check_win():
    if check_cross(board) or check_horizontal(board) or check_vertical(board):
        print(f"The winner is {winner}")

# switch the player
def change_player():
    global current_player
    if current_player == "X":
        current_player = "O" # reasing the variable
    else:
        current_player = "X"

# computer
def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            change_player()

# check for win of tie again
while game_running:
    print_board(board)
    if winner != None:
        break
    player_input(board)
    check_win()
    check_tie(board)
    change_player()
    computer(board)
    check_win()
    check_tie(board)

