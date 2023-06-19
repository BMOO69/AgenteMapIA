def bidirectional_search(graph, start, goal):
    # Inicialización
    open_list_start = [start]
    open_list_goal = [goal]
    closed_list_start = set()
    closed_list_goal = set()
    parents_start = {start: None}
    parents_goal = {goal: None}

    while open_list_start and open_list_goal:
        # Expandir desde el nodo de inicio
        current_node_start = open_list_start.pop(0)

        if current_node_start in closed_list_goal:
            # Se ha encontrado una intersección, reconstruir el camino
            path = []
            while current_node_start is not None:
                path.append(current_node_start)
                current_node_start = parents_start[current_node_start]
            path.reverse()

            current_node_goal = closed_list_goal.intersection(path).pop()
            while current_node_goal is not None:
                path.append(current_node_goal)
                current_node_goal = parents_goal[current_node_goal]

            return path

        closed_list_start.add(current_node_start)

        # Explorar vecinos desde el nodo de inicio
        for neighbor in graph[current_node_start]:
            if neighbor not in closed_list_start:
                open_list_start.append(neighbor)
                parents_start[neighbor] = current_node_start

        # Expandir desde el nodo objetivo
        current_node_goal = open_list_goal.pop(0)

        if current_node_goal in closed_list_start:
            # Se ha encontrado una intersección, reconstruir el camino
            path = []
            while current_node_goal is not None:
                path.append(current_node_goal)
                current_node_goal = parents_goal[current_node_goal]
            path.reverse()

            current_node_start = closed_list_start.intersection(path).pop()
            while current_node_start is not None:
                path.append(current_node_start)
                current_node_start = parents_start[current_node_start]

            return path

        closed_list_goal.add(current_node_goal)

        # Explorar vecinos desde el nodo objetivo
        for neighbor in graph[current_node_goal]:
            if neighbor not in closed_list_goal:
                open_list_goal.append(neighbor)
                parents_goal[neighbor] = current_node_goal

    # No se ha encontrado un camino
    return None
# Definición de la clase Objeto
class Objeto:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name

# Creación del grafo
grafo = {
    Objeto("A", 0, 0): [Objeto("B", 1, 0), Objeto("C", 0, 1)],
    Objeto("B", 1, 0): [Objeto("A", 0, 0), Objeto("D", 2, 0)],
    Objeto("C", 0, 1): [Objeto("A", 0, 0), Objeto("E", 0, 2)],
    Objeto("D", 2, 0): [Objeto("B", 1, 0), Objeto("F", 3, 0)],
    Objeto("E", 0, 2): [Objeto("C", 0, 1), Objeto("G", 0, 3)],
    Objeto("F", 3, 0): [Objeto("D", 2, 0), Objeto("H", 4, 0)],
    Objeto("G", 0, 3): [Objeto("E", 0, 2)],
    Objeto("H", 4, 0): [Objeto("F", 3, 0)]
}

start_node = Objeto("A", 0, 0)
goal_node = Objeto("H", 4, 0)

path = bidirectional_search(grafo, start_node, goal_node)
if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino válido.")

if __name__ == "__main__":
    print("holita 2")