class RealString:

    def __init__(self):
        self.apple = str("Я")
        self.apple1 = str("Б")
        self.apple2 = str("Л")
        self.apple3 = str("О")
        self.apple4 = str("К")
        self.apple5 = str("О")
        self.apple11 = str("A")
        self.apple22 = str("P") 
        self.apple33 = str("P")
        self.apple44 = str("L")
        self.apple55 = str("E")


    def methone(self):
            print(ord("a"))
            print(ord("p"))
            print(ord("p"))
            print(ord("l"))
            print(ord("e"))

    def methtwo(self):
            print(ord("я"))
            print(ord("б"))
            print(ord("л"))
            print(ord("о"))
            print(ord("к"))
            print(ord("о"))
            
rs = RealString()
rs.methone(10, 5) 
rs.methtwo(5, 10)