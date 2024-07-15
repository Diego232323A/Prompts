# Weather Prediction API

This project collects weather data using the OpenWeatherMap API, preprocesses it, trains a linear regression model to predict temperature based on humidity and pressure, and deploys the model to an API using Flask.

## Requirements

- Python 3.6 or higher
- OpenWeatherMap API Key

## Facility

1. Clone the repository:

 ```bash
 git clone https://github.com/Diego232323A/Prompts.git
 cd weather-prediction-api
 ```

2. Install the dependencies:

 ```bash
 pip install -r requirements.txt
 ```

3. Obtain an OpenWeatherMap API key and replace `'YOUR_OPENWEATHERMAP_API_KEY'` in the code with your valid API key.

## Use

### 1. Data Collection

Run the `Collect_data.py` script to collect weather data.

### 2. Data Preprocessing
Run the script `Preprocess_data.py` to preprocess the data.

### 3. Model Training
Run the script `Train_model.py` to train the model.

### 4. Model Deployment
Run the script `Deploy_model.py` to deploy the API.

### 5.Test the API
Send a POST request to http://127.0.0.1:5000/predict with JSON like this:
{
 "humidity": 50,
 "pressure": 1013
}