class mesta:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def numbers(self):
        global vvod
        global res1 
        vvod = int(input('Введите номер места'))
        if vvod > self.x * self.y:
            print('Введены неправильные данные')
        elif vvod % self.y == 0:
            res1 = vvod // self.y
            print('Номер купе = ', res1)
        else:
            res1 = vvod // self.y + 1
            print('Номер купе', res1)

mestos = mesta(9,4)

mestos.numbers()
