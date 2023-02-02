# Sky.py -  module to get weather data
# aka knowing if its hot without even opening my door

import requests

class Sky:
    def __init__(self):
        pass

    def Fetch_Weather_Data(self):

        API_KEY  = "218977d47345c7b68bba837d21cb2d47"
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

        city = "clarksville"
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)
        
        weather_data = response.json()
        
        #? Grabbing specfic data from json 
        weather = weather_data["weather"][0]["main"]
        temp = weather_data["main"]["temp"]
        fl = weather_data["main"]["feels_like"]
        
        #? equation to turn it from kelvin to fahrenheit and round 
        feels_like =  round(1.8*(fl-273) + 32.)
        temperature = round(1.8*(temp-273) + 32.)
       
        #? Returns tuple and has to be this order when using function       
        return weather, temperature, feels_like 
        
#? How to use |
#?           \_/
if __name__ == "__main__":
    S = Sky()
    weather, temp, feels_like = S.Fetch_Weather_Data()
    print(f"Weather: {weather}")
    print(f"Temperature: {temp}")
    print(f"feels like: {feels_like}")
    

