from datetime import datetime

import requests


def get_weather(lat: float, lon: float) -> dict:
    """
    Take latitude and longitude to get weather data
    using openweather api and return data in dict format
    """
    weather_key = '0a2c03e9dee2533389d7b459d0f8595e'
    # source contain JSON data from API
    source = requests.get('http://api.openweathermap.org/data/2.5/weather?'
                          f'lat={lat}&lon={lon}&appid={weather_key}')
    # list_of_data contain json encoded content
    data = source.json()
    result = {"weather": {
        "celsius": int(data['main']['temp']) - 272,
        "fahrenheit": int(((data['main']['temp']) - 272) * 1.8 + 32)},
        "city": str(data['name']),
        "sunset": datetime.fromtimestamp(
            data['sys']['sunset']),
        "sunrise": datetime.fromtimestamp(
            data['sys']['sunset']),
    }
    return result
