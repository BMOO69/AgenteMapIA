
import heapq

from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile
from Model.Vertexx import Vertexx


def heuristic(node, goal):
    # Función heurística, en este caso, la distancia Manhattan
    return abs(node[1][0] - goal[1][0]) + abs(node[1][1] - goal[1][1])

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

# Grafo de ejemplo representado como un diccionario
"""
graph = {
    ("A", (0, 0)): [("B", (1, 0)), ("C", (0, 1))],
    ("B", (1, 0)): [("A", (0, 0)), ("D", (1, 1))],
    ("C", (0, 1)): [("A", (0, 0)), ("D", (1, 1))],
    ("D", (1, 1)): [("B", (1, 0)), ("C", (0, 1))]
}"""

start_node = Vertexx('e1', (13, 83))
goal_node = Vertexx('n9', (421, 344))

manage = ManagerFile
grafo = GrafoNoDirigido
#graph = manage.obGrafoSinText(GrafoNoDirigido)
graph = ManagerFile.obGrafoSinText(grafo)
#start_node = ("A", (0, 0))
#goal_node = ("D", (1, 1))



path = astar(graph, start_node, goal_node)

if path:
    print("Ruta encontrada:")
    for node in path:
        print(node)
else:
    print("No se encontró una ruta válida.")


if __name__ == "__main__":
    print(" gola adasdasd")


