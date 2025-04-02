import math

class Da:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(f"{self.x:.2}")

calculator = Da(math.e)

calculator.print()
