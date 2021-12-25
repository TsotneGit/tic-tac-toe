def make_move(board, col):
    for n, i in enumerate(board):
        if i[col] != ".":
            return n-1
        elif n == 5:
            return n