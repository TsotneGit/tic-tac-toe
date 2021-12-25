board = [
    ["y", ".", ".", ".", ".", ".", "."],
    ["y", ".", ".", ".", ".", ".", "."],
    ["y", ".", ".", ".", ".", ".", "."],
    ["y", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."]
] 

def make_move(board, col):
    for n, i in enumerate(board):
        if i[col] != ".":
            return n-1
        elif n == 5:
            return n

def check_winner(board):
    # Check horizontally
    for row in board:
        counter = 0
        last = ""
        for j in row:
            if j != ".":
                if last != "":
                    if last == j:
                        counter += 1
                    else:
                        counter = 0
                        last = j
                else:
                    last = j
                    counter += 1

            if counter == 4:
                return j

    for col in range(7):
        counter = 0
        last = ""
        for row in range(6):
            if board[row][col] != ".":
                if last != "":
                    if last == board[row][col]:
                        counter += 1
                    else:
                        counter = 0
                        last = j
                else:
                    last = board[row][col]
                    counter += 1

            if counter == 4:
                return board[row][col]

print(check_winner(board))