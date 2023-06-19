from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile
from Model.Vertexx import Vertexx
from View.Algorithms import astar, buscar_nodo_en_grafoBFS

start_node = Vertexx('e1', 13, 83)
goal_node = Vertexx('e7', 1207, 485)

manage = ManagerFile()
gra = GrafoNoDirigido

graph = manage.obGrafoSinText(gra)

path2 = astar(graph, start_node, goal_node)
path =  buscar_nodo_en_grafoBFS(graph, start_node, goal_node)
if path:
    print("Ruta encontrada:")
    for node in path:
        print(node)
else:
    print("No se encontró una ruta válida.")

if __name__ == "__main__":
    print("holita")
    print(type(path))
    print(type(path2))

    print(type(path[0]))
    print(type(path2[0]))