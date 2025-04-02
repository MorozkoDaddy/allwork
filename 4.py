class Mathe:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print('',self.x,'\n', self.y, '\n', self.z)

calculator = Mathe(5,10,21)

calculator.print()
