import turtle
from connect_four_logic import *
from connect_four_drawing import *
from tkinter import messagebox
from time import sleep

SPLITS = 100
SPLITS2 = 100//2
SCREEN_SIZE = (700, 600)
winner = 0
turn = "yellow"
falling = False
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
    if not falling and not winner:
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
    elif not winner:
        messagebox.showerror(title="Connect four", message="You can't make a move until it's your turn")
    
    else:
        messagebox.showerror(title="Connect four", message="You can't make a move after player won")

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
    sleep(1)
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