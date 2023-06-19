import heapq
import math

from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile
from Model.Vertexx import Vertexx




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


start_node = Vertexx('e1', 13, 83)
goal_node = Vertexx('e7', 1207, 485)

manage = ManagerFile()
gra = GrafoNoDirigido

graph = manage.obGrafoSinText(gra)

path = astar(graph, start_node, goal_node)

if path:
    print("Ruta encontrada:")
    for node in path:
        print(node)
else:
    print("No se encontró una ruta válida.")

if __name__ == "__main__":
    print("holita")
    print(type(path))
    print(type(path[0]))
    print(path)