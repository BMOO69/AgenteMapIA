from GrafoNoDirigido import *


def buildGrafo(graph):
    g = graph()

    for v in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'):
        g.addVertex(Vertexx(v))
    g.addArist(Arist(g.getVertex('s'), g.getVertex('a')))
    return g


g1 = buildGrafo(Grafo)
