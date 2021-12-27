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
    for row in range(6):
        counter = 0
        last = ""
        first_row = 0
        first_col = 0
        for col in range(7):
            if board[row][col] != ".":
                if last != "":
                    if last == board[row][col]:
                        counter += 1
                    else:
                        counter = 1
                        last = board[row][col]
                        first_row = row
                        first_col = col
                else:
                    last = board[row][col]
                    counter += 1
                    first_row = row
                    first_col = col
            else:
                counter = 0
                last = ""
                first_row = row
                first_col = col

            if counter == 4:
                return (row, col, first_row, first_col)
    
    # Check vertically
    for col in range(7):
        counter = 0
        last = ""
        first_row = 0
        first_col = 0
        for row in range(6):
            if board[row][col] != ".":
                if last != "":
                    if last == board[row][col]:
                        counter += 1
                    else:
                        counter = 1
                        last = board[row][col]
                        first_row = row
                        first_col = col
                else:
                    last = board[row][col]
                    counter += 1
                    first_row = row
                    first_col = col

            if counter == 4:
                return (row, col, first_row, first_col)

    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] and board[row][col] != ".":
                return (row+3, col+3, row, col)
    
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] and board[row][col] != ".":
                return (row+3, col-3, row, col)