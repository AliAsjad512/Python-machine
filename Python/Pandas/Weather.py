import requests
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class WeatherData:
    location: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    wind_speed: float
    description: str
    icon: str
    timestamp: str

class WeatherAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or "YOUR_API_KEY"  # Get from openweathermap.org
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city, country_code=None, units='metric'):
        """Get current weather for a city"""
        query = f"{city},{country_code}" if country_code else city
        
        params = {
            'q': query,
            'appid': self.api_key,
            'units': units
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            return WeatherData(
                location=f"{data['name']}, {data['sys']['country']}",
                temperature=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                humidity=data['main']['humidity'],
                pressure=data['main']['pressure'],
                wind_speed=data['wind']['speed'],
                description=data['weather'][0]['description'],
                icon=data['weather'][0]['icon'],
                timestamp=datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            )
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather: {e}")
            return None
    
    def get_weather_by_coords(self, lat, lon, units='metric'):
        """Get weather by coordinates"""
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': units
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            return self.get_weather(data['name'], data['sys']['country'])
        except:
            return None
    
    def display_weather(self, weather_data):
        """Display weather in a readable format"""
        if not weather_data:
            print("No weather data available")
            return
        
        print(f"\n{'='*40}")
        print(f"WEATHER REPORT - {weather_data.location}")
        print(f"{'='*40}")
        print(f"Temperature: {weather_data.temperature}°C")
        print(f"Feels like: {weather_data.feels_like}°C")
        print(f"Humidity: {weather_data.humidity}%")
        print(f"Pressure: {weather_data.pressure} hPa")
        print(f"Wind Speed: {weather_data.wind_speed} m/s")
        print(f"Conditions: {weather_data.description.title()}")
        print(f"Last Updated: {weather_data.timestamp}")
        print(f"{'='*40}")

# Usage
weather = WeatherAPI()
# data = weather.get_weather("London", "UK")
# weather.display_weather(data)