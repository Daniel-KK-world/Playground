import requests

#define variables for api key and base url

API_KEY = 'your_openweathermap_api_key'  #replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

#fetch weather data from openweathermap api for a given city
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None
    
    
#display temperature and weather description
def display_weather(city):
    weather_data = get_weather(city)
    if weather_data:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Current temperature in {city} is {temp}°C with {description}.")
    else:
        print(f"Could not retrieve weather data for {city}.")
        
        
#now let's write a main function to test
if __name__ == "__main__":
    while True:
        city = input("Enter city name: ").strip()
        if not city:
            print("City name cannot be empty. Please try again.")
            continue
        display_weather(city)
        break
    
    