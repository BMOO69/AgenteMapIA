import tkinter as tk

from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile
class Controller():
    def __init__(self, app):
        self.app = app
        #self.app.send_agent_button.configure(command=lambda: self.run_algorithm())
        self.app.send_agent_button.configure(command=lambda: self.draw_Nodes())
        self.grafo = ManagerFile()

        self.app.mainloop()

    def run_algorithm(self):
        g = self.grafo.obGrafoSinText(GrafoNoDirigido)
        print(g)

    def draw_Nodes(self):
        self.app.img_frame.create_oval(0,0,50,50,outline='black',width=3)
