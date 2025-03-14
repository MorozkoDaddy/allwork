class Nik:
    def __init__(self):
        self.name = str("nikolai")
        self.years = 18
    def vvod(self):
        print("=============")
        self.name = input("Имя ")
        print("=============")
        self.name = str("nikolai")
        print("=============")
        print('Hello ' + self.name)
        print("=============")
niker = Nik()
niker.vvod()