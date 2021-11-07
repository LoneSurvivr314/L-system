import turtle
import time
class L_system:
    def __init__(self, axiom, rules):
        self.sentence=[axiom]
        self.rules = rules

    def iterate(self, numIterations):
        for i in range(numIterations):
            self.sentence = [self.rules.get(word, word) for word in self.sentence] #try to find a matching replacemnt rule, else return the original
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



for iteration in range(1,10):
    #rest the turtle
    t.goto(-256,-256)
    t.clear()
    t.left(60)

    mySys.iterate(1)

    #perform each draw action for a certain letter
    for letter in mySys.sentence:
        if letter in ("A","B"):
            t.fd(512/2**iteration)
        elif letter == "-":
            t.right(60)
        elif letter == "+":
            t.left(60)
    
    #update screen
    s.update()
    time.sleep(1)
    
turtle.done()