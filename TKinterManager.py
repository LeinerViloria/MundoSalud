import tkinter as tk
from typing import Callable

def salir(window: tk.Misc) -> None:
    window.destroy()

def setCloseButton(window: tk.Misc):
    closeButton = getButton(window, "Salir", lambda: salir(window))
    closeButton.grid(row=2, column=1, padx=5, pady=5)

def getButton(window: tk.Misc, text: str, onClick: Callable[[], None]) -> tk.Button:
    boton = tk.Button(window, text=text, command=onClick)
    return boton

def getMainWindow() -> tk.Tk:
    mainWindow = tk.Tk()
    setCloseButton(mainWindow)
    return mainWindow

def runMainWindow():
    ventana_principal = getMainWindow()
    ventana_principal.configure(background="blue")
    ventana_principal.attributes("-alpha", 0.7)
    ventana_principal.title("MUNDO-SALUD")
    ventana_principal.minsize(1200, 800)

    ventana_principal.mainloop()