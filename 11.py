import math
class Mathe:
    def __init__(self, x):
        self.x = x

    def res(self):
        y = (self.x**2 + 10)/(math.sqrt(self.x**2 + 1))
        print(y)
        
calculator = Mathe(5)

calculator.res()
