class Vertexx:

    def __init__(self, name, posXY):
        self.name = name
        self.posXY = posXY


    def __hash__(self):
        return hash((self.name, self.posXY))
    def __eq__(self, other):
        if isinstance(other, Vertexx):
            if other.getName() == self.name and self.posXY == other.posXY:
                return True
        else:
            return False

    def __lt__(self, other):
        return False
    def getName(self):
        return self.name

    def getXY(self):
        return self.posXY

    def __str__(self) -> str:
        return self.name+str(self.posXY)


