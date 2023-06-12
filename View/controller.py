import tkinter as tk

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

        #self.app.send_agent_button.configure(command=lambda: self.run_algorithm())
        self.app.send_agent_button.configure(command=lambda: self.draw_Nodes())



        self.app.mainloop()

    def run_algorithm(self):
        g = self.manage.obGrafoSinText(GrafoNoDirigido)
        lis = ('e1',(30,90))

        print(g)

    def drawBackground(self):
        for n in self.nodes:
            valor = self.grafo.grafoDiccionario[n]
            for nod in valor:
                node_origin = n.getXY()
                node_dest = nod.getXY()
                self.drawEdge(node_origin[0],node_origin[1], node_dest[0],node_dest[1])


    def drawEdge(self,x1,y1,x2,y2):
        self.app.img_frame.create_line(x1, y1, x2, y2, fill="#7DA0CA", width=3)

    def drawPath(self):
        pass

    def draw_Nodes(self):
        self.nodes
        pass
        for nod in self.nodes:
            node = nod.getXY()
            node_id = nod.getName()
            (x, y) = node
            self.app.img_frame.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
            self.app.img_frame.create_text(x, y, text=node_id)
