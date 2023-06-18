import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import defaultdict
from tkinter import simpledialog
# from customtkinter import CustomTkinter as ctk
import sys
sys.path.append('D:/TONIO/trabajos/IA/ia carmen/AgenteMapIA/')
from Model.Grafo import Grafo
from PIL import ImageTk, Image
from tkinter import *
from Model.Vertexx import Vertexx



biblioteca = Grafo() 
nodos = False
class ImageGraphBuilder:
    
    def __init__(self, image_path):
        self.image_path = image_path
        self.nodes = {}
        self.edges = []
        self.start_node = None
        self.end_node = None
        self.is_finished = False

    def on_image_click(self, event):
        # if self.is_finished:
        #     return

        x = event.x
        y = event.y
        nomb=self.create_node(x, y)
        biblioteca.addVertex(Vertexx(nomb, (x, y)))
        # print(biblioteca.grafoDiccionario)
        # if not self.start_node:
        #     self.start_node = self.create_node(x, y)
        # else:
        #     self.end_node = self.create_node(x, y)
        #     self.create_edge()

    def create_node(self, x, y):
        node_name = self.get_node_name()
        if node_name:
            self.nodes[node_name] = (x, y)
            self.draw_node(x, y, node_name)
            return node_name

    def get_node_name(self):
        node_name = simpledialog.askstring("Nombre del Nodo", "Ingrese el nombre del nodo:")
        return node_name

    def create_edge(self):
        edge_name = self.get_edge_name()
        if edge_name:
            self.edges.append((self.start_node, self.end_node, edge_name))
            self.draw_edge(self.start_node, self.end_node, edge_name)
            self.start_node = None
            self.end_node = None

    def get_edge_name(self):
        edge_name = simpledialog.askstring("Nombre de la Arista", "Ingrese el nombre de la arista:")
        return edge_name

    def draw_node(self, x, y, node_name):
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
        canvas.create_text(x + 10, y, text=node_name)

    def draw_edge(self, start_node, end_node, edge_name):
        start_x, start_y = self.nodes[start_node]
        end_x, end_y = self.nodes[end_node]
        canvas.create_line(start_x, start_y, end_x, end_y, fill="blue")
        canvas.create_text((start_x + end_x) / 2, (start_y + end_y) / 2, text=edge_name)

    def finish_graph(self):
        self.is_finished = True
        messagebox.showinfo("Finalizar", "La acción ha sido finalizada.")

    def boton1():
            print("precionado")
            ImageGraphBuilder(imagen).on_image_click

# Crear la ventana principal
root = Tk()

root.geometry("800x600")
from PIL import Image
# Cargar la imagen
image_path = "view/mapa.png"  # Reemplaza con la ruta de tu imagen
imagen = Image.open(image_path)
imagen = imagen.resize((400, 400))  # Ajusta el tamaño de la imagen según sea necesario
photo = ImageTk.PhotoImage(imagen)

# Crear el lienzo
canvas = Canvas(root, width=imagen.width, height=imagen.height)
canvas.create_image(0, 0, image=photo, anchor="nw")
canvas.bind("<Button-1>")
canvas.pack(side="right", padx=10, pady=10)

# Crear el menú y los botones
menu_frame = Frame(root)
menu_frame.pack()

button1 = Button(menu_frame, text="Seleccionar Nodos")
button = tk.Button(root, text="Presionar", command=boton1)
button1.pack()

button2 = Button(menu_frame, text="Botón 2")
button2.pack()

# Crear las áreas de texto y los rótulos
label1 = Label(root, text="Rótulo 1")
label1.pack()

text_area1 = Entry(root)
text_area1.pack()

label2 = Label(root, text="Rótulo 2")
label2.pack()

text_area2 = Entry(root)
text_area2.pack()

label3 = Label(root, text="Rótulo 3")
label3.pack()

text_area3 = Entry(root)
text_area3.pack()

label4 = Label(root, text="Rótulo 4")
label4.pack()

text_area4 = Entry(root)
text_area4.pack()

# Crear los botones inferiores
button3 = Button(root, text="Botón 3")
button3.pack()

button4 = Button(root, text="Botón 4")
button4.pack()
# Ejecutar el bucle principal del GUI
root.mainloop()
root = tk.Tk()


