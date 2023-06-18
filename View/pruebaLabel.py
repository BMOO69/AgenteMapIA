import customtkinter as ctk
import tkinter as tk

from PIL import ImageTk, Image

root = ctk.CTk()

# Crear canvas
canvas = ctk.CTkCanvas(root, width=400, height=300)
canvas.pack()

# Agregar label al canvas
label = ctk.CTkLabel(canvas, text="¡Hola!",fg_color="red")
ima = Image.open("imagenes/mapa.png")
nuevaima = ima.resize((1200,650))

gf = ImageTk.PhotoImage(nuevaima)
#label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
canvas.create_window(20, 20, window=label)

# Ejecutar el bucle principal
root.mainloop()


if __name__ == "__main__":
    print("hola mundo")