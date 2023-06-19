import heapq
import math
from collections import deque


def heuristic(node, goal):

    return math.sqrt((goal.getX()-node.getX())**2+(goal.getY()-node.getY())**2)

def astar(graph, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))
    g_scores = {start: 0}
    parents = {}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in parents:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start)
            path.reverse()
            return path

        closed_list.add(current_node)

        for neighbor in graph.getNeighbors(current_node):
            g_score = g_scores[current_node] + 1
            if neighbor not in g_scores or g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                f_score = g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_node

    return None

def buscar_nodo_en_grafoBFS(grafo, nodo_inicio, nodo_objetivo):
    visitados = set()
    cola = deque([(nodo_inicio, [])])

    while cola:
        nodo, camino = cola.popleft()
        if nodo == nodo_objetivo:
            return camino + [nodo]

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.grafoDiccionario[nodo]:
                cola.append((vecino, camino + [nodo]))
    return None



