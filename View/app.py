import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image


from View.controller import Controller

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("green")
class AppWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("1200x580")
        self.resizable(False,False)
        self.update_idletasks()

        self.main_frame = ctk.CTkFrame(self,width=1200,height=650)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1,weight=3)

        self.options_frame = ctk.CTkFrame(self.main_frame, width=1200,height=650)
        self.options_frame.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10, ipady=10, padx=(0, 10), pady=(0,10))
        self.options_frame.columnconfigure(0,weight=1)
        self.ima = Image.open("imagenes/mapa.png")
        self.nuevaima = self.ima.resize((1200,650))

        self.gf = ImageTk.PhotoImage(self.nuevaima)
        #imagen_redimensionada = self.gf.resize((1200, 650))
        self.img_frame = ctk.CTkCanvas(self.main_frame, width=1200, height=650, bg="#0E6063")
        self.img_frame.grid(row=0, column=1, sticky=tk.NSEW, ipadx=10, ipady=10, padx=(0,10))
        self.img_frame.create_image(10, 10, image=self.gf, anchor=tk.NW)

        #canvas.bind("<Button-1>", obtener_coordenadas)
        """
        self.map_label = ctk.CTkLabel(self.img_frame, font=ctk.CTkFont(size=20, weight="bold"))
         
        self.map_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
aqui estarara el mapa"""
        self.label = ctk.CTkLabel(self.options_frame, text="AGENTES IA")
        self.label.grid(row=0, column=0, sticky=tk.NSEW)

        self.label_start = ctk.CTkLabel(self.options_frame, text="Inicio")
        self.label_start.grid(row=1, column=0, sticky=tk.NSEW)

        self.entry_start = ctk.CTkEntry(self.options_frame, placeholder_text="ingrese el inicio")
        self.entry_start.grid(row=2, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.label_destination = ctk.CTkLabel(self.options_frame, text="Destino")
        self.label_destination.grid(row=3, column=0, sticky=tk.NSEW)

        self.entry_destination = ctk.CTkEntry(self.options_frame, placeholder_text="ingrese el destino")
        self.entry_destination.grid(row=4, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.send_agent_button = ctk.CTkButton(self.options_frame, text="Enviar",command=lambda: self.buscar_ruta())
        self.send_agent_button.grid(row=5, column=0, sticky=tk.NSEW)

        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def clean_roads(self):
        pass

    def paint_graph(self):
        pass


    def clear_graph(self):
        pass

    def buscar_ruta(self):
        pass
app = AppWindow()
ctr = Controller(app)