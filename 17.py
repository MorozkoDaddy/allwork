import math

class Mathe:
    def __init__(self, x):
        self.x = x
    def res(self):
        y = 2*math.pi*self.x
        z = math.pi*self.x**2
        print('длина окружности = ', y, 'площадь круга = ', z)
        
calculator = Mathe(5)

calculator.res()
