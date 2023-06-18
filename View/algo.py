import heapq

def heuristic(node, goal):
    # Función heurística, en este caso, la distancia Manhattan
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

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
            g_score = g_scores[current_node] + graph[current_node][neighbor]
            if neighbor not in g_scores or g_score < g_scores[neighbor]:
                # Actualización del costo y el padre
                g_scores[neighbor] = g_score
                f_score = g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_node

    # No se ha encontrado una ruta válida
    return None

# Ejemplo de uso

# Grafo de ejemplo

if __name__ == "__main__":
    print("hola algo.py")

    graphs = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'C': 2, 'D': 1},
        'C': {'A': 10, 'B': 2, 'D': 6},
        'D': {'B': 1, 'C': 6}
    }

    start_node = 'A'
    goal_node = 'D'

    path = astar(graphs, start_node, goal_node)

    if path:
        print(f"Ruta encontrada: {path}")
    else:
        print("No se encontró una ruta válida.")
