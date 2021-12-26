def make_move(board, col):
    for n, i in enumerate(board):
        if i[col] != "." and n <= 5:
            return n-1
        elif n == 5:
            return n
    else:
        return -1


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
                        counter = 1
                        last = j
                else:
                    last = j
                    counter += 1
            else:
                counter = 0
                last = ""

            if counter == 4:
                return j
    
    # Check vertically
    for col in range(7):
        counter = 0
        last = ""
        for row in range(6):
            if board[row][col] != ".":
                if last != "":
                    if last == board[row][col]:
                        counter += 1
                    else:
                        counter = 1
                        last = j
                else:
                    last = board[row][col]
                    counter += 1

            if counter == 4:
                return board[row][col]

    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] and board[row][col] != ".":
                return board[row][col]
    
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] and board[row][col] != ".":
                return board[row][col]