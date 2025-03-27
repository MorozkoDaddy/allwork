class cent:

    def __init__(self, x):
        self.x = x
    
    def centt(self):
        self.x = self.x // 100

    def res(self):
        print('Полных центнеров = ', self.x)

centner = cent(1998)

centner.centt()
centner.res()
