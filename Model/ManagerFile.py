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
        g.addVertex(Vertexx('e1', (10, 228)))
        g.addVertex(Vertexx('e2', (460, 10)))
        g.addVertex(Vertexx('e3', (828, 10)))
        g.addVertex(Vertexx('e4', (1100, 10)))
        g.addVertex(Vertexx('e5', (1200, 76)))
        g.addVertex(Vertexx('e6', (1200, 650)))
        g.addVertex(Vertexx('e7', (828, 650)))
        g.addVertex(Vertexx('e8', (368, 650)))
        g.addVertex(Vertexx('e9', (10, 570)))
        g.addVertex(Vertexx('n1', (184, 228)))
        g.addVertex(Vertexx('n2', (368, 228)))
        g.addVertex(Vertexx('n3', (828, 76)))
        g.addVertex(Vertexx('n4', (1100, 76)))
        g.addVertex(Vertexx('n5', (552, 226)))
        g.addVertex(Vertexx('n6', (828, 226)))
        g.addVertex(Vertexx('n7', (230, 418)))
        g.addVertex(Vertexx('n8', (506, 494)))
        g.addVertex(Vertexx('n9', (828, 494)))
        g.addVertex(Vertexx('n10', (1000, 418)))
        g.addVertex(Vertexx('n11', (1140, 226)))# Todo: numero de nodos o vertices es de 20 :(

        g.addArist(Arist(g.getVertex('e1'), g.getVertex('n1')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n7')))
        g.addArist(Arist(g.getVertex('e2'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('e9'), g.getVertex('n7')))
        g.addArist(Arist(g.getVertex('n7'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('e8'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n5'), g.getVertex('n6')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('e3'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('n3'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('e4'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('n4'), g.getVertex('e5')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('n11'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n9')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('e7')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('n10'), g.getVertex('e6')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n11')))
        g.addArist(Arist(g.getVertex('n7'), g.getVertex('n2')))
        return g
# Todo El grafo dirigido tiene 24 aristas
# Todo el grafo no dirigido tiene 48 aristas
# arreglar el alritmos de bidireccion de grafo en el metodo grafo no dirijido




