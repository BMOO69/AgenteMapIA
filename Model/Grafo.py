from Vertexx import *


class Grafo():
    def __init__(self):
        self.grafoDiccionario = {}

    def addVertex(self, vertexx):
        if vertexx in self.grafoDiccionario:
            return "ya existe ese grafo"

        assert isinstance(vertexx, Vertexx)
        self.grafoDiccionario[vertexx] = []

    def addArist(self, aristt):
        origen = aristt.getVertexOrigin()
        destino = aristt.getVertexDest()

        if origen not in self.grafoDiccionario:
            raise ValueError(f"Vertice {origen.getName()} no esta en el grafo")
        if destino not in self.grafoDiccionario:
            raise ValueError(f"Vertice {destino.getname()} no esta en grafo")

        self.grafoDiccionario[origen].append(destino)


    def vertexInGrafo(self, vertex):
        return vertex in self.grafoDiccionario


    def getVertex(self, nameVertex):
        for i in self.grafoDiccionario:
            if nameVertex == i.getName():
                return i
        print(f"Vertice {nameVertex} no existe en el grafo")


    def getNeighbors(self, vertex):
        return self.grafoDiccionario[vertex]


    def __str__(self) -> str:
        allVertex = ""

        for i in self.grafoDiccionario:  # todos los origenes o llaves
            for j in self.grafoDiccionario[i]:
                allVertex += i.getName() + "---> " + j.getName() + "\n"  # a donde puedes ir de este nodo
        return allVertex
