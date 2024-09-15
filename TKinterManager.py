import tkinter as tk
from typing import Callable
from PIL import Image, ImageTk

def salir(window: tk.Misc) -> None:
    window.destroy()

def setCloseButton(window: tk.Misc):
    closeButton = getButton(window, "Salir", lambda: salir(window))
    closeButton.grid(row=2, column=1, padx=0, pady=5)

def getButton(window: tk.Misc, text: str, onClick: Callable[[], None], icon_path: str = None) -> tk.Button:
    # Crear el botón
    boton = tk.Button(window, text=text, command=onClick, font=("Arial", 12))
    
    # Configurar el icono si se proporciona
    if icon_path:
        icon = Image.open(icon_path)
        icon = icon.resize((20, 20), Image.ANTIALIAS)
        icon_image = ImageTk.PhotoImage(icon)
        boton.config(image=icon_image, compound=tk.LEFT)
        boton.image = icon_image  # Necesario para mantener la referencia a la imagen
    
    # Establecer el color de fondo y el color del texto
    boton.config(bg="#4169E1", fg="#D3D3D3")
    
    # Establecer el estilo del borde y el padding
    boton.config(relief="raised", borderwidth=1, padx=10, pady=5)

     # Funciones para manejar el efecto de hover
    def on_enter(event):
        boton.config(bg="#315BA1")  # Color más oscuro al pasar el cursor

    def on_leave(event):
        boton.config(bg="#4169E1")  # Restaurar el color original

    # Asociar los eventos de hover al botón
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def getMainWindow() -> tk.Tk:
    mainWindow = tk.Tk()
    setCloseButton(mainWindow)
    return mainWindow

def getFrame(window: tk.Misc, row: int, column: int) -> tk.Frame:
    frame = tk.Frame(window)
    frame.grid(row=row, column=column, padx=2)
    return frame

def getListBox(window: tk.Misc, frame_row: int, frame_column: int) -> tk.Listbox:
    frame = getFrame(window, frame_row, frame_column)
    listbox = tk.Listbox(frame, height=10, width=50)
    listbox.grid(row=0, column=1)
    return listbox