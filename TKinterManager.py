import tkinter as tk
from typing import Callable
from PIL import Image, ImageTk

def salir(window: tk.Misc) -> None:
    window.destroy()

def setCloseButton(window: tk.Misc):
    closeButton = getButton(window, "Salir", lambda: salir(window))
    closeButton.grid(row=2, column=1, padx=5, pady=5)

def setFullScreen(window: tk.Tk):
    # Obtener el tamaño de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Configurar el tamaño de la ventana para que ocupe toda la pantalla
    window.geometry(f"{screen_width}x{screen_height}+0+0")

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

def runMainWindow():
    ventana_principal = getMainWindow()
    ventana_principal.configure(background="light blue")
    ventana_principal.attributes("-alpha", 1)
    ventana_principal.title("MUNDO-SALUD")
    ventana_principal.iconbitmap('img/medical.ico')

    setFullScreen(ventana_principal)

    ventana_principal.mainloop()