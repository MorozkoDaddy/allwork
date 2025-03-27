class apple:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def apples(self):
        global res1 
        global res2
        res1 = self.x // self.y
        res2 = self.x % self.y

    def res(self):
        print('Всем досталась по ', res1,'яблок','остаток яблок = ', res2)

howmuch = apples(8,4)

howmuch.apples()
howmuch.res()
