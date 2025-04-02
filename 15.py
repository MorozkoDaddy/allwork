x = int(input('Введите радиус окружности'))

import math

class Mathe:
    def __init__(self, x):
        self.x = x

    def res(self):
        y = 2*self.x
        print(y)
        
calculator = Mathe(5)

calculator.res()
