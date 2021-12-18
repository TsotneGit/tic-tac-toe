import turtle

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

wn = turtle.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor("black")
wn.setup(500, 500)
wn.tracer(0)
turn = "O"
SPLITS = 166
SPLITS2 = 166//2

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
    id_ = get_id(x,y)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(10)
    t.color("blue")
    t.penup()
    t.goto(-250+(((id_-1)%3+1)*2-1)*SPLITS2, 250-((id_-1)//3+1)*SPLITS+26)
    t.pendown()
    t.circle(60)

def draw_x(x, y):
    pass
    

# Closing
run = True
def exit_turtle():
    global run
    run = False
wn.listen()
wn.onkey(exit_turtle, "q")

# Listen to mouseclick events
wn.onclick(lambda x,y: [draw_o(x,y), draw_x(x,y)][turn=="X"])
# wn.onclick(draw_o)

# Main loop
while run:
    wn.update()