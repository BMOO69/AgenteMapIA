from Grafo import *
from View.Arist import Arist


class GrafoNoDirigido(Grafo):
    def addArist(self, arist):
        Grafo.addArist(self, arist)
        aristBack = Arist(arist.getVertexOrigin(), arist.getVertexDest())
        Grafo.addArist(self, aristBack)
