class TriangleChecker:

    def __init__(self):
        self.x = 2
        self.y = 5
        self.z = 7
    
    def scet(self):
        if(type(self.x) != type(1) and (type(self.y) != type(1)) and type(self.y) != type(1)):
            {
                print("только числа введи черт")
            }
        elif((self.x <= 0) or (self.y <= 0) or (self.z <= 0)):
            {
                print("отрицал не идет")
            }
        elif(self.x + self.y >= self.z or self.y + self.z >= self.x or self.z + self.x >= self.y):
            print("Ура можно построить треугольник!! ТЫ молодец Санечка, я тобой горжусь, ты очень крутой, я твой фанат, Александр Дмитриевич")
        else:
            {
                print("треугольник не сделать")
            }
triangles = TriangleChecker()
triangles.scet()

