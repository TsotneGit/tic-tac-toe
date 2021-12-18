import turtle
from tic_tac_toe_game import *

BOARD_WITH_NUMBERS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

turn = "X"
count = 0
SPLITS = 166
SPLITS2 = 166//2
winner = ""

wn = turtle.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor("black")
wn.setup(500, 500)
wn.tracer(0)

for i in range(-84, 83, 166):
    line = turtle.Turtle()
    line.speed(0)
    line.color("white")
    line.shape("square")
    line.shapesize(stretch_wid=50, stretch_len=1)
    line.penup()
    line.goto(i, 250)
    line.pendown()
    line.goto(i, -250)

for i in range(-84, 83, 166):
    line = turtle.Turtle()
    line.speed(0)
    line.color("white")
    line.shape("square")
    line.shapesize(stretch_wid=1, stretch_len=50)
    line.penup()
    line.goto(250, i)
    line.pendown()
    line.goto(-250, i)

def get_id(x, y):
    if x<-84:
        if 82<y:
            return 1
        elif -84<y<82:
            return 4
        else:
            return 7

    elif -84<x<83:
        if 82<y:
            return 2
        elif -84<y<82:
            return 5
        else:
            return 8
        
    elif 83<x:
        if 82<y:
            return 3
        elif -84<y<82:
            return 6
        else:
            return 9

def draw_o(x, y):
    global turn
    # Draw O
    id_ = get_id(x,y)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(10)
    t.color("blue")
    t.penup()
    t.goto(-250+(((id_-1)%3+1)*2-1)*SPLITS2, 250-((id_-1)//3+1)*SPLITS+26)
    t.pendown()
    t.circle(60)
    
    # Update playingboard matrix
    make_move(board, id_, turn)

    turn = "X"

def draw_x(x, y):
    global turn
    id_ = get_id(x,y)
    t = turtle.Turtle()
    t.hideturtle()
    t.goto(-250+(((id_-1)%3+1)*2-1)*SPLITS2, 250-((id_-1)//3+1)*SPLITS+SPLITS2)
    t.color("red")
    t.penup()
    t.width(10)
    t.pendown()
    for angle in range(-135, 136, 90):
        mock = t.clone()
        mock.left(angle)
        mock.forward(SPLITS2)
    
    # Update playingboard matrix
    make_move(board, id_, turn)
    
    turn = "O"   

# Closing
run = True
def exit_turtle():
    global run
    run = False
wn.listen()
wn.onkey(exit_turtle, "q")

# Listen to mouseclick events
def draw_char(x,y):
    if turn == "X":
        draw_x(x,y)
    else:
        draw_o(x,y)
wn.onclick(draw_char)

# Main loop
while run:

    while count < 9:
        winner = check_winner(board)
        if winner != "":
            print(winner, "Won")
            break
        winner = check_winner(board)

    wn.update()