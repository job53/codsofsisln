import turtle

class TurtleForNoobs:

    def test(self):
        skk = turtle.Turtle()
        for i in range(4):
            skk.forward(50)
            skk.right(90)
        turtle.done()

t = TurtleForNoobs()
t.test()