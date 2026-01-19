import requests
import pandas as pd
import time
import random
from datetime import datetime
from itertools import combinations

from config import (
    OPENWEATHER_API_KEY,
    OPENROUTE_API_KEY,
    CITIES,
    VEHICLE_TYPES,
    WEEKDAYS
)

from utils import (
    generate_order_id,
    calculate_traffic_level,
    estimate_delivery_time,
    get_random_datetime
)


class TransportDataCollector:
    """Transport & Logistics data yig'ish klassi"""
    
    def __init__(self):
        self.weather_cache = {}  # Ob-havo ma'lumotlarini saqlash
        self.distance_cache = {}  # Masofa ma'lumotlarini saqlash
        self.collected_data = []  # Yig'ilgan datalar
        
    def get_weather(self, city):
        """
        Shahar uchun ob-havo ma'lumotini olish
        Cache ishlatamiz — bir shahar uchun faqat 1 marta API chaqiramiz
        """
        if city in self.weather_cache:
            print(f"   📦 Cache'dan olindi: {city}")
            return self.weather_cache[city]
        
        print(f"   🌐 API'dan olinyapti: {city}")
        
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": f"{city},UZ",  # Uzbekistan
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                weather_info = {
                    "temperature": round(data['main']['temp'], 1),
                    "weather": data['weather'][0]['main'],
                    "wind_speed": round(data['wind']['speed'], 1),
                    "humidity": data['main']['humidity']
                }
                
                # Cache'ga saqlash
                self.weather_cache[city] = weather_info
                
                # API rate limit uchun biroz kutamiz
                time.sleep(0.5)
                
                return weather_info
            else:
                print(f"   ⚠️ Xato: {response.status_code}")
                # Default qiymat
                return {
                    "temperature": 20,
                    "weather": "Clear",
                    "wind_speed": 5,
                    "humidity": 50
                }
        
        except Exception as e:
            print(f"   ❌ Exception: {e}")
            return {
                "temperature": 20,
                "weather": "Clear",
                "wind_speed": 5,
                "humidity": 50
            }
    
    def get_distance(self, city1, city2):
        """
        Ikki shahar orasidagi masofani olish
        Cache ishlatamiz
        """
        # Cache key
        cache_key = tuple(sorted([city1, city2]))
        
        if cache_key in self.distance_cache:
            return self.distance_cache[cache_key]
        
        # Koordinatalar (Uzbekiston shaharlari)
        coordinates = {
            "Tashkent": [69.2401, 41.2995],
            "Samarkand": [66.9597, 39.6270],
            "Bukhara": [64.4256, 39.7747],
            "Khiva": [60.3632, 41.3775],
            "Nukus": [59.6103, 42.4530],
            "Andijan": [72.3442, 40.7821],
            "Fergana": [71.7864, 40.3864],
            "Namangan": [71.6726, 40.9983],
            "Urgench": [60.6318, 41.5500],
            "Termez": [67.2783, 37.2242]
        }
        
        if city1 not in coordinates or city2 not in coordinates:
            # Agar shahar topilmasa, taxminiy masofa
            return {"distance": 200, "duration": 3}
        
        start = coordinates[city1]
        end = coordinates[city2]
        
        print(f"   🗺 Masofa hisoblanmoqda: {city1} → {city2}")
        
        url = "https://api.openrouteservice.org/v2/directions/driving-car"
        
        headers = {
            "Authorization": OPENROUTE_API_KEY
        }
        
        params = {
            "start": f"{start[0]},{start[1]}",
            "end": f"{end[0]},{end[1]}"
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                distance_km = round(
                    data['features'][0]['properties']['segments'][0]['distance'] / 1000, 1
                )
                duration_hours = round(
                    data['features'][0]['properties']['segments'][0]['duration'] / 3600, 2
                )
                
                result = {
                    "distance": distance_km,
                    "duration": duration_hours
                }
                
                # Cache'ga saqlash
                self.distance_cache[cache_key] = result
                
                # Rate limit
                time.sleep(0.5)
                
                return result
            else:
                print(f"   ⚠️ Xato: {response.status_code}")
                # Taxminiy qiymat
                return {"distance": 200, "duration": 3}
        
        except Exception as e:
            print(f"   ❌ Exception: {e}")
            return {"distance": 200, "duration": 3}
    
    def generate_dataset(self, target_rows=70000):
        """
        Asosiy dataset yaratish
        
        Strategiya:
        1. Shahar juftliklarini yaratamiz (10 × 9 = 90 juftlik)
        2. Har bir juftlik uchun weather + distance olmaiz
        3. Har bir juftlikni ko'paytiramiz (vehicle, time, etc.)
        """
        
        print("\n" + "=" * 60)
        print("DATA YIG'ISH BOSHLANDI")
        print("=" * 60)
        
        # 1. Shahar juftliklarini yaratish
        print("\n📍 Shahar juftliklarini yaratish...")
        city_pairs = list(combinations(CITIES, 2))
        print(f"   Jami juftliklar: {len(city_pairs)}")
        
        # 2. Har bir juftlik uchun weather + distance olish
        print("\n🌐 API'lardan ma'lumot yig'ilmoqda...")
        
        base_data = []
        
        for idx, (city1, city2) in enumerate(city_pairs, 1):
            print(f"\n[{idx}/{len(city_pairs)}] {city1} ↔ {city2}")
            
            # Weather (har bir shahar uchun)
            weather1 = self.get_weather(city1)
            weather2 = self.get_weather(city2)
            
            # Distance
            distance_info = self.get_distance(city1, city2)
            
            # Saqlash
            base_data.append({
                "origin_city": city1,
                "destination_city": city2,
                "distance_km": distance_info["distance"],
                "origin_weather": weather1["weather"],
                "origin_temp": weather1["temperature"],
                "dest_weather": weather2["weather"],
                "dest_temp": weather2["temperature"]
            })
        
        print(f"\n✅ API'dan yig'ildi: {len(base_data)} juftlik")
        
        # 3. Data'ni ko'paytirish (target_rows ga yetguncha)
        print(f"\n🔄 Data ko'paytirilmoqda → {target_rows} qator...")
        
        rows_per_pair = target_rows // len(base_data)
        print(f"   Har bir juftlik uchun: {rows_per_pair} qator")
        
        for base in base_data:
            for _ in range(rows_per_pair):
                # Tasodifiy parametrlar
                dt = get_random_datetime(days_back=60)
                hour = dt.hour
                weekday = dt.strftime("%A")
                vehicle = random.choice(VEHICLE_TYPES)
                
                # Weather (origin va destination o'rtasida)
                # Ba'zan origin, ba'zan dest weather'ni olish
                weather = random.choice([base["origin_weather"], base["dest_weather"]])
                temperature = random.choice([base["origin_temp"], base["dest_temp"]])
                
                # Traffic level hisoblash
                traffic = calculate_traffic_level(
                    hour, 
                    weather, 
                    base["distance_km"]
                )
                
                # Delivery time hisoblash
                delivery_time = estimate_delivery_time(
                    base["distance_km"],
                    vehicle,
                    traffic,
                    weather
                )
                
                # Qatorni qo'shish
                row = {
                    "order_id": generate_order_id(),
                    "origin_city": base["origin_city"],
                    "destination_city": base["destination_city"],
                    "distance_km": base["distance_km"],
                    "vehicle_type": vehicle,
                    "order_date": dt.strftime("%Y-%m-%d"),
                    "order_hour": hour,
                    "weekday": weekday,
                    "weather": weather,
                    "temperature": temperature,
                    "traffic_level": traffic,
                    "delivery_time_hours": delivery_time
                }
                
                self.collected_data.append(row)
        
        print(f"\n🎉 Jami yig'ildi: {len(self.collected_data)} qator")
        
        return self.collected_data
    
    def save_to_csv(self, filename="output/raw_data.csv"):
        """Data'ni CSV ga saqlash"""
        
        print(f"\n💾 CSV ga saqlanmoqda: {filename}")
        
        df = pd.DataFrame(self.collected_data)
        df.to_csv(filename, index=False)
        
        print(f"✅ Saqlandi: {len(df)} qator, {len(df.columns)} ustun")
        print(f"\n📊 Dataset ma'lumotlari:")
        print(df.info())
        print(f"\n📈 Birinchi 5 qator:")
        print(df.head())
        
        return df