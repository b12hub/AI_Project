# test_utils.py

from utils import *

print("=" * 50)
print("YORDAMCHI FUNKSIYALARNI TEST QILISH")
print("=" * 50)

# 1. Order ID
print("\n1️⃣ Order ID generatsiya:")
for i in range(3):
    print(f"   {generate_order_id()}")

# 2. Traffic level
print("\n2️⃣ Traffic level hisoblash:")
print(f"   Ertalab 8:00, Rain, 20km: {calculate_traffic_level(8, 'Rain', 20)}")
print(f"   Tunda 2:00, Clear, 300km: {calculate_traffic_level(2, 'Clear', 300)}")
print(f"   Kechqurun 18:00, Fog, 50km: {calculate_traffic_level(18, 'Fog', 50)}")

# 3. Delivery time
print("\n3️⃣ Delivery time taxmin qilish:")
print(f"   Truck, 292km, Medium traffic, Clouds: {estimate_delivery_time(292, 'Truck', 'Medium', 'Clouds')} soat")
print(f"   Motorcycle, 50km, High traffic, Rain: {estimate_delivery_time(50, 'Motorcycle', 'High', 'Rain')} soat")

# 4. Random datetime
print("\n4️⃣ Tasodifiy vaqtlar:")
for i in range(3):
    dt = get_random_datetime()
    print(f"   {dt.strftime('%Y-%m-%d %H:%M')} - {dt.strftime('%A')}")

print("\n" + "=" * 50)