import math

class zone:

    def __init__(self, x):
        self.x = x
    
    def raschet(self):
        if self.x > 4:
            return 'Точка попадает в II зону'
        elif self.x == 4:
            return 'Введите другое число'
        else:
            return 'Точка попадает в I зону'
         
calculator = zone(4)

print(calculator.raschet())
