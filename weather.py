import requests

def weather():
    # Replace with your actual API key
    API_KEY = "YOUR API KEY HERE"  

    # Replace with correct coordinates for Mokopane
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={-23.9050}&lon={29.4603}&appid={API_KEY}&units=metric" 

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if request fails

        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]

        print("Current weather in Mokopane:")
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Feels like: {feels_like:.1f}°C")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Humidity: {humidity:.2f}%")
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch weather data. Reason: {e}")

