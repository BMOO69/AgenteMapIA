from Model.Arist import Arist
from Model.Grafo import Grafo


class GrafoNoDirigido(Grafo):
    def addArist(self, arist):
        Grafo.addArist(self, arist)
        aristBack = Arist(arist.getVertexOrigin(), arist.getVertexDest())
        Grafo.addArist(self, aristBack)
