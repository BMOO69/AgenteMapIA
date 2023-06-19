from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile

manage = ManagerFile()
grafo = GrafoNoDirigido
#graph = manage.obGrafoSinText(GrafoNoDirigido)
graph = manage.obGrafoSinText(grafo)

if __name__ == "__main__":
    print(graph)