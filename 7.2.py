import math

class mathe:

    def __init__(self, x):
        self.x = x
    
    def res(self):
        i = 0
        self.x = 0
        while i != 10:
            b = float(input('Введите число'))
            if b % 1 != 0:
                self.x = self.x + b
            else:
                self.x = self.x
            i = i + 1 
        return self.x
               
calculator = mathe(0)

print(calculator.res())
