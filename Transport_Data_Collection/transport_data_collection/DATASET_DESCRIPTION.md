# 📊 Dataset Tafsilotlari

## Dataset Nomi
**Transport & Logistics Delivery Time Dataset**

---

## Umumiy Ma'lumot

- **Jami qatorlar:** 69,975
- **Jami ustunlar:** 12
- **Missing values:** 0 (dataset to'liq to'ldirilgan)
- **Fayl formati:** CSV
- **Fayl hajmi:** ~6.4 MB
- **Encoding:** UTF-8

---

## Ustunlar Tafsiloti

### 1. order_id (string)
**Tavsif:** Har bir buyurtma uchun noyob identifikator

**Format:** `ORD-YYYYMMDDHHMMSS-NNNN`
- `ORD` — Order prefiksi
- `YYYYMMDDHHMMSS` — Timestamp
- `NNNN` — 4 xonali tasodifiy raqam

**Misol:** `ORD-20260105133858-9510`

**Null qiymatlar:** 0

---

### 2. origin_city (string)
**Tavsif:** Yukni jo'natish shahri

**Mumkin bo'lgan qiymatlar:** 10 ta shahar
```
Tashkent, Samarkand, Bukhara, Khiva, Nukus,
Andijan, Fergana, Namangan, Urgench, Termez
```

**Taqsimot:** Taxminan teng (har bir shahar ~15.5%)

**Null qiymatlar:** 0

---

### 3. destination_city (string)
**Tavsif:** Yukni qabul qilish shahri

**Mumkin bo'lgan qiymatlar:** 10 ta shahar (origin_city bilan bir xil)

**Qoida:** `origin_city ≠ destination_city` (bir shahar ichida yo'q)

**Null qiymatlar:** 0

---

### 4. distance_km (float)
**Tavsif:** Shaharlar orasidagi yo'l masofasi (kilometr)

**Manba:** OpenRouteService API (real yo'l masofasi)

**Diapazon:** 76.7 km (eng qisqa) — 1433.6 km (eng uzoq)

**O'rtacha:** ~450 km

**Null qiymatlar:** 0

**Misol:** `292.9`

---

### 5. vehicle_type (string)
**Tavsif:** Yuk tashish uchun ishlatiladigan transport turi

**Mumkin bo'lgan qiymatlar:**
- `Truck` — Yuk mashinasi (katta yuk)
- `Van` — Furgon (o'rta yuk)
- `Car` — Yengil mashina (kichik yuk)
- `Pickup` — Pikap
- `Motorcycle` — Mototsikl (tezkor yetkazish)

**Taqsimot:** Tasodifiy, har bir tur ~20%

**Null qiymatlar:** 0

---

### 6. order_date (string)
**Tavsif:** Buyurtma berilgan sana

**Format:** `YYYY-MM-DD`

**Diapazon:** Oxirgi 60 kun (2025-11-06 dan 2026-01-04 gacha)

**Null qiymatlar:** 0

**Misol:** `2025-12-15`

---

### 7. order_hour (int)
**Tavsif:** Buyurtma berilgan soat (24-soatlik format)

**Diapazon:** 0 — 23

**Taqsimot:** Tasodifiy

**Null qiymatlar:** 0

**Misol:** `14` (soat 14:00)

---

### 8. weekday (string)
**Tavsif:** Hafta kuni

**Mumkin bo'lgan qiymatlar:**
```
Monday, Tuesday, Wednesday, Thursday,
Friday, Saturday, Sunday
```

**Taqsimot:** Taxminan teng (~14.3% har biri)

**Null qiymatlar:** 0

---

### 9. weather (string)
**Tavsif:** Ob-havo sharoiti

**Manba:** OpenWeather API (real ma'lumot)

**Mumkin bo'lgan qiymatlar:**
- `Clear` — Ochiq
- `Clouds` — Bulutli
- `Rain` — Yomg'irli
- `Snow` — Qorli
- `Fog` — Tumanli
- `Mist` — Duman

**Null qiymatlar:** 0

**Eslatma:** Origin va destination shaharlaridan biri tanlangan

---

### 10. temperature (float)
**Tavsif:** Harorat (Celsius)

**Manba:** OpenWeather API

**Diapazon:** -5°C — 35°C (Uzbekiston iqlimiga mos)

**Null qiymatlar:** 0

**Misol:** `7.0`

---

### 11. traffic_level (string)
**Tavsif:** Yo'l tirbandligi darajasi

**Hisoblash usuli:** Rule-based algoritm

**Mumkin bo'lgan qiymatlar:**
- `Low` — Kam tirbandlik
- `Medium` — O'rtacha tirbandlik
- `High` — Yuqori tirbandlik

**Hisoblash omillari:**
1. **Soat:**
   - Rush hours (7-9, 17-19): +2 ball
   - Tunda (22-5): -1 ball

2. **Ob-havo:**
   - Rain/Snow/Fog: +2 ball
   - Clear: -1 ball

3. **Masofa:**
   - >200 km: -1 ball (shahar tashqarida)
   - <50 km: +1 ball (shahar ichida)

**Qoida:**
- ≥3 ball → High
- ≥1 ball → Medium
- <1 ball → Low

**Null qiymatlar:** 0

---

### 12. delivery_time_hours (float) ⭐ TARGET
**Tavsif:** Yukni yetkazib berish vaqti (soat)

**Bu — MODEL UCHUN BASHORAT QILINADIGAN QIYMAT**

**Hisoblash formulasi:**
```
delivery_time = (distance / base_speed) × traffic_factor × weather_factor × randomness
```

**Diapazon:** 0.5 soat — 25 soat

**O'rtacha:** ~6-8 soat

**Null qiymatlar:** 0

**Misol:** `4.57`

---

## Ma'lumotlar Manbasi

### Real API Ma'lumotlar
1. **OpenWeather API**
   - `weather`
   - `temperature`

2. **OpenRouteService API**
   - `distance_km`

### Sintetik Ma'lumotlar
1. **Tasodifiy generatsiya:**
   - `order_date`
   - `order_hour`
   - `weekday`
   - `vehicle_type`

2. **Hisoblangan qiymatlar:**
   - `traffic_level` (rule-based)
   - `delivery_time_hours` (formula-based)

---

## Data Quality

✅ **Afzalliklar:**
- To'liq to'ldirilgan (null qiymatlar yo'q)
- Real API ma'lumotlari
- Mantiqiy bog'lanishlar
- Katta hajm (69,975 qator)

⚠️ **Cheklovlar:**
- Faqat Uzbekiston shaharlari
- Qishki oylar ma'lumotlari (60 kun)
- Ba'zi feature'lar sintetik

---

## Ishlatish Tavsiялari

### Model Training Uchun

1. **Feature Engineering:**
   - `distance_km` → log transformation
   - `order_hour` → cyclical encoding (sin/cos)
   - One-hot encoding: `vehicle_type`, `weather`, `weekday`

2. **Train/Test Split:**
   - 80% train, 20% test
   - Yoki time-based split (oxirgi 2 hafta — test)

3. **Target:**
   - `delivery_time_hours` — regression task

---

## Sample Data
```csv
order_id,origin_city,destination_city,distance_km,vehicle_type,order_date,order_hour,weekday,weather,temperature,traffic_level,delivery_time_hours
ORD-20260105133858-9510,Tashkent,Samarkand,292.9,Truck,2025-12-21,3,Saturday,Clouds,4.7,Low,5.57
ORD-20260105133858-5857,Tashkent,Samarkand,292.9,Pickup,2025-12-16,12,Monday,Mist,7.0,Low,4.06
```

---

**Oxirgi yangilanish:** 2026-01-05