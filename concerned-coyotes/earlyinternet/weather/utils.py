import json
import urllib.request



def get_weather(lat,lon):
    key='0a2c03e9dee2533389d7b459d0f8595e'
    # source contain JSON data from API 
    source=urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}').read()

    # converting JSON data to a dictionary
    list_of_data=json.loads(source)
    data = {  
            "Temp": str(float(list_of_data['main']['temp'])-272.15)+ '°C',
            "City":str(list_of_data['name']), 
        } 
    return data

if __name__=="__main__":
    weather_data=get_weather(21.178,72.83)
    print(weather_data)
