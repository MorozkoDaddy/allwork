import math
class Mathe:
    def __init__(self, x):
        self.x = x

    def res(self):
        y = 17 * self.x**2 - 6*self.x + 13
        print(y)
        
calculator = Mathe(5)

calculator.res()
