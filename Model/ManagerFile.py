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
        g.addVertex(Vertexx('e1', (13, 83)))
        g.addVertex(Vertexx('e2', (13, 346)))
        g.addVertex(Vertexx('e3', (13, 570)))
        g.addVertex(Vertexx('e4', (305, 660)))
        g.addVertex(Vertexx('e5', (790, 660)))
        g.addVertex(Vertexx('e6', (1150, 660)))
        g.addVertex(Vertexx('e7', (1207, 485)))
        g.addVertex(Vertexx('e8', (1207, 286)))
        g.addVertex(Vertexx('e9', (1207, 34)))
        g.addVertex(Vertexx('e10', (700, 13)))
        #g.getVertex(Vertexx('e11', (390, 12)))
        g.addVertex(Vertexx('n1', (210, 85)))
        g.addVertex(Vertexx('n2', (214, 342)))
        g.addVertex(Vertexx('n3', (217, 457)))
        g.addVertex(Vertexx('n4', (430, 565)))
        g.addVertex(Vertexx('n5', (790, 565)))
        g.addVertex(Vertexx('n6', (988, 566)))
        g.addVertex(Vertexx('n7', (509, 81)))
        g.addVertex(Vertexx('n8', (600, 127)))
        g.addVertex(Vertexx('n9', (421, 344)))
        g.addVertex(Vertexx('n10', (574, 451)))
        g.addVertex(Vertexx('n11', (750, 43)))
        g.addVertex(Vertexx('n12', (741, 201)))
        g.addVertex(Vertexx('n13', (765, 286)))
        g.addVertex(Vertexx('n14', (790, 484)))
        g.addVertex(Vertexx('n15', (843, 94)))
        g.addVertex(Vertexx('n16', (979, 167)))
        g.addVertex(Vertexx('n17', (1069, 287)))
        g.addVertex(Vertexx('n18', (1115, 487)))

        g.addArist(Arist(g.getVertex('e1'), g.getVertex('n1')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('e2'), g.getVertex('n2')))
        g.addArist(Arist(g.getVertex('e1'), g.getVertex('n1')))
        g.addArist(Arist(g.getVertex('e3'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n3')))
        g.addArist(Arist(g.getVertex('e4'), g.getVertex('n4')))
        g.addArist(Arist(g.getVertex('n3'), g.getVertex('n9')))
        g.addArist(Arist(g.getVertex('n2'), g.getVertex('n9')))
        g.addArist(Arist(g.getVertex('n1'), g.getVertex('n7')))
        #g.addArist(Arist(g.getVertex('n7'), g.getVertex('e11')))
        g.addArist(Arist(g.getVertex('n7'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n8')))
        g.addArist(Arist(g.getVertex('n4'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n10')))
        g.addArist(Arist(g.getVertex('e5'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n4'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n10'), g.getVertex('n14')))
        g.addArist(Arist(g.getVertex('n14'), g.getVertex('n5')))
        g.addArist(Arist(g.getVertex('n9'), g.getVertex('n13')))
        g.addArist(Arist(g.getVertex('n13'), g.getVertex('n14')))
        g.addArist(Arist(g.getVertex('n12'), g.getVertex('n13')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n12')))
        g.addArist(Arist(g.getVertex('n13'), g.getVertex('n14')))
        g.addArist(Arist(g.getVertex('n8'), g.getVertex('n11')))
        g.addArist(Arist(g.getVertex('e10'), g.getVertex('n11')))
        g.addArist(Arist(g.getVertex('n11'), g.getVertex('n15')))
        g.addArist(Arist(g.getVertex('n12'), g.getVertex('n15')))
        g.addArist(Arist(g.getVertex('n15'), g.getVertex('n16')))
        g.addArist(Arist(g.getVertex('e9'), g.getVertex('n16')))
        g.addArist(Arist(g.getVertex('e8'), g.getVertex('n17')))
        g.addArist(Arist(g.getVertex('n16'), g.getVertex('n17')))
        g.addArist(Arist(g.getVertex('n14'), g.getVertex('n17')))
        g.addArist(Arist(g.getVertex('n14'), g.getVertex('n18')))
        g.addArist(Arist(g.getVertex('n5'), g.getVertex('n6')))
        g.addArist(Arist(g.getVertex('n6'), g.getVertex('n18')))
        g.addArist(Arist(g.getVertex('e7'), g.getVertex('n18')))
        g.addArist(Arist(g.getVertex('e6'), g.getVertex('n6')))
        g.addArist(Arist(g.getVertex('n3'), g.getVertex('n4')))
        return g
"""
#Todo: este es el grafo anterior con valores incorrectos

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
"""
# Todo El grafo dirigido tiene 24 aristas
# Todo el grafo no dirigido tiene 48 aristas
# arreglar el alritmos de bidireccion de grafo en el metodo grafo no dirijido




