import turtle
import time
class L_system:
    def __init__(self, axiom, rules):
        self.sentence=[axiom]
        self.rules = rules

    def iterate(self, numIterations):
        for i in range(numIterations):
            self.sentence = [self.rules.get(letter, letter) for letter in self.sentence] #try to find a matching replacemnt rule, else return the original
            self.sentence = flatten2d(self.sentence)

    def display(self, spacer = ""):
        print(spacer.join(self.sentence))


def flatten2d(list):
    return [element for sublist in list for element in sublist]

mySys = L_system(axiom = "A", rules = {"A":["B","-","A","-","B"],
                                       "B":["A","+","B","+","A"]})

#set up screen and turtle
s = turtle.Screen()
t = turtle.Turtle()
s.tracer(0, 0)


mySys.iterate(5)

for turnAngle in range(60,-1,-1):
    #rest the turtle
    t.goto(0,0)
    t.clear()
    t.setheading(90)
    
    #perform each draw action for a certain letter
    for letter in mySys.sentence:
        if letter in ("A","B"):
            t.fd(4)
        elif letter == "-":
            t.right(turnAngle)
        elif letter == "+":
            t.left(turnAngle)
    
    #update screen
    s.update()
    
turtle.done()