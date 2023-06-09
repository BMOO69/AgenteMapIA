from Grafo import *
from GrafoNoDirigido import *
from Model.Arist import *


def buildGrafo(graph):
    g = graph()

    for v in ('e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11'):
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
    return g                                                 # el grafo no dirigido tiene 48 aristas
    #arreglar el alritmos de bidireccion de grafo en el metodo grafo no dirijido

g1 = buildGrafo(GrafoNoDirigido)
print(g1)
