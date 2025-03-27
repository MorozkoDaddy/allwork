class meter:

    def __init__(self, x):
        self.x = x
    
    def metercalc(self):
        self.x = self.x // 100

    def result(self):
        print('Полных метров = ', self.x)

calculators = meter(2000)

calculators.metercalc()
calculators.result()
