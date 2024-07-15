import pandas as pd

# Carga de los datos
df = pd.read_csv('weather_data.csv')

# Manejo de valores nulos (aunque no debería haber ninguno en este caso)
df.fillna(0, inplace=True)

# Normalización de los datos
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['temperature', 'humidity', 'pressure']] = scaler.fit_transform(df[['temperature', 'humidity', 'pressure']])

# Guardar los datos preprocesados
df.to_csv('preprocessed_weather_data.csv', index=False)
