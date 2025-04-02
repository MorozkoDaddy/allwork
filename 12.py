import math

class Mathe:
    def __init__(self, x):
        self.x = x

    def res(self):
        y = math.sqrt(2*self.x+math.sin(abs(3*self.x))/3.56)
        print(y)
        
calculator = Mathe(5)

calculator.res()
