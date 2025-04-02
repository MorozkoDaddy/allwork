x = int(input('Введите сторону : '))

import math

class Mathe:
    def __init__(self, x):
        self.x = x

    def res(self):
        y = 4*self.x
        print(y)
        
calculator = Mathe(5)

calculator.res()
