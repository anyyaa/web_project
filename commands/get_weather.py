from geopy.geocoders import Nominatim
import requests
import json
from tokens import weather_api
import datetime

date = datetime.datetime.today()


def get_weather(city):
    geolocator = Nominatim(user_agent='weather-bot')
    location = geolocator.geocode(city)
    lat = location.latitude
    long = location.longitude
    weather_req = requests.get(
        'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}'.format(lat, long, weather_api))
    current_weather = json.loads(weather_req.text)['current']
    print(json.loads(weather_req.text))
    temp = round(current_weather['temp'] - 273.15)
    feels_like = round(current_weather['feels_like'] - 273.15)
    clouds = current_weather['clouds']
    wind_speed = current_weather['wind_speed']
    pressure = current_weather['pressure'] / 1.33
    humidity = current_weather['humidity']
    return f'Температура: {temp}°С, ощущается как {feels_like}°С.' \
           f' Облачность: {clouds}%, ' \
           f'скорость ветра - {wind_speed}м/с, ' \
           f'давление {str(pressure)[:3]} мм.рт.ст, ' \
           f'влажность {humidity}%'


def get_weather_days(days, city):
    days = int(days)
    # прогноз до 8 дней

    geolocator = Nominatim(user_agent='weather-bot')
    location = geolocator.geocode(city)
    lat = location.latitude
    long = location.longitude
    weather_req = requests.get(
        f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&exclude=hourly&appid={weather_api}')
    weather = json.loads(weather_req.text)['daily']

    daily_temp = [round(elem['temp']['day'] - 273.15) for elem in weather][:days]
    daily_pressure = [round(elem['pressure'] / 1.33) for elem in weather][:days]
    daily_humidity = [elem['humidity'] for elem in weather][:days]
    daily_wind = [elem['wind_speed'] for elem in weather][:days]
    resp_date, resp_temp, resp_pressure, resp_wind, resp_humidity = [], [], [], [], []

    for i in range(len(daily_wind)):
        resp_date.append(f'Forecast for {str(date + datetime.timedelta(days=i)).split()[0]}')
        resp_temp.append(f'Tempreture: {daily_temp[i]}')
        resp_pressure.append(f'Pressure: {daily_pressure[i]}')
        resp_wind.append(f'Wind: {daily_wind[i]}')
        resp_humidity.append(f'Humidity: {daily_humidity[i]}')
    return [resp_date, resp_temp, resp_pressure, resp_wind, resp_humidity]

