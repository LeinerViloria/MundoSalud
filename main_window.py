import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
import TKinter_Manager as Tk_Manager
import path_manager as pm
from sklearn.metrics import mean_squared_error

day_column = 'Dia'
patients_treated_label = 'Pacientes atendidos'
waiting_time_label = 'Tiempo de espera (min)'
global_tree = None

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
    global global_tree

    if global_tree is not None:
        global_tree.destroy()

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

    global_tree = tree

    # Añadir área para la predicción
    add_prediction_section(window, df)

def add_prediction_section(window: tk.Misc, df: pd.DataFrame) -> None:
    frame = tk.Frame(window)
    frame.grid(row=12, column=1, padx=1, pady=5)

    # Etiqueta para la entrada
    tk.Label(frame, text="Número de Pacientes:").grid(row=0, column=0, padx=5, pady=5)

    # Entrada para número de pacientes
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, padx=5, pady=5)

    # Botón para realizar la predicción
    predict_button = tk.Button(frame, text="Predecir Tiempo de Espera", command=lambda: predict_waiting_time(entry.get(), df))
    predict_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    predict_button2 = tk.Button(frame, text="Predecir probabilidad de recomendación", command=lambda: predict_probability_of_recommendation(entry.get(), df))
    predict_button2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Etiqueta para mostrar el resultado de la predicción
    global prediction_result_label
    prediction_result_label = tk.Label(frame, text="")
    prediction_result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    ###

    satisfaction_frame = tk.Frame(window)
    satisfaction_frame.grid(row=12, column=2, padx=1, pady=5)

    # Etiqueta para la entrada
    tk.Label(satisfaction_frame, text="Tiempo de espera:").grid(row=0, column=0, padx=5, pady=5)

    # Entrada para número de pacientes
    entry1 = tk.Entry(satisfaction_frame)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    # Etiqueta para la entrada
    tk.Label(satisfaction_frame, text="Duracion de la consulta (min):").grid(row=1, column=0, padx=5, pady=5)

    # Entrada para número de pacientes
    entry2 = tk.Entry(satisfaction_frame)
    entry2.grid(row=1, column=1, padx=5, pady=5)

    # Etiqueta para la entrada
    tk.Label(satisfaction_frame, text="Personal medico disponible:").grid(row=2, column=0, padx=5, pady=5)

    # Entrada para número de pacientes
    entry3 = tk.Entry(satisfaction_frame)
    entry3.grid(row=2, column=1, padx=5, pady=5)

    # Botón para realizar la predicción
    predict_button = tk.Button(satisfaction_frame, text="Predecir satisfacción general", command=lambda: predict_patient_satisfaction(df,entry1.get(), entry2.get(), entry3.get()))
    predict_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Etiqueta para mostrar el resultado de la predicción
    global satisfaction_prediction_result_label
    satisfaction_prediction_result_label = tk.Label(satisfaction_frame, text="")
    satisfaction_prediction_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

def predict_waiting_time(patients: str, df: pd.DataFrame) -> None:
    try:
        num_patients = int(patients)
        
        # Preparar datos para el modelo
        x = df[[patients_treated_label]].values  # Columnas con el número de pacientes atendidos
        y = df[waiting_time_label].values        # Columnas con el tiempo de espera
        
        # Dividir los datos en conjunto de entrenamiento y prueba
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)
        
        # Entrenar el modelo de regresión lineal
        model = LinearRegression()
        model.fit(x_train, y_train)  # Entrena el modelo solo con los datos de entrenamiento
        
        # Evaluar el modelo con el conjunto de prueba (opcional)
        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Error Cuadrático Medio en el conjunto de prueba: {mse:.2f}")
        
        # Predecir el tiempo de espera basado en el número de pacientes ingresados
        predicted_waiting_time = model.predict([[num_patients]])  # Se usa una lista anidada
        
        # Mostrar el resultado
        prediction_result_label.config(text=f"Tiempo de Espera Predicho: {predicted_waiting_time[0]:.2f} minutos")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def predict_patient_satisfaction(df: pd.DataFrame, waiting_time: str, consultation_duration: str, medical_staff: str) -> None:
    try:
        # Convertir entradas a enteros
        waiting_time_int = int(waiting_time)
        consultation_duration_int = int(consultation_duration)
        medical_staff_int = int(medical_staff)

        # Preparar datos para el modelo
        x = df[['Tiempo de espera (min)', 'Duración de la consulta', 'Personal médico disponible']].values
        y = df['Satisfacción general'].values

        # Dividir los datos en conjunto de entrenamiento y prueba
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)

        # Entrenar el modelo de regresión lineal
        model = LinearRegression()
        model.fit(x_train, y_train)

        # Evaluar el modelo con el conjunto de prueba (opcional)
        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Error Cuadrático Medio en el conjunto de prueba: {mse:.2f}")

        # Predecir la satisfacción general basada en las nuevas entradas
        predicted_satisfaction = model.predict([[waiting_time_int, consultation_duration_int, medical_staff_int]])
        
        # Mostrar el resultado
        satisfaction_prediction_result_label.config(text=f"Satisfacción General Predicha: {predicted_satisfaction[0]:.2f}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
    except Exception as e:
        messagebox.showerror("Error en la predicción", str(e))

def predict_probability_of_recommendation(patients: str, df: pd.DataFrame):
    aux = 1