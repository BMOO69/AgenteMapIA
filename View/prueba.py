from Model.ManagerFile import *
from Model.GrafoNoDirigido import *
from Model.Vertexx import *

manage = ManagerFile()
grafo = manage.obGrafoSinText(GrafoNoDirigido)
nodos = manage.obtenerNodesMana(grafo)
# print(nodos)
lis = ('e1', (30, 90))
ve = Vertexx('e1', 30, 90)
Vertexx('e1', 30, 90)
# print(grafo.getVertex(Vertexx('e1', 30, 90)))

if __name__ == "__main__":
    print("funciona?:")

    print(grafo.getVertex(ve))