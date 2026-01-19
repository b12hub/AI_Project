# utils.py
# Yordamchi funksiyalar

import random
from datetime import datetime, timedelta

def generate_order_id():
    """Noyob order ID yaratish"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_num = random.randint(1000, 9999)
    return f"ORD-{timestamp}-{random_num}"

def calculate_traffic_level(hour, weather, distance):
    """
    Tirbandlik darajasini hisoblash
    
    Qoidalar:
    - Rush hours (7-9, 17-19): Ko'proq tirbandlik
    - Yomon ob-havo: Ko'proq tirbandlik
    - Uzoq masofa: Kam tirbandlik (shahar tashqarida)
    """
    traffic_score = 0
    
    # Soatga qarab
    if 7 <= hour <= 9 or 17 <= hour <= 19:
        traffic_score += 2  # Rush hour
    elif 22 <= hour or hour <= 5:
        traffic_score -= 1  # Tunda kam
    
    # Ob-havoga qarab
    if weather in ["Rain", "Snow", "Fog"]:
        traffic_score += 2
    elif weather == "Clear":
        traffic_score -= 1
    
    # Masofaga qarab
    if distance > 200:
        traffic_score -= 1  # Shahardan tashqarida kam
    elif distance < 50:
        traffic_score += 1  # Shahar ichida ko'p
    
    # Natijani aniqlash
    if traffic_score >= 3:
        return "High"
    elif traffic_score >= 1:
        return "Medium"
    else:
        return "Low"

def estimate_delivery_time(distance, vehicle_type, traffic_level, weather):
    """
    Yetkazib berish vaqtini taxmin qilish (soatlarda)
    
    Formula:
    - Bazaviy vaqt = masofa / tezlik
    - Tezlik vehicle type'ga bog'liq
    - Traffic va weather qo'shimcha vaqt qo'shadi
    """
    
    # Bazaviy tezliklar (km/soat)
    base_speeds = {
        "Truck": 60,
        "Van": 70,
        "Car": 80,
        "Pickup": 75,
        "Motorcycle": 65
    }
    
    speed = base_speeds.get(vehicle_type, 70)
    
    # Bazaviy vaqt
    base_time = distance / speed
    
    # Traffic ta'siri
    traffic_delay = {
        "Low": 0,
        "Medium": 0.3,  # 30% ko'proq
        "High": 0.6     # 60% ko'proq
    }
    
    delay_factor = 1 + traffic_delay.get(traffic_level, 0)
    
    # Ob-havo ta'siri
    weather_delay = {
        "Clear": 0,
        "Clouds": 0.1,
        "Rain": 0.25,
        "Snow": 0.4,
        "Fog": 0.3
    }
    
    weather_factor = 1 + weather_delay.get(weather, 0)
    
    # Final vaqt
    total_time = base_time * delay_factor * weather_factor
    
    # Biroz tasodifiylik qo'shamiz (real hayotda farq bo'ladi)
    randomness = random.uniform(0.95, 1.05)
    
    return round(total_time * randomness, 2)

def get_random_datetime(days_back=30):
    """
    Tasodifiy sana va vaqt qaytarish
    (Oxirgi 30 kun ichida)
    """
    now = datetime.now()
    random_days = random.randint(0, days_back)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    
    random_date = now - timedelta(days=random_days)
    random_date = random_date.replace(
        hour=random_hours, 
        minute=random_minutes,
        second=0,
        microsecond=0
    )
    
    return random_date