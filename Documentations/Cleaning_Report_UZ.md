# **MA'LUMOTLARNI TOZALASH VA VALIDATSIYA XULOSASI**

## **KIRUVCHI MA'LUMOTLAR TO'PLAMI (INPUT DATASET)**

* **Fayl:** raw_data.csv
* **Qatorlar:** 69,975
* **Ustunlar:** 12

## **CHIQUVCHI MA'LUMOTLAR TO'PLAMI (OUTPUT DATASET)**

* **Fayl:** clean_data_v1.csv
* **Qatorlar:** 69,926
* **Ustunlar:** 11

## **TRANSFORMATSIYA XULOSASI**

* **Kiruvchi qatorlar:** 69,975
* **Chiquvchi qatorlar:** 69,926
* **O'chirilgan qatorlar:** 49

## **O'CHIRILGAN USTUNLAR**

* **order_id** - *Asos: Sintetik identifikator, modellashtirishda foydalanilmaydi*

## **QOLGAN USTUNLAR**

* origin_city
* destination_city
* distance_km
* vehicle_type
* order_date
* order_hour
* weekday
* weather
* temperature
* traffic_level
* delivery_time_hours

## **MA'LUMOT TURLARINI QAT'IY BELGILASH (DATA TYPE ENFORCEMENT)**

* ✅ **distance_km:** float64
* ✅ **order_hour:** int64
* ✅ **temperature:** float64
* ✅ **delivery_time_hours:** float64
* ✅ **order_date:** datetime64[ns]

## **QAT'IY VALIDATSIYA QOIDALARI (BARCHASI MUVAFFAQIYATLI)**

* ✅ **order_hour ∈ [0, 23]:** 0 ta qoidabuzarlik
* ✅ **distance_km > 0:** 0 ta qoidabuzarlik
* ✅ **delivery_time_hours > 0:** 0 ta qoidabuzarlik
* ✅ **origin_city ≠ destination_city:** 0 ta qoidabuzarlik

## **KATEGORIK NORMALIZATSIYA**

* ✅ Barcha kategorik ustunlar chetki bo'shliqlardan tozalandi (trimmed) va kichik harflarga o'tkazildi
* ✅ **origin_city:** 69,975 ta qiymat o'zgartirildi
* ✅ **destination_city:** 69,975 ta qiymat o'zgartirildi
* ✅ **vehicle_type:** 69,975 ta qiymat o'zgartirildi
* ✅ **weekday:** 69,975 ta qiymat o'zgartirildi
* ✅ **weather:** 69,975 ta qiymat o'zgartirildi
* ✅ **traffic_level:** 69,975 ta qiymat o'zgartirildi

## **DUBLIKATLAR (DUPLICATES)**

* ✅ To'liq qatorli dublikatlar o'chirildi: 49
* ✅ Qolgan dublikatlar: 0

## **YETISHMAYOTGAN QIYMATLAR (MISSING VALUES)**

* ✅ Jami yetishmayotgan qiymatlar: 0

## **MA'LUMOTLAR SIFATI HOLATI**

* ✅ **CLEAN (TOZA):** Ma'lumotlar to'plami barcha validatsiya qoidalaridan o'tdi
* ✅ **READY (TAYYOR):** Ma'lumotlar to'plami feature engineering jarayoniga tayyor

## **KEYINGI QADAMLAR (BLOCK 2.3)**

1. `order_date` ustunidan feature engineering o'tkazish
2. Ixtiyoriy: Masofa toifalarini (distance categories) yaratish
3. Ixtiyoriy: Haroratni intervallarga bo'lish (temperature binning)
4. Modellashtirish pipeline-iga o'tish
