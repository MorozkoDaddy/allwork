import math

class Mathe:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(f"{self.x:.4}")

calculator = Mathe(math.pi)

calculator.print()
