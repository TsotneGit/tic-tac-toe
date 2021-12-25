import turtle 

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


# def draw_circle(x, _):
#     global turn, moves
#     id_ = get_id(x,_)
#     # Update playingboard matrix
#     # if make_move(board, id_, turn) == -1:
#     #     return
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.width(10)
#     t.color("yellow")
#     current_y = 215
#     while current_y>-300:
#         t.color("yellow")
#         t.penup()
#         t.goto(-350+((id_+1)*2-1)*SPLITS2, current_y)
#         t.pendown()
#         t.circle(30)
#         wn.delay(10000)
#         wn.update()
#         t.color("black")
#         t.goto(-350+((id_+1)*2-1)*SPLITS2, current_y)
#         if current_y>-200:
#             t.circle(30)
#         else:
#             t.color("yellow")
#             t.circle(30)
#         current_y-=100

#     t.penup()
#     turn = "X"
#     moves+=1
