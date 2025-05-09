import turtle
import time

class cursorcontrol:

    wn=None
    space=None
    speed=1
    banner = None
    
    def __init__(self):
        self.wn=turtle.Screen()
        self.wn.setup(width=600,height=600)
        self.wn.bgcolor('lightblue')
        self.space= turtle.Turtle()
        self.space.shape('square')
        self.space.color('red')
        self.space.penup()

        
        self.banner = turtle.Turtle()
        self.banner.speed(0)
        self.banner.color('white')
        self.banner.penup()
        self.banner.ht()
        self.banner.goto(0,260)
        self.banner.write('SCORE')

    def arriba(self):
        self.space.setheading(90)

    def abajo(self):
        self.space.setheading(270)

    def derecha(self):
        self.space.setheading(0)

    def izquierda(self):
        self.space.setheading(180)

    def trigger(self):
        self.wn.listen()
        self.wn.onkey(self.arriba,'Up')
        self.wn.onkey(self.abajo,'Down')
        self.wn.onkey(self.izquierda,'Left')
        self.wn.onkey(self.derecha,'Right')
        while True:
            self.space.forward(self.speed)
            if self.space.xcor()>290 or self.space.xcor()<-290 or self.space.ycor()>290 or self.space.ycor()<-290:
                time.sleep(0)
                self.space.goto(0,0)
                self.space.direction='stop'


c=cursorcontrol()
c.trigger()