import math

class Mathe:
    def __init__(self, x):
        self.x = x

    def res(self):
        y = math.sin((3.2 + math.sqrt(1 + self.x)/abs(5*self.x)))
        print(y)
        
calculator = Mathe(5)

calculator.res()
