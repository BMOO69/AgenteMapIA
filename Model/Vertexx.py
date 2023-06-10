class Vertexx:

    def __init__(self, name, px, py):
        self.name = name
        self.posX = px
        self.posY = py

    
    def getName(self):
        return self.name

    def getY(self):
        return self.posY

    def getX(self):
        return self.posX

    def __str__(self) -> str:
        return self.name


