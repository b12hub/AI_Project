# 🚚 Transport & Logistics Dataset Collection

**Maqsad:** Machine Learning modellari uchun **69,975 qatorlik** transport va logistika ma'lumotlarini yig'ish.

---

## 📊 Dataset Haqida

| Parametr | Qiymat |
|----------|--------|
| **Qatorlar soni** | 69,975 |
| **Ustunlar soni** | 12 |
| **Fayl hajmi** | ~6.4 MB |
| **Format** | CSV |
| **Sana** | 2026-01-05 |

---

## 🎯 Loyiha Maqsadi

Ushbu dataset **yetkazib berish vaqtini bashorat qilish** (delivery time prediction) uchun yaratilgan.

**Asosiy savol:**
> Berilgan shahar, transport turi, ob-havo va boshqa parametrlarga qarab, yuk qancha vaqtda yetib boradi?

---

## 🗂 Dataset Strukturasi

### Ustunlar (12 ta):

| Ustun nomi | Turi | Tavsif | Misol |
|------------|------|--------|-------|
| `order_id` | string | Noyob buyurtma ID | `ORD-20260105133858-9510` |
| `origin_city` | string | Jo'nash shahri | `Tashkent` |
| `destination_city` | string | Yetib borish shahri | `Samarkand` |
| `distance_km` | float | Masofa (kilometr) | `292.9` |
| `vehicle_type` | string | Transport turi | `Truck` |
| `order_date` | string | Buyurtma sanasi | `2025-12-15` |
| `order_hour` | int | Buyurtma soati (0-23) | `14` |
| `weekday` | string | Hafta kuni | `Monday` |
| `weather` | string | Ob-havo sharoiti | `Clouds` |
| `temperature` | float | Harorat (°C) | `7.0` |
| `traffic_level` | string | Tirbandlik darajasi | `Low` / `Medium` / `High` |
| `delivery_time_hours` | float | **TARGET**: Yetkazish vaqti (soat) | `4.57` |

---

## 📍 Shaharlar (10 ta)
```
1. Tashkent (Toshkent)
2. Samarkand (Samarqand)
3. Bukhara (Buxoro)
4. Khiva (Xiva)
5. Nukus (Nukus)
6. Andijan (Andijon)
7. Fergana (Farg'ona)
8. Namangan (Namangan)
9. Urgench (Urganch)
10. Termez (Termez)
```

**Shahar juftliklari:** 45 yo'nalish (10 × 9 / 2)

---

## 🚗 Transport Turlari (5 ta)

- **Truck** — Yuk mashinasi
- **Van** — Furgon
- **Car** — Yengil mashina
- **Pickup** — Pikap
- **Motorcycle** — Mototsikl

---

## 🌦 Ob-havo Turlari

- `Clear` — Ochiq
- `Clouds` — Bulutli
- `Rain` — Yomg'irli
- `Snow` — Qorli
- `Fog` — Tumanli
- `Mist` — Duman

---

## 🚦 Tirbandlik Darajasi

| Daraja | Tavsif |
|--------|--------|
| **Low** | Kam tirbandlik |
| **Medium** | O'rtacha tirbandlik |
| **High** | Yuqori tirbandlik |

**Tirbandlik qanday hisoblanadi:**
- Rush hours (7-9, 17-19): 🔴 Ko'proq
- Yomon ob-havo: 🔴 Ko'proq
- Uzoq masofa (shahar tashqarida): 🟢 Kamroq

---

## 🔌 Ma'lumot Manbalari

### 1️⃣ OpenWeather API
🔗 https://openweathermap.org/api

**Nima olindi:**
- Harorat
- Ob-havo sharoiti
- Shamol tezligi
- Namlik

**So'rovlar soni:** ~1,000 call

---

### 2️⃣ OpenRouteService API
🔗 https://openrouteservice.org

**Nima olindi:**
- Shaharlar orasidagi masofa
- Taxminiy yo'l vaqti

**So'rovlar soni:** ~100 call

---

### 3️⃣ Sintetik Ma'lumotlar

Quyidagi parametrlar **algoritmik ravishda** yaratildi:

- `order_date`, `order_hour`, `weekday` — Tasodifiy sanalar (oxirgi 60 kun)
- `traffic_level` — Rule-based hisoblash
- `delivery_time_hours` — Formula asosida hisoblash

---

## 📐 Yetkazish Vaqti Formulasi
```python
delivery_time = (distance / base_speed) × traffic_factor × weather_factor
```

**Tezlik (km/soat):**
- Truck: 60
- Van: 70
- Car: 80
- Pickup: 75
- Motorcycle: 65

**Traffic factor:**
- Low: 1.0 (0%)
- Medium: 1.3 (+30%)
- High: 1.6 (+60%)

**Weather factor:**
- Clear: 1.0
- Clouds: 1.1 (+10%)
- Rain: 1.25 (+25%)
- Snow: 1.4 (+40%)
- Fog: 1.3 (+30%)

---

## 🛠 Texnologiyalar

- **Python 3.x**
- **Kutubxonalar:**
  - `requests` — API so'rovlari
  - `pandas` — Data boshqaruv
  - `datetime` — Vaqt bilan ishlash

---

## 📂 Fayllar Strukturasi
```
transport_data_collection/
│
├── config.py              # API kalitlari va sozlamalar
├── utils.py               # Yordamchi funksiyalar
├── data_collector.py      # Asosiy data yig'ish
├── run.py                 # Ishga tushirish
├── test_api.py            # API test
├── test_utils.py          # Funksiyalar test
│
├── output/
│   └── raw_data.csv       # YAKUNIY DATASET
│
└── README.md              # Bu fayl
```

---

## 🚀 Qanday Ishlatish

### 1️⃣ Talablarni O'rnatish
```bash
pip install requests pandas
```

### 2️⃣ API Kalitlarini Olish

- OpenWeather: https://openweathermap.org/api
- OpenRouteService: https://openrouteservice.org/dev/#/signup

### 3️⃣ `config.py` ni Tahrirlash
```python
OPENWEATHER_API_KEY = "sizning_kalit"
OPENROUTE_API_KEY = "sizning_kalit"
```

### 4️⃣ Ishga Tushirish
```bash
python3 run.py
```

⏱ **Vaqt:** ~5-7 daqiqa

---

## 📈 Dataset Statistikasi
```python
import pandas as pd

df = pd.read_csv('output/raw_data.csv')

print(f"Qatorlar: {len(df)}")
print(f"Ustunlar: {len(df.columns)}")
print(f"\nNa'lumotlar:")
print(df.info())
```

---

## 🧹 Keyingi Qadamlar

1. **Data Cleaning**
   - Null qiymatlarni tekshirish
   - Outlier'larni topish
   - Data type'larni to'g'irlash

2. **EDA (Exploratory Data Analysis)**
   - Vizualizatsiya
   - Korrelyatsiya tahlili
   - Feature engineering

3. **Model Training**
   - Train/test split
   - Model tanlash (Random Forest, XGBoost, etc.)
   - Hyperparameter tuning

---

## 👥 Jamoa

- **API & Data Collection:** [Nurmuhammad]
- **Data Cleaning:** [Bobur]
- **Model Training:** [Matmurod]

---

## 📄 Litsenziya

Ushbu dataset o'quv maqsadlari uchun yaratilgan.

---

## 🙏 Minnatdorchilik

- OpenWeather API
- OpenRouteService API
- Pandas jamiyati

---

## 📞 Aloqa

Savollar bo'lsa:
- Email: [nurmuhammadsamadov63@gmail.com]
- GitHub: [nurmuhammad1160]

---

**Yaratilgan sana:** 2026-01-05  
**Versiya:** 1.0  
**Dataset hajmi:** 69,975 qator