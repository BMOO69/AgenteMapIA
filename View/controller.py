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
        #self.app.send_agent_button.configure(command=lambda: self.run_algorithm())
        self.app.send_agent_button.configure(command=lambda: self.draw_Nodes())



        self.app.mainloop()

    def run_algorithm(self):
        g = self.manage.obGrafoSinText(GrafoNoDirigido)
        lis = ('e1',(30,90))

        print(g)

    def drawEdge(self,x1,y1,x2,y2):
        self.app.img_frame.create_line(x1, y1, x2, y2, fill="red", width=3)

    def drawPath(self):
        pass

    def draw_Nodes(self):

        print(self.nodes)
        self.app.img_frame.create_oval(0,0,50,50,outline='black',width=3)
