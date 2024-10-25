import requests

API_KEY = "bc43573b44fee853878f60e444bd58e3"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None
