import math

class Mathe:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def res(self):
        y = math.sqrt((self.z + self.x)**2 - self.x**2)
        print(y)
        
calculator = Mathe(6350, 200)

calculator.res()
