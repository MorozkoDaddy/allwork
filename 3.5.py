class rezak:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def rezat(self):
        global res1 
        res1 = self.x // self.z

    def res(self):
        print('можно отрубить = ', res1)

calculator = rezak(540, 130, 130)

calculator.rezat()
calculator.res()
