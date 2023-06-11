import tkinter as tk
from Model.ManagerFile import *
from controller.DataGraf import *
from controller.DataGraf import getVertexx

root  = tk.Tk()
canvas = tk.Canvas(root , width=1200, height=700)
canvas.pack()

#graDate = ManagerFile()
#g = graDate.obGrafoSinText(GrafoNoDirigido)
#print(g)
da = getVertexx()
#print(da)
print(pruebaaaa())
nodes = getNoode()

for i in nodes:
    print(i)

def drawNodes():
    global nodes
    for node in nodes:
        node_id, (x, y) = node
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red")
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

def drawEdge(x1,y1,x2,y2):
    canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

def getVertexx():
    edges = []
    for i in data.grafoDiccionario:
        for j in data.grafoDiccionario[i]:
            edges.append((i.getName(),j.getName()))

#root.mainloop()

#if __name__ == "__main__":
    #drawBackground(da)
   # drawNodes();


