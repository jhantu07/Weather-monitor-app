
from sqlalchemy import create_engine, Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database connection
Base = declarative_base()
DATABASE_URL = "sqlite:///weather.db"  # You can use SQLite for now

class DailyWeatherSummary(Base):
    __tablename__ = 'daily_weather_summary'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    avg_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    dominant_condition = Column(String)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
import requests
from datetime import datetime
import time

API_KEY = 'bc43573b44fee853878f60e444bd58e3'  # Replace 'your_api_key' with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def fetch_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

# Example usage for one city
data = fetch_weather_data('Delhi')
print(data)

def process_weather_data(data):
    main = data['main']
    weather = data['weather'][0]
    temp = main['temp']
    feels_like = main['feels_like']
    dominant_condition = weather['main']

    return {
        'temp': temp,
        'feels_like': feels_like,
        'condition': dominant_condition
    }

def save_daily_summary(session, date, avg_temp, max_temp, min_temp, dominant_condition):
    summary = DailyWeatherSummary(
        date=date,
        avg_temp=avg_temp,
        max_temp=max_temp,
        min_temp=min_temp,
        dominant_condition=dominant_condition
    )
    session.add(summary)
    session.commit()
def check_alerts(current_temp):
    """Checks if the current temperature exceeds the threshold and triggers an alert."""
    if current_temp > 35:
        print(f"Alert: High temperature detected: {current_temp}°C")
