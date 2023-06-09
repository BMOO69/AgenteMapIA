from Model import Grafo
from Model.Arist import Arist


class GrafoNoDirigido(Grafo.Grafo):
    def addArist(self, arist):
        Grafo.Grafo.addArist(self, arist)
        aristBack = Arist(arist.getVertexOrigin(), arist.getVertexDest())
        Grafo.Grafo.addArist(self, aristBack)
