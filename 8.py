a = int(input('Введите jnumber:'))
import math
class Number:
    def __init__(self, x):
        self.x = x

    def print(self):
        print('Вы ввели jnumber:', self.x)

calculator = Number(a)

calculator.print()
