import turtle

class TurtleForNoobs:

    def circulo(self,radio):
        t = turtle.Turtle()
        t.circle(radio)
        t.done()
    
    def ks(self,length,d):
        if d==0:
            turtle.forward(length)
        else:
            length = length/3
            d=d-1
            self.ks(length,d)
            turtle.right(60)
            self.ks(length,d) 
            turtle.left(120)
            self.ks(length,d)
            turtle.right(60)
            self.ks(length,d)
            


    def copoDeNieve(self):
        turtle.reset()
        turtle.ht()
        for i in range(3):
            self.ks(200,3)
            turtle.left(120)
        turtle.update()
        turtle.done()
    
    

t = TurtleForNoobs()
t.copoDeNieve()