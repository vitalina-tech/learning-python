import random
board_size=5
board=[['0']*5 for _ in range(board_size)]
ship_row=random.randint(0,board_size-1)
ship_col=random.randint(0,board_size-1)
def print_board(board):
    for row in board:
        print(' '.join(row))
print("Let's play Battleship!")
print_board(board)
for turn in range(1,6):
    print(f"\nTurn {turn}")
    guess_row=int(input("Guess Row (0-4):"))
    guess_col=int(input("Guess Col (0-4):"))
    if guess_row==ship_row and guess_col==ship_col:
        print("You hit my battleship! You win!")
        board[guess_row][guess_col]="X"
        print(print_board)
        break
    elif 0<=guess_row<board_size and 0<=guess_col<board_size:
        if board[guess_row][guess_col]=="X":
            print("You already tried this spot!")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col]="X"
    else:
        print("That's not even in the ocean!")
    print_board(board)
    if turn==5:
        print("\nGame Over. The ship was at:", ship_row, ship_col)