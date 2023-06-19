import heapq
import math

from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile
from Model.Vertexx import Vertexx


def heuristic(node, goal):
    # Función heurística, en este caso, la distancia Manhattan
    ni = node.getPX()
    nd = goal.posXY()
    x1, y1 = ni
    x2, y2 = nd

    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

    #return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(graph, start, goal):
    # Inicialización
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))
    g_scores = {start: 0}
    parents = {}

    while open_list:
        # Selección del nodo con menor f(n)
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
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
"""
class Objeto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Objeto) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return False

# Grafo de ejemplo representado como un diccionario
graph = {
    Objeto(0, 0): [Objeto(1, 0), Objeto(0, 1)],
    Objeto(1, 0): [Objeto(0, 0), Objeto(1, 1)],
    Objeto(0, 1): [Objeto(0, 0), Objeto(1, 1)],
    Objeto(1, 1): [Objeto(1, 0), Objeto(0, 1)]
}

start_node = Objeto(0, 0)
goal_node = Objeto(1, 1)
"""
inicio = Vertexx('e1', (13, 83))
final = Vertexx('n4', (430, 565))

manage = ManagerFile()
gra = manage.obGrafoSinText(GrafoNoDirigido)

path = astar(gra, inicio, final)

if path:
    print("Ruta encontrada:")
    for node in path:
        print(f"({node.x}, {node.y})")
else:
    print("No se encontró una ruta válida.")


if __name__ == "__main__":
    print("hola mundo")


print('hola')