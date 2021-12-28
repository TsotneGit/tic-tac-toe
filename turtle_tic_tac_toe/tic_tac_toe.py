import time
import turtle
from tic_tac_toe_game import *
from voice_rec import get_audio

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
moves = 0
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

def draw_o(x=0, y=0, id_=1):
    global turn, moves
    # id_ = get_id(x,y)
    # Update playingboard matrix
    if make_move(board, id_, turn) == -1:
        return
    # Draw O
    t = turtle.Turtle()
    t.hideturtle()
    t.width(10)
    t.color("blue")
    t.penup()
    t.goto(-250+(((id_-1)%3+1)*2-1)*SPLITS2, 250-((id_-1)//3+1)*SPLITS+26)
    t.pendown()
    t.circle(60)
    t.penup()
    turn = "X"
    moves+=1

def draw_x(x=0, y=0, id_=1):
    global turn, moves
    # id_ = get_id(x,y)

    # Update playingboard matrix
    if make_move(board, id_, turn) == -1:
        return

    # Draw X
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
    t.penup()
    turn = "O"
    moves += 1   

# Closing
run = True
def exit_turtle():
    global run
    run = False
wn.listen()
wn.onkey(exit_turtle, "q")

# Listen to mouseclick events
def draw_char(x=0, y=0, id_=1):
    if turn == "X":
        draw_x(x,y, id_ = id_)
    else:
        draw_o(x,y, id_ = id_)
# wn.onclick(draw_char)

def end_game(won):
    wn.clear()
    wn.bgcolor("black")
    text_t = turtle.Turtle()
    text_t.hideturtle()
    text_t.color("white")
    if won != "":
        text_t.write(won+" won!", font=('Courier', 40), align="center")
    else:
        text_t.write("It's a tie!", font=('Courier', 40), align="center")
    wn.update()
    time.sleep(2)

# Main loop
while run:
    wn.update()
    audio = get_audio()
    if audio.isdigit():
        draw_char(id_=int(audio))
    winner = check_winner(board)
    if winner != "" or moves>=9:
        end_game(winner)
        run = False
    winner = check_winner(board)
    