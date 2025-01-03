# Real time city Weather Update 
import requests
def get_weather(city):
    # OpenWeatherMap API key
    api_key = "2c2b4ebb1cc8313df2981efa70ed920a"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # API query
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Temperature in Celsius
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather}")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or API error!")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)

'''API Key সংগ্রহ
OpenWeatherMap এ গিয়ে একটি ফ্রি অ্যাকাউন্ট তৈরি করুন।
একটি API Key সংগ্রহ করুন।'''