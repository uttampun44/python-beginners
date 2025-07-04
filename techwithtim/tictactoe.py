board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]


def print_board(board):
    for i, row in enumerate(board):
        # insert a new line after each row
        row_str = ""
        for j, item in enumerate(row):
            row_str += str(item)
            if j < len(row) - 1:
                row_str += " | "
        print(row_str)
        if i != len(board) - 1:
           print("-----------")
        
# player move function
def get_player_move(turn, board):

    # inserting the player's turn in row and column 
    while True:
        row = int(input(f"Player {turn}'s turn. Enter row: "))
        col = int(input(f"Player {turn}'s turn. Enter column: "))
        
        if row < 1 or row > len(board):
            print("Invalid Row ! Please try again")
        elif col < 1 or col > len(board[row - 1]):
                print("Invalid Column ! Please try again")
        elif board[row - 1][col - 1] != "":
            print("Cell is already filled ! Please try again")
        else:
            break

    board[row - 1][col - 1] = turn

def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None


turn_x = "X"
turn_0 = 0

print_board(board)
while True:
    print("Player X's turn", turn_x, "Please enter your move")
    get_player_move(turn_x, board)
    print_board(board)
    print("Player 0 's turn", turn_0, "Please enter your move")
    get_player_move(turn_0, board)
    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins the game")
        break
    else:
        turn_x, turn_0 = turn_0, turn_x
        print("It's a tie")
