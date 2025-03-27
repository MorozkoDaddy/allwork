class week:

    def __init__(self, x):
        self.x = x
    
    def ckhet(self):
        self.x = self.x // 7

    def res(self):
        print('Недель полных прошло = ', self.x)

weeks = week(234)

weeks.ckhet()
weeks.res()
