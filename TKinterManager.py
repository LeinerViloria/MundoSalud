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
    window = getMainWindow()
    window.mainloop()