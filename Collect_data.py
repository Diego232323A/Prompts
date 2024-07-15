import requests
import pandas as pd

API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
CITIES = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
URL = 'http://api.openweathermap.org/data/2.5/weather'

weather_data = []

for city in CITIES:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(URL, params=params)
    data = response.json()

    if 'main' in data:
        city_weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure']
        }
        weather_data.append(city_weather)
    else:
        print(f"Error fetching data for {city}: {data.get('message', 'Unknown error')}")

df = pd.DataFrame(weather_data)
df.to_csv('weather_data.csv', index=False)
