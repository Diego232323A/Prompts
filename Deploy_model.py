from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Cargar el modelo entrenado
model = LinearRegression()
df = pd.read_csv('preprocessed_weather_data.csv')
X = df[['humidity', 'pressure']]
y = df['temperature']
model.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    humidity = data['humidity']
    pressure = data['pressure']
    # Crear un DataFrame con los nombres de características adecuados
    input_data = pd.DataFrame([[humidity, pressure]], columns=['humidity', 'pressure'])
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
