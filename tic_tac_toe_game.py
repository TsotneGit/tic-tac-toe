win_positions = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
]

winner = 0
move = 0

def print_2d(__board):
    for i in __board:
        print('|', end="")
        for j in i:
            print(j, end="|")
        print()

def check_winner(__board):
    for i in win_positions:
        count = 0
        temp = ""
        for j in i:
            if temp != "":
                if that:=__board[(j-1)//3][(j-1)%3] != temp and that != ".":
                    count = 0
                    break
                elif that != ".":
                    count += 1
            else:
                temp = that
                count += 1
        if count == 3:
            return temp
    return ""

def make_move(__board, _to, _who):
    global move
    if __board[(_to-1)//3][(_to-1)%3] != "X" and __board[(_to-1)//3][(_to-1)%3] != "O" and _to<=9:
        __board[(_to-1)//3][(_to-1)%3] = _who
        move += 1
    else:
        print("This cell is occupied")

            
