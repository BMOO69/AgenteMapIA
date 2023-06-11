from io import open

from Model.Arist import Arist
from Model.GrafoNoDirigido import GrafoNoDirigido
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
        g.addVertex(Vertexx('e1', (30, 90)))
        g.addVertex(Vertexx('e2', (140, 30)))
        g.addVertex(Vertexx('e3', (220, 30)))
        g.addVertex(Vertexx('e4', (280, 60)))
        g.addVertex(Vertexx('e5', (310, 60)))
        g.addVertex(Vertexx('e6', (300, 200)))
        g.addVertex(Vertexx('e7', (220, 200)))
        g.addVertex(Vertexx('e8', (130, 200)))
        g.addVertex(Vertexx('e9', (30, 190)))
        g.addVertex(Vertexx('n1', (70, 90)))
        g.addVertex(Vertexx('n2', (120, 100)))
        g.addVertex(Vertexx('n3', (220, 60)))
        g.addVertex(Vertexx('n4', (280, 60)))
        g.addVertex(Vertexx('n5', (160, 110)))
        g.addVertex(Vertexx('n6', (220, 110)))
        g.addVertex(Vertexx('n7', (70, 160)))
        g.addVertex(Vertexx('n8', (150, 150)))
        g.addVertex(Vertexx('n9', (220, 150)))
        g.addVertex(Vertexx('n10', (280, 150)))
        g.addVertex(Vertexx('n11', (290, 100)))#numero de nodos o vertices es de 20 :(

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



""""   def obGrafoSinText(self):
        g = GrafoNoDirigido()
        for v in (
        'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9',
        'n10', 'n11'):
            g.addVertex(Vertexx(v))

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
        g.addArist(Arist(g.getVertex('n7'), g.getVertex('n2')))  # el grafo dirigido tiene 24 aristas
        return g  # el grafo no dirigido tiene 48 aristas
        # arreglar el alritmos de bidireccion de grafo en el metodo grafo no dirijido
"""



