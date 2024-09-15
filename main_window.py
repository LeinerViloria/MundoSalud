import tkinter as tk
from tkinter.ttk import Treeview

import pandas as pd
import TKinter_Manager as Tk_Manager
import path_manager as pm

def runMainWindow():
    # VENTANA PRINCIPAL
    ventana_principal = tk.Tk()
    Tk_Manager.setCloseButton(ventana_principal)
    ventana_principal.configure(background="light blue")
    ventana_principal.attributes("-alpha", 1)
    ventana_principal.title("MUNDO-SALUD")
    ventana_principal.iconbitmap('img/medical.ico')
    ventana_principal.minsize(930, 600)

    # TITULO PRINCIPAL
    etiqueta_principal = tk.Label(ventana_principal, text="Elige un dataframe para usarlo como fuente para las predicciones")
    etiqueta_principal.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    xlsx_files = pm.getFiles()

    # FRAME QUE MUESTRA LOS EXCEL
    frame = tk.Frame(ventana_principal)
    frame.grid(row=8, column=1, padx=2)
    main_listbox = tk.Listbox(frame, height=10, width=50)
    main_listbox.grid(row=0, column=1)
    for file in xlsx_files:
        main_listbox.insert(tk.END, file)

    main_listbox.bind("<<ListboxSelect>>", lambda event: on_listbox_select(event, ventana_principal))

    ventana_principal.mainloop()

def on_listbox_select(event, window):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        file = event.widget.get(index)
        file_path = f"{pm.current_directory}/source/{file}"
        display_excel_data(window, file_path)

def display_excel_data(window: tk.Misc, file_path: str) -> None:
    frame = tk.Frame(window)
    frame.grid(row=8, column=2, padx=2)
    
    # Leer el archivo Excel
    df = pd.read_excel(file_path)
    
    # Crear el Treeview
    tree = Treeview(frame)
    tree.grid(row=2, column=0)
    
    # Configurar columnas
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=180)
    
    # Insertar filas
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))