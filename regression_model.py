import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Día': [1, 2, 3, 4, 5],
    'Pacientes Atendidos': [20, 25, 18, 30, 22],
    'Tiempo de Espera (min)': [15, 20, 12, 25, 18]
}

df = pd.DataFrame(data)

X = df[['Pacientes Atendidos']]
y = df['Tiempo de Espera (min)']

model = LinearRegression()
model.fit(X, y)

def predict_wait_time(patients: int) -> float:
    """Predice el tiempo de espera en función del número de pacientes atendidos."""
    return model.predict([[patients]])[0]
