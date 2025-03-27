import math

class mathe:

    def __init__(self, x):
        self.x = x
    
    def raschet(self):
        i = 0
        a = 0
        while i != 9:
            b = int(input('Введите число'))
            a = a + b  
            i = i + 1 
        return a
               
calculator = mathe(1)

print(calculator.raschet())
