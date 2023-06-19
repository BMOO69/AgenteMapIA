from tkinter import Tk, Label
from PIL import Image, ImageTk

# Crear una instancia de la ventana principal
ventana = Tk()

# Cargar la imagen utilizando PIL
imagen_pil = Image.open("imagenes/colegio.png")

# Convertir la imagen PIL a un objeto ImageTk compatible con Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_pil)

# Crear un widget de etiqueta (label)
etiqueta = Label(ventana, image=imagen_tk)

# Mostrar el widget de etiqueta
etiqueta.pack()

# Ejecutar el bucle principal
ventana.mainloop()
