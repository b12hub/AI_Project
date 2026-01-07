# Ma'lumotlarni profillash va "Sanity Check" hisoboti - TUZATILGAN

## Transport va logistika ma'lumotlar to'plami (Dataset)

**Sana:** 2026-01-05

**Dataset:** `raw_data.csv` (69,975 qator × 12 ustun)

**Target Variable:** `delivery_time_hours`

---

## Executive Summary

Transport va logistika ma'lumotlar to'plami barcha bashorat qiluvchi feature-lar bo'yicha to'liq ma'lumotlar, haqiqiy diapazonlar va mantiqiy izchillik bilan **yuqori sifat xarakteristikalarini** namoyish etadi. Ma'lumotlar to'plamida machine learning modelini ishlab chiqishda foydalanishga to'sqinlik qiladigan **hech qanday kritik muammo mavjud emas**.

Takroriy `order_id` qiymatlarining mavjudligi (74.9% takrorlanish darajasi) ML ilovalari uchun **muammo emas**, chunki sintetik identifikatorlar dizayn bo'yicha modellashtirish jarayonidan chiqarib tashlanadi. Ushbu holat shunchaki identifikatorlarni yaratish jarayoni turli buyurtmalar uchun identifikatorlarni qayta ishlatishini ko'rsatadi, bu logistika tizimlarida keng tarqalgan va modelni o'qitish yoki baholashga hech qanday ta'sir ko'rsatmaydi.

**Tavsiya:** Ma'lumotlar to'plami standart preprocessing bosqichlaridan (bashorat qilmaydigan identifikatorlarni olib tashlash va feature engineering) so'ng **ML uchun MUVOFIQ**.

---

## Key Findings (Asosiy topilmalar)

### ✅ **Ijobiy jihatlar**

1. **To'liq ma'lumotlar**: Hech bir ustunda yetishmayotgan qiymatlar mavjud emas (100% to'liqlik).
2. **Haqiqiy diapazonlar**: Barcha raqamli qiymatlar kutilgan diapazonlarda:
* Manfiy yetkazib berish vaqti yoki masofalar mavjud emas.
* Buyurtma soatlari to'g'ri chegaralangan (0-23).
* Harorat oralig'i oqilona (-4°C dan 7.2°C gacha).


3. **Mantiqiy izchillik**: Kelib chiqish va manzil shaharlari bir xil bo'lgan buyurtmalar mavjud emas.
4. **Muvozanatli taqsimotlar**: Kategorik o'zgaruvchilarda oqilona muvozanat mavjud.
* Vehicle types: har biri 19.8%-20.1% dan.
* Traffic levels: 76.2% Low, 23.8% Medium.


5. **Toza Target Variable**: Past outlier foizi (0.24%).
6. **Muvofiq sana oralig'i**: To'g'ri datetime formatidagi 61 kunlik davr.

### ⚠️ **Kichik kuzatuvlar**

1. **Harorat taqsimoti**: 20.1% manfiy haroratlar (qishki ma'lumotlar).
2. **Target Skewness**: O'rtacha o'ngga og'ish (0.6551) - yetkazib berish vaqtlari uchun normal holat.
3. **Yuqori o'zgaruvchanlik**: CV = 65.94% turli xil yetkazib berish ssenariylarini ko'rsatadi.

---

## Data Quality Assessment (Sifat bahosi)

### Dataset strukturasi

* **Qatorlar:** 69,975
* **Ustunlar:** 12
* **Numerical Features:** 4 (`distance_km`, `order_hour`, `temperature`, `delivery_time_hours`)
* **Categorical Features:** 7 (`order_id` dan tashqari)

### Ma'lumotlar sifati metrikalari

| Metrika | Qiymat | Holat |
| --- | --- | --- |
| Missing Values | 0 | ✅ A'lo |
| Duplicate Rows | 0 | ✅ Yaxshi |
| Invalid Values | 0 | ✅ A'lo |
| Outliers (Target) | 171 (0.24%) | ✅ Qabul qilinarli |

---

## Target Variable Analysis

### Taqsimot xarakteristikalari

* **Mean:** 9.15 soat
* **Median:** 8.05 soat (o'ngga og'ish tasdiqlandi)
* **Standard Deviation:** 6.04 soat
* **Range:** 0.83 - 29.84 soat
* **Coefficient of Variation:** 65.94%

### Outlier-lar tahlili

* **IQR metodi:** 171 ta outlier (0.24%) - juda past.
* **Z-score metodi:** 243 ta outlier (0.35%) - qabul qilinarli.
* **Outlier oralig'i:** 27.76 - 29.84 soat (ekstremal emas).

---

## Red Flags xulosasi

### Kritik muammolar (tuzatilishi shart)

**Hech qanday muammo aniqlanmadi.**

### Bashorat qilmaydigan identifikatorlar

1. **order_id** - Takrorlanuvchi sintetik identifikator.
* **Holat:** Ta'rifi bo'yicha bashorat qilmaydi.
* **Harakat:** Modellashtirish pipeline-dan chiqarib tashlash.
* **Ta'sir:** Model ishlashiga (performance) ta'sir qilmaydi.



---

## BLOCK 2.2 uchun tavsiyalar

### Zudlik bilan talab qilinadigan harakatlar

1. **Standart Preprocessing**
```python
# Bashorat qilmaydigan identifikatorni olib tashlash
df = df.drop('order_id', axis=1)

```


2. **Feature Engineering**
* `order_date` ustunidan temporal feature-larni ajratib olish (`day_of_year`, `is_weekend`, va h.k.).
* `distance_km` dan masofa toifalarini (bins) yaratish.
* Ob-havo ta'sirini tahlil qilish uchun harorat bin-larini ko'rib chiqish.



---

## Texnik baholash

### ML uchun muvofiqlik

* **Joriy holat:** ✅ **MUVOFIQ**
* **Dataset sifat ko'rsatkichi:** **9/10** (A'lo)

### Kutilayotgan ML natijalari

* **Bazaviy kutilma:** Yaxshi natijalar kutilmoqda.
* **Feature Importance:** Masofa, transport turi va temporal feature-lar ustunlik qilishi mumkin.
* **Model muvofiqligi:** Robust regression modellari (Random Forest, XGBoost, Neyron tarmoqlari).

---

## Xulosa

Ushbu logistika ma'lumotlar to'plami machine learning ilovalari uchun **alohida sifatga** ega. `order_id` takrorlanishi ma'lumotlar yaxlitligiga ta'sir qilmaydigan tizimli artefakt xolos.

**Zudlik bilan amalga oshiriladigan keyingi qadamlar:**

1. `order_id` ustunini drop qilish.
2. `order_date` dan vaqtga oid (temporal) feature-larni yaratish.
3. Standart ML pipeline ishlab chiqishni boshlash.

---

## Appendices (Ilovalar)

### A. Ustunlar ta'riflari

| Ustun | Tur | Rol | Tavsif |
| --- | --- | --- | --- |
| **order_id** | Object | Identifier | Buyurtma identifikatori (modellashtirishdan chiqarib tashlang) |
| **origin_city** | Object | Feature | Kelib chiqish shahri |
| **distance_km** | Float64 | Feature | Masofa kilometrlarda |
| **traffic_level** | Object | Feature | Tirbandlik darajasi (Low/Medium) |
| **delivery_time_hours** | Float64 | **Target** | Yetkazib berish vaqti soatlarda |

---
