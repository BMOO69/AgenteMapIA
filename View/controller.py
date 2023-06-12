import time
import tkinter as tk
from collections import deque

from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile
class Controller():
    def __init__(self, app):
        self.app = app
        self.manage = ManagerFile()
        self.grafo = GrafoNoDirigido
        self.grafo = self.manage.obGrafoSinText(self.grafo)
        self.nodes = self.manage.obtenerNodesMana(self.grafo)

        self.drawBackground()
        self.draw_Nodes()

        self.app.send_agent_button.configure(command=lambda: self.run_algorithm())

        self.app.mainloop()

    def run_algorithm(self):
        start = self.app.entry_start.get()
        goal = self.app.entry_destination.get()
        ini = self.grafo.getVertex(start)
        fin = self.grafo.getVertex(goal)
        path = self.buscar_nodo_en_grafo(self.grafo.grafoDiccionario, ini, fin)

        self.drawPath(path)
        for i in path:

            print(i)
        print(type(path))

    def buscar_nodo_en_grafo(self, grafo, nodo_inicio, nodo_objetivo):
        visitados = set()
        cola = deque([(nodo_inicio, [])])

        while cola:
            nodo, camino = cola.popleft()
            if nodo == nodo_objetivo:
                return camino + [nodo]

            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in grafo[nodo]:
                    cola.append((vecino, camino + [nodo]))

        return None

    def drawBackground(self):
        for n in self.nodes:
            valor = self.grafo.grafoDiccionario[n]
            for nod in valor:
                node_origin = n.getXY()
                node_dest = nod.getXY()
                self.drawEdge(node_origin[0],node_origin[1], node_dest[0],node_dest[1], "#7DA0CA")

    def drawPath(self, path):

        if path[0] != None:
            start = path[0]
            for fs in range(1,len(path)):
                node_origin = start.getXY()
                node_dest = path[fs].getXY()
                self.drawEdge(node_origin[0], node_origin[1], node_dest[0], node_dest[1], "red")
                start = path[fs]

        else:
            print("esta vacia")

    def drawEdge(self,x1,y1,x2,y2, color):
        self.app.img_frame.create_line(x1, y1, x2, y2, fill=color, width=3)

    def draw_Nodes(self):
        self.nodes
        pass
        for nod in self.nodes:
            node = nod.getXY()
            node_id = nod.getName()
            (x, y) = node
            self.app.img_frame.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
            self.app.img_frame.create_text(x, y, text=node_id)
