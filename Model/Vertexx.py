class Vertexx:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.name, self.x, self.y))
    def __eq__(self, other):
<<<<<<< HEAD
        if isinstance(other, Vertexx):
            if other.getName() == self.name and self.posXY == other.posXY:
                return True
        else:
            return False
=======
        return isinstance(other, Vertexx)and self.name==other.name and self.x == other.x and self.y == other.y

>>>>>>> pruebaContro

    def __lt__(self, other):
        return False
    def getName(self):
        return self.name

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    def __str__(self) -> str:
        return self.name+" ("+str(self.x)+","+str(self.y)+")"
    def __repr__(self):
        return self.name

