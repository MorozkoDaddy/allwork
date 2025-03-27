import math

class bignum:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def rasschet(self):
        res1 = self.y * 0.3048
        res2 = self.x
        a = 0
        if res1 > res2:
            a = res1
        elif res1 == res2:
            a = 'Числа равны'
        else:
            a = res2
        return a
        
         
calculator = bignum(4,5)
print('Наибольшее число = ',)

print(calculator.rasschet())
