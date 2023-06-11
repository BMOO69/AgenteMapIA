class Vertexx:

    def __init__(self, name, posX, posY):
        self.name = name
        self.posX = posX
        self.posY = posY


    def __hash__(self):
        return hash((self.name, self.posX, self.posY))
    def __eq__(self, other):
        if isinstance(other, Vertexx):
            if other.getName() == self.name:
                return True
        else:
            return False

    def getName(self):
        return self.name

    def getY(self):
        return self.posY

    def getX(self):
        return self.posX

    def __str__(self) -> str:
        return self.name


