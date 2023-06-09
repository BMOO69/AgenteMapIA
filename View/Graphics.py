import time
import tkinter as tk



root = tk.Tk()
canvas = tk.Canvas(root, width=1500, height=1000)
canvas.pack()

nodes = [("A", (100, 100)), ("B", (200, 200)), ("C", (300, 100)), ("D", (400, 200)), ("E", (500, 100)),
         ("F", (600, 200)), ("G", (700, 100)), ("H", (800, 200)), ("I", (900, 100)), ("J", (1000, 200))]

def drawNodes():
    global nodes
    for node in nodes:
        node_id, (x, y) = node
        canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")
        canvas.create_text(x, y, text=node_id)
def drawBackground(edges):

    global root, canvas, nodes
    # Dibujar los nodos


    # Dibujar las aristas
    for edge in edges:
        id_origin, id_dest = edge
        node_origin = next(node for node in nodes if node[0] == id_origin)
        node_dest = next(node for node in nodes if node[0] == id_dest)
        x1, y1 = node_origin[1]
        x2, y2 = node_dest[1]
        canvas.create_line(x1, y1, x2, y2, width=3)

def drawEdge(x1,y1,x2,y2):
    canvas.create_line(x1, y1, x2, y2, fill="red", width=3)


def drawPath(path):
    global root, nodes
    for edge in path:
        id_origin, id_dest = edge
        node_origin = next(node for node in nodes if node[0] == id_origin)
        node_dest = next(node for node in nodes if node[0] == id_dest)
        x1, y1 = node_origin[1]
        x2, y2 = node_dest[1]
        root.after(2000, drawEdge, x1, y1, x2, y2)
    root.mainloop()



if __name__ == '__main__':
    #global nodes
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"),
             ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("J", "A"),
             ("B", "D"), ("D", "F"), ("F", "H"), ("H", "J"), ("J", "B")]
    drawBackground(edges)
    drawNodes()
    path = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")]
    drawPath(path)
    #drawPath()