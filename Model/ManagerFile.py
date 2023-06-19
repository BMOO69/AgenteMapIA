from io import open

from Model.Arist import Arist
from Model.Vertexx import Vertexx


class ManagerFile(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if ManagerFile.__instance is None:
            ManagerFile.__instance = object.__new__(cls)
        return ManagerFile.__instance

    def obtenerGrafo(self):
        fileedge = open("aristaGra.txt","r")
        listAr = fileedge.readlines()
        fileedge.close()
        return listAr

    def obtenerNodesMana(self,graph):
        var = graph.getNodeslist()
        return var
        #print("prueba funciona la obteccion de nodos")
    def obGrafoSinText(self,graph):
        #g = GrafoNoDirigido()
        g = graph()
        g.addVertex(Vertexx('e1', 13, 83))
        g.addVertex(Vertexx('e2', 13, 346))
        g.addVertex(Vertexx('e3', 13, 570))
        g.addVertex(Vertexx('e4', 305, 660))
        g.addVertex(Vertexx('e5', 790, 660))
        g.addVertex(Vertexx('e6', 1150, 660))
        g.addVertex(Vertexx('e7', 1207, 485))
        g.addVertex(Vertexx('e8', 1207, 286))
        g.addVertex(Vertexx('e9', 1207, 34))
        g.addVertex(Vertexx('e10',700, 13))
        #g.getVertex(Vertexx('e11', (390, 12)))
        g.addVertex(Vertexx('colegio1',210, 85))
        g.addVertex(Vertexx('hospital2', 214, 342))
        g.addVertex(Vertexx('mall3', 217, 457))
        g.addVertex(Vertexx('parque4', 430, 565))
        g.addVertex(Vertexx('nn5', 790, 565))
        g.addVertex(Vertexx('nn6', 988, 566))
        g.addVertex(Vertexx('nn7', 509, 81))
        g.addVertex(Vertexx('nn8', 600, 127))
        g.addVertex(Vertexx('nn9', 421, 344))
        g.addVertex(Vertexx('nn10', 574, 451))
        g.addVertex(Vertexx('nn11', 750, 43))
        g.addVertex(Vertexx('nn12', 741, 201))
        g.addVertex(Vertexx('nn13', 765, 286))
        g.addVertex(Vertexx('nn14', 790, 484))
        g.addVertex(Vertexx('nn15', 843, 94))
        g.addVertex(Vertexx('nn16', 979, 167))
        g.addVertex(Vertexx('nn17', 1069, 287))
        g.addVertex(Vertexx('nn18', 1115, 487))

        g.addArist(Arist(g.getVertex('e1'), g.getVertex('colegio1')))
        g.addArist(Arist(g.getVertex('colegio1'), g.getVertex('hospital2')))
        g.addArist(Arist(g.getVertex('e2'), g.getVertex('hospital2')))
        g.addArist(Arist(g.getVertex('e1'), g.getVertex('colegio1')))
        g.addArist(Arist(g.getVertex('e3'), g.getVertex('mall3')))
        g.addArist(Arist(g.getVertex('hospital2'), g.getVertex('mall3')))
        g.addArist(Arist(g.getVertex('e4'), g.getVertex('parque4')))
        g.addArist(Arist(g.getVertex('mall3'), g.getVertex('nn9')))
        g.addArist(Arist(g.getVertex('hospital2'), g.getVertex('nn9')))
        g.addArist(Arist(g.getVertex('colegio1'), g.getVertex('nn7')))
        #g.addArist(Arist(g.getVertex('n7'), g.getVertex('e11')))
        g.addArist(Arist(g.getVertex('nn7'), g.getVertex('nn8')))
        g.addArist(Arist(g.getVertex('nn9'), g.getVertex('nn8')))
        g.addArist(Arist(g.getVertex('parque4'), g.getVertex('nn10')))
        g.addArist(Arist(g.getVertex('nn9'), g.getVertex('nn10')))
        g.addArist(Arist(g.getVertex('e5'), g.getVertex('nn5')))
        g.addArist(Arist(g.getVertex('parque4'), g.getVertex('nn5')))
        g.addArist(Arist(g.getVertex('nn10'), g.getVertex('nn14')))
        g.addArist(Arist(g.getVertex('nn14'), g.getVertex('nn5')))
        g.addArist(Arist(g.getVertex('nn9'), g.getVertex('nn13')))
        g.addArist(Arist(g.getVertex('nn13'), g.getVertex('nn14')))
        g.addArist(Arist(g.getVertex('nn12'), g.getVertex('nn13')))
        g.addArist(Arist(g.getVertex('nn8'), g.getVertex('nn12')))
        g.addArist(Arist(g.getVertex('nn13'), g.getVertex('nn14')))
        g.addArist(Arist(g.getVertex('nn8'), g.getVertex('nn11')))
        g.addArist(Arist(g.getVertex('e10'), g.getVertex('nn11')))
        g.addArist(Arist(g.getVertex('nn11'), g.getVertex('nn15')))
        g.addArist(Arist(g.getVertex('nn12'), g.getVertex('nn15')))
        g.addArist(Arist(g.getVertex('nn15'), g.getVertex('nn16')))
        g.addArist(Arist(g.getVertex('e9'), g.getVertex('nn16')))
        g.addArist(Arist(g.getVertex('e8'), g.getVertex('nn17')))
        g.addArist(Arist(g.getVertex('nn16'), g.getVertex('nn17')))
        g.addArist(Arist(g.getVertex('nn14'), g.getVertex('nn17')))
        g.addArist(Arist(g.getVertex('nn14'), g.getVertex('nn18')))
        g.addArist(Arist(g.getVertex('nn5'), g.getVertex('nn6')))
        g.addArist(Arist(g.getVertex('nn6'), g.getVertex('nn18')))
        g.addArist(Arist(g.getVertex('e7'), g.getVertex('nn18')))
        g.addArist(Arist(g.getVertex('e6'), g.getVertex('nn6')))
        g.addArist(Arist(g.getVertex('mall3'), g.getVertex('parque4')))
        return g

# Todo El grafo dirigido tiene 24 aristas
# Todo el grafo no dirigido tiene 48 aristas
# arreglar el alritmos de bidireccion de grafo en el metodo grafo no dirijido




