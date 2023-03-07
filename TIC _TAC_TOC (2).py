import sys
board=[" " for i in range(1,10)]
def print_board():
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print('----+---+----')
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print('----+---+----')
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
def playermove(token):
    print("\n it's {} turn".format(token))
    choice=int(input("\n choose your move(1-9): "))
    if board[choice-1]==" ":
        board[choice-1]=token
    else:
        print("\n The space is already taken!>>")
        print("choice another place<<<")    
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
def is_draw():
    if " " not in board:
        print("It's a draw!")
        sys.exit()
while True:
    print_board()
    playermove("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!\n")
        break
    elif is_draw():
        break
    playermove("O")
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!\n")
        break
    elif is_draw():
        break
