import tkinter as tk
from typing import Callable

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

def getButton(window: tk.Misc, text: str, onClick: Callable[[], None]) -> tk.Button:
    boton = tk.Button(window, text=text, command=onClick)
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