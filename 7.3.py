import math

class Number:

    def __init__(self, x):
        self.x = x
    
    def numbers(self):
        i = 0
        self.x = 0
        while i != 12:
            b = int(input('Введите число'))
            self.x = self.x + b  
            i = i + 1
        return self.x
               
calculator = Number(0)

print(calculator.numbers())
