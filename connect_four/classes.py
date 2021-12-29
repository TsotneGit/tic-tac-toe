import turtle


class Game:
    SPLITS = 100
    SPLITS2 = 100 // 2
    SCREEN_SIZE = (700, 600)

    def __init__(self):
        self.board = [
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
        ]

        self.turn = "yellow"
        self.move_count = 0
        self.falling = False
        self.winner = 0
        self.run = True

        self.wn = turtle.Screen()
        self.wn.title("Connect Four")
        self.wn.bgcolor("black")
        self.wn.setup(*self.SCREEN_SIZE)
        self.wn.tracer(0)
        self.wn.cv._rootwindow.resizable(False, False)

        self.wn.listen()
        self.wn.onkey(self.exit_turtle, "q")

        self.draw_board()
        self.main_loop()

    def draw_board(self):
        for i in range(-250, 251, self.SPLITS):
            self.line = turtle.Turtle()
            self.line.speed(0)
            self.line.color("white")
            self.line.shape("square")
            self.line.shapesize(stretch_wid=60, stretch_len=1)
            self.line.penup()
            self.line.goto(i, 300)
            self.line.pendown()
            self.line.goto(i, -300)

        for i in range(-200, 201, self.SPLITS):
            self.line = turtle.Turtle()
            self.line.speed(0)
            self.line.color("white")
            self.line.shape("square")
            self.line.shapesize(stretch_wid=1, stretch_len=70)
            self.line.penup()
            self.line.goto(300, i)
            self.line.pendown()
            self.line.goto(300, i)

    def exit_turtle(self):
        self.run = False

    def main_loop(self):
        while self.run:
            self.wn.update()


Game()
