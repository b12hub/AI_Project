# test_api.py
# API'lar ishlaydimi tekshiramiz

import requests
from config import OPENWEATHER_API_KEY, OPENROUTE_API_KEY

def test_openweather():
    """OpenWeather API test"""
    print("🌦 OpenWeather API tekshirilmoqda...")
    
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Tashkent",
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  # Celsius uchun
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Ishlayapti! Toshkent harorati: {data['main']['temp']}°C")
        print(f"   Ob-havo: {data['weather'][0]['main']}")
        return True
    else:
        print(f"❌ Xato: {response.status_code}")
        print(f"   Xabar: {response.text}")
        return False

def test_openroute():
    """OpenRouteService API test"""
    print("\n🗺 OpenRouteService API tekshirilmoqda...")
    
    # Tashkent koordinatalari
    start = [69.2401, 41.2995]  # [longitude, latitude]
    # Samarkand koordinatalari
    end = [66.9597, 39.6270]
    
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    
    headers = {
        "Authorization": OPENROUTE_API_KEY
    }
    
    params = {
        "start": f"{start[0]},{start[1]}",
        "end": f"{end[0]},{end[1]}"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        distance = data['features'][0]['properties']['segments'][0]['distance'] / 1000  # km
        duration = data['features'][0]['properties']['segments'][0]['duration'] / 3600  # soat
        
        print(f"✅ Ishlayapti!")
        print(f"   Tashkent → Samarkand: {distance:.1f} km")
        print(f"   Taxminiy vaqt: {duration:.1f} soat")
        return True
    else:
        print(f"❌ Xato: {response.status_code}")
        print(f"   Xabar: {response.text}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("API'LARNI TEKSHIRISH")
    print("=" * 50)
    
    weather_ok = test_openweather()
    route_ok = test_openroute()
    
    print("\n" + "=" * 50)
    if weather_ok and route_ok:
        print("🎉 HAMMASI TAYYOR! Data yig'ishni boshlash mumkin!")
    else:
        print("⚠️ Ba'zi API'lar ishlamayapti. Kalitlarni tekshiring.")
    print("=" * 50)