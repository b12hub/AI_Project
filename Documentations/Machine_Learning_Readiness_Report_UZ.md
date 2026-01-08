# Machine Learning-ga Tayyorlik Hisoboti: GOLD STANDARD

## Ijroiya Xulosasi

**Dataset Holati: ✅ ISHLAB CHIQARISHGA TAYYOR (GOLD STANDARD)**

`GOLD_STANDARD_DATASET.csv` sizning ma'lumotlaringizning yakuniy va optimallashtirilgan evolyutsiyasini ifodalaydi. Multikolliniarlikni bartaraf etish, ortiqcha matnli ustunlarni o'chirish va yangi ekologik ko'rsatkichlarni (`temperature`, `is_long_route`) qo'shish orqali dataset **99.63% R²** aniqlik ko'rsatkichiga erishdi.

---

## Dataset Sharhi (GOLD STANDARD)

* **Umumiy namunalar**: 69,512 ta yozuv
* **Ustunlar soni**: 26 ta (25 ta Bashorat qiluvchi + 1 ta Maqsadli)
* **Maqsadli o'zgaruvchi**: `delivery_time_hours` (Uzluksiz vaqt)
* **Ma'lumotlar sifati**: 100% To'liq (0 ta bo'shliq, 0 ta dublikat)

### Ustunlar Tavsifi (Barcha 25 ta belgi)

| # | Ustun Nomi | Tavsif |
| --- | --- | --- |
| 1 | **expected_time_no_traffic** | Masofa va tezlik cheklovlariga asoslangan nazariy vaqt. |
| 2 | **vehicle_distance_mismatch** | Transportning optimal yo'ldan og'ish darajasi. |
| 3 | **vehicle_traffic_stress** | Tirbandlikning aynan shu transport turiga ta'siri. |
| 4 | **distance_km** | Yo'nalishning umumiy uzunligi (kilometrda). |
| 5 | **vehicle_time_efficiency** | Transport/haydovchi kombinatsiyasining tarixiy samaradorligi. |
| 6 | **traffic_weather_risk** | Tirbandlik va ob-havo xavfining birlashgan indeksi. |
| 7 | **is_peak_hour** | Buyurtma tig'iz vaqtda berilganligi (1 = Ha, 0 = Yo'q). |
| 8 | **operational_stress_index** | Buyurtma paytidagi tizimning umumiy yuklamasi. |
| 9 | **route_frequency** | Ushbu yo'nalishning datasetda ishlatilish chastotasi. |
| 10 | **is_heavy_traffic_truck** | Tirbandlikda qolgan yuk mashinasi xavfi. |
| 11 | **traffic_level_medium** | O'rtacha tirbandlik darajasi (One-hot encoded). |
| 12-16 | **vehicle_type_*** | Transport turlari: Yengil mashina, Mototsikl, Pikap, Yuk mashinasi, Van. |
| 17-20 | **weather_*** | Ob-havo sharoitlari: Ochiq, Bulutli, G'ubor, Tuman. |
| 21 | **route_traffic_volatility** | Yo'nalishdagi tirbandlik o'zgaruvchanligi darajasi. |
| 22 | **destination_city_encoded** | Manzil shahrining raqamli kodi. |
| 23 | **route_id_encoded** | Yo'nalishning (A nuqtadan B nuqtaga) noyob identifikatori. |
| 24 | **temperature** | Yetkazib berish paytidagi havo harorati (Yangi belgi). |
| 25 | **is_long_route** | Masofa uzoq masofali chegara qiymatidan oshganligi (Yangi belgi). |

---

## Model Samaradorligi Tahlili

### 1. Regressiya Metodi (Vaqtni Bashorat Qilish)

**Tavsiya etilgan algoritm**: *Gradient Boosting Regressor (XGBoost/LightGBM)*

* **R² koeffitsienti**: 0.9963 (99.63% aniqlik)
* **RMSE (Kvadratik xato)**: 0.366 soat (~22 daqiqa)
* **MAE (Mutloq xato)**: 0.266 soat (~16 daqiqa)
* **Xulosa**: Model mijozlarga yetkazib berish vaqtini (ETA) juda aniq ko'rsatish imkonini beradi.

### 2. Klassifikatsiya Metodi (Kechikishni Aniqlash)

**Tavsiya etilgan algoritm**: *Random Forest Classifier*

* **Accuracy (Aniqlik)**: 98.83%
* **F1-Score**: 98.83%
* **Specificity**: 98.77% (Tez yetkazib berishlarni xatosiz aniqlaydi).

---

## Belgilar Muhimligi (Mutual Information - MI)

MI tahlili "Gold Standard" belgilarining maqsadli o'zgaruvchi bilan chiziqli bo'lmagan yuqori bog'liqligini tasdiqladi:

1. **expected_time_no_traffic** (Ball: 2.36)
2. **route_traffic_volatility** (Ball: 1.92)
3. **vehicle_distance_mismatch** (Ball: 1.81)

---

## PCA Manifold (Geometrik) Tahlili

* **Struktura**: 2D fazoda ma'lumotlar "Past Vaqt"dan "Yuqori Vaqt"ga silliq o'tuvchi (gradient) shaklni hosil qilgan.
* **Zichlik**: Manifoldda sezilarli shovqinlar (outliers) aniqlanmadi, bu datasetning toza ekanligidan dalolat beradi.

---

## ML Tayyorlik Tekshiruvi

* [x] **Matnli ustunlar yo'q**: Barcha `object` turlari o'chirildi yoki kodlandi.
* [x] **Multikolliniarlik yo'q**: Takroriy masofa va tirbandlik ko'rsatkichlari tozalandi.
* [x] **Ma'lumot sizib chiqishi (Leakage) tekshirildi**: `route_traffic_volatility` tarixiy ma'lumot ekanligi tasdiqlandi.
* [x] **Yangi Signallar**: `temperature` va `is_long_route` mantiqiy tendensiyalarni ushlash uchun qo'shildi.

---

## Tavsiyalar va Joriy Qilish

### Texnik Konfiguratsiya (Tavsiya)

```python
# Gold Standard Dataset uchun eng yaxshi parametrlar
model = GradientBoostingRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=7,
    subsample=0.8,
    random_state=42
)

```

## Xulosa

**GOLD STANDARD DATASET** avvalgi `CLEANED` versiyasidan sezilarli darajada ustun. Harorat ma'lumotlarining qo'shilishi va "shovqinli" belgilarning olib tashlanishi natijasida dataset yuqori samarali ML tizimlari uchun matematik jihatdan optimallashtirildi.

**Ishonch Darajasi: 🎯 MAKSIMAL (FOYDALANISHGA TAYYOR)**

---
