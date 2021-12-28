import turtle
from time import sleep

SPLITS = 100
SPLITS2 = 100//2
SCREEN_SIZE = (700, 600)
winner = ""
falling = False
turn = "yellow"
moves = 0
board = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."]
] 

wn = turtle.Screen()
wn.title("Connect Four")
wn.bgcolor("black")
wn.setup(*SCREEN_SIZE)
wn.tracer(0)
wn.cv._rootwindow.resizable(False, False)

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

SPLITS = 100
SPLITS2 = 100//2
SCREEN_SIZE = (700, 600)

def get_id(x, _):
    if -350<x<-250:
        return 0
    elif -250<=x<=-150:
        return 1
    elif -150<x<=-50:
        return 2
    elif -50<x<=50:
        return 3
    elif 50<x<=150:
        return 4
    elif 150<x<=250:
        return 5
    elif 250<x<=350:
        return 6

def draw_circle(x, y, color):
    global turn
    id_ = get_id(x,y)
    # Update playingboard matrix
    # if make_move(board, id_, turn) == -1:
    #     return
    t = turtle.Turtle()
    t.hideturtle()
    t.width(10)
    t.color(color)
    t.penup()
    t.goto(-350+((id_+1)*2-1)*SPLITS2, y)
    t.pendown()
    t.circle(30)
    t.penup()

for i in range(-250, 251, SPLITS):
    line = turtle.Turtle()
    line.speed(0)
    line.color("white")
    line.shape("square")
    line.shapesize(stretch_wid=60, stretch_len=1)
    line.penup()
    line.goto(i, 300)
    line.pendown()
    line.goto(i, -300)

for i in range(-200, 201, SPLITS):
    line = turtle.Turtle()
    line.speed(0)
    line.color("white")
    line.shape("square")
    line.shapesize(stretch_wid=1, stretch_len=70)
    line.penup()
    line.goto(300, i)
    line.pendown()
    line.goto(300, i)

def animation(x, y):
    global turn, moves, falling
    current_y = 220
    which = 0
    id_ = get_id(x,y)
    if not falling:
        falling = True
        while current_y>=-300 and board[which][id_] == ".":
            draw_circle(x, current_y, turn)
            if which!=5 and board[which+1][id_] == ".":
                sleep(0.1)
                wn.update()
                draw_circle(x, current_y, "black")
            current_y-=SPLITS
            which+=1
        falling = False
    
        move_row = make_move(board, id_)
        if move_row != -1:
            board[move_row][id_] = ["y", "r"][turn == "red"]
            turn = ["red", "yellow"][turn=="red"]
        moves += 1
    else:
        messagebox.showerror(title="Connect four", message="You can't make a move until it's your turn")

def show_winner(winner):
    t = turtle.Turtle()
    t.speed(0)
    t.width(10)
    t.hideturtle()
    t.color("green")
    t.penup()
    t.goto(-350+winner[3]*SPLITS+SPLITS2, 300-(winner[2])*SPLITS-SPLITS2)
    t.pendown()
    t.goto(-350+winner[1]*SPLITS+SPLITS2, 300-(winner[0]+1)*SPLITS+SPLITS2)
    wn.update()
    sleep(2)
    wn.clear()
    wn.bgcolor("black")
    text_t = turtle.Turtle()
    text_t.hideturtle()
    text_t.color("white")
    if winner != 0:
        text_t.write(["Yellow", "Red"][board[winner[0]][winner[1]]=="r"]+" won!", font=('Courier', 40), align="center")
    else:
        text_t.write("It's a tie!", font=('Courier', 40), align="center")
    wn.update()
    sleep(2)

run = True
def exit_turtle():
    global run
    run = False
wn.listen()
wn.onkey(exit_turtle, "q")
wn.onclick(animation)

while run:
    winner = check_winner(board)
    if type(winner) == tuple or moves == 42:
        show_winner(winner)
        break
    wn.update()