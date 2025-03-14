class Tsoda:
    def __init__(self, pipka0):
        self.pipka = pipka0

    def show_my_drink(self, kolvo):
        self.kolvo0 = kolvo
        match kolvo:
            case "vodka":
                print("vodka")
            case "pivo":
                print("pivo")
            case "samagon":
                print("samagonka")