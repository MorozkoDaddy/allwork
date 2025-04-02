import math
class Mathe:
    def __init__(self, x):
        self.x = x

    def res(self):
        y = 3 * self.x**2 + 5*self.x - 21
        print(y)
        
calculator = Mathe(5)

calculator.res()
