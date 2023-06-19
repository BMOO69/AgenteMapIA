import time
import tkinter as tk
from collections import deque
import customtkinter as ctk
from PIL import Image, ImageTk
#from PIL.Image import Image
from PIL.ImageTk import PhotoImage

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
        print(type(ini))
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
                #node_origin = n.getXY()
                #node_dest = nod.getXY()
                node_ori_x = n.getX()
                node_ori_y = n.getY()
                node_dest_x = nod.getX()
                node_dest_y = nod.getY()
                self.drawEdge(node_ori_x,node_ori_y, node_dest_x,node_dest_y, "#7DA0CA")

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
        imagen_cole = Image.open("imagenes/colegio.png")
        imagen_redi_cole = imagen_cole.resize((30,30))
        imagen_tk_cole = ImageTk.PhotoImage(imagen_redi_cole)

        imagen_park = Image.open("imagenes/parque.png")
        imagen_redi_park = imagen_park.resize((40, 40))
        imagen_tk_park = ImageTk.PhotoImage(imagen_redi_park)

        imagen_hosp = Image.open("imagenes/hospital.png")
        imagen_redi_hosp = imagen_hosp.resize((40, 40))
        imagen_tk_hosp = ImageTk.PhotoImage(imagen_redi_hosp)

        imagen_mall = Image.open("imagenes/mall.png")
        imagen_redi_mall = imagen_mall.resize((40, 40))
        imagen_tk_mall = ImageTk.PhotoImage(imagen_redi_mall)

        for nod in self.nodes:
            node = (nod.getX(),nod.getY())
            node_id = nod.getName()
            (x, y) = node
            var = "".join(filter(lambda char: not char.isdigit(), node_id))
            if var == "colegio": #colegios
                label = ctk.CTkLabel(self.app.img_frame, image=imagen_tk_cole,font=ctk.CTkFont(size=20, weight="bold") ,text=node_id, text_color="black")
                self.app.img_frame.create_window(x, y, window=label)

            elif var == "parque": #parques
                label = ctk.CTkLabel(self.app.img_frame, image=imagen_tk_park, font=ctk.CTkFont(size=20, weight="bold"),
                                     text=node_id, text_color="black")
                self.app.img_frame.create_window(x, y, window=label)

            elif var == "hospital": # hospitales
                label = ctk.CTkLabel(self.app.img_frame, image=imagen_tk_hosp, font=ctk.CTkFont(size=20, weight="bold"),
                                     text=node_id, text_color="black")
                self.app.img_frame.create_window(x, y, window=label)

            elif var == "mall": # mall
                label = ctk.CTkLabel(self.app.img_frame, image=imagen_tk_mall, font=ctk.CTkFont(size=20, weight="bold"),
                                     text=node_id, text_color="black")
                self.app.img_frame.create_window(x, y, window=label)
            else:
                self.app.img_frame.create_oval(x - 15, y - 15, x + 15, y + 15, fill="blue")
                self.app.img_frame.create_text(x, y, text=node_id)

    def draw_Nodes2(self):
        self.nodes
        for nod in self.nodes:
            node = nod.getXY()
            node_id = nod.getName()
            (x, y) = node

            self.app.img_frame.create_oval(x - 15, y - 15, x + 15, y + 15, fill="blue")
            self.app.img_frame.create_text(x, y, text=node_id)
