from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.move_speed = MOVE_DISTANCE

    def go_up(self):
        self.forward(self.move_speed)
        
    def  move_left(self):
        self.left(30)
        
    def move_right(self):
        self.right(30)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def decrease_speed(self):
        self.move_speed -= MOVE_INCREMENT