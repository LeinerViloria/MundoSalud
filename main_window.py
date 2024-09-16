import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview
import numpy as np
from sklearn.linear_model import LinearRegression
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

    # Añadir área para la predicción
    add_prediction_section(window, df)

def add_prediction_section(window: tk.Misc, df: pd.DataFrame) -> None:
    frame = tk.Frame(window)
    frame.grid(row=8, column=3, padx=10, pady=10)

    # Etiqueta para la entrada
    tk.Label(frame, text="Número de Pacientes:").grid(row=0, column=0, padx=5, pady=5)

    # Entrada para número de pacientes
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, padx=5, pady=5)

    # Botón para realizar la predicción
    predict_button = tk.Button(frame, text="Predecir Tiempo de Espera", command=lambda: predict_waiting_time(entry.get(), df))
    predict_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # Etiqueta para mostrar el resultado de la predicción
    global prediction_result_label
    prediction_result_label = tk.Label(frame, text="")
    prediction_result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def predict_waiting_time(patients: str, df: pd.DataFrame) -> None:
    try:
        num_patients = int(patients)
        
        # Preparar datos para el modelo
        X = df[['Pacientes Atendidos']].values
        y = df['Tiempo de Espera (min)'].values
        
        # Entrenar el modelo de regresión lineal
        model = LinearRegression()
        model.fit(X, y)
        
        # Predecir el tiempo de espera
        predicted_waiting_time = model.predict(np.array([[num_patients]]))[0]
        
        # Mostrar el resultado
        prediction_result_label.config(text=f"Tiempo de Espera Predicho: {predicted_waiting_time:.2f} minutos")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")