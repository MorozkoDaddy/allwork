
// движеие авто вдоль дороги. Какая то лаба

class TCar:
    def __init__(self, road0, p0, v0 ):
        self.road = road0
        self.P = p0
        self.V = v0
        self.X = 0
        
    def move(self):
        self.X += self.V
        if self.X > self.road.length:
            self.X = 0

class TRoad:
    def __init__(self, length0, width0):
        if length0 > 0:
            self.length = 0
        else:
             self.length = 0
        if width0 > 0:
            self.width = width0
        else:
            self.width = 0

N = 3
cars = []
road = TRoad (10,10)
for i in range (N):
    cars.append (TCar(road, i+1, 2*(i+1)))
for k in range (100):
    for i in range (N):
        cars[i].move()
print ("После 100 шагов:")
for i in range(N):
    print (cars[i].X)
