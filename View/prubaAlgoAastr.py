import heapq

from Model.Vertexx import Vertexx
from Model.GrafoNoDirigido import *
from Model.ManagerFile import ManagerFile

def heuristic(node, goal):
    # Función heurística, en este caso, la distancia Manhattan
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(graph, start, goal):
    # Inicialización
    ini = start.getXY()
    fin = goal.getXY()
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, ini))
    g_scores = {ini: 0}
    parents = {}

    while open_list:
        # Selección del nodo con menor f(n)
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == fin:
            # Se ha encontrado el objetivo, reconstruir el camino
            path = []
            while current_node in parents:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start)
            path.reverse()
            return path

        closed_list.add(current_node)

        # Exploración de vecinos
        for neighbor in graph[current_node]:
            g_score = g_scores[current_node] + 1  # Costo unitario para cada vecino
            if neighbor not in g_scores or g_score < g_scores[neighbor]:
                # Actualización del costo y el padre
                g_scores[neighbor] = g_score
                f_score = g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_node

    # No se ha encontrado una ruta válida
    return None

# Ejemplo de uso

# Clase para representar los objetos en el grafo
class Objeto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Grafo de ejemplo representado como un diccionario

graph = {
    Objeto(0, 0): [Objeto(1, 0), Objeto(0, 1)],
    Objeto(1, 0): [Objeto(0, 0), Objeto(1, 1)],
    Objeto(0, 1): [Objeto(0, 0), Objeto(1, 1)],
    Objeto(1, 1): [Objeto(1, 0), Objeto(0, 1)]
}

#start_node = Objeto(0, 0)
#goal_node = Objeto(1, 1)

ini = Vertexx('e1', (13, 83))
des = Vertexx('n13', (765, 286))

gra = ManagerFile.obGrafoSinText(GrafoNoDirigido)

path = astar(gra, ini, des)

if path:
    print("Ruta encontrada:")
    for node in path:
        print(f"({node.x}, {node.y})")
else:
    print("No se encontró una ruta válida.")

if __name__ == "__main__":
    print("hola undo")
    print(gra)
