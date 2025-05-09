import turtle

class TurtleForNoobs:
 def estrella(self):
    est=turtle.Turtle()
    est.right(75)
    est.forward(100)
    for i in range(4):
        est.right(144)
        est.forward(100)
    turtle.done()
    
t = TurtleForNoobs()
t.estrella()