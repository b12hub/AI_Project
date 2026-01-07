# 🧠 Feature Engineering Hisoboti

## Xavfni hisobga oluvchi yetkazib berish vaqtini bashorat qilish uchun ishlab chiqarish darajasidagi (Production-Grade) Feature Arxitexturasi

---

## 1. Maqsad va pozitsiyalash

Ushbu hisobot loyihaning **Feature Engineering bosqichini** hujjatlashtiradi, bu butun pipeline-ning **asosiy intellekt qatlami** hisoblanadi.

Agar ma'lumotlarni tozalash (data cleaning) *to'g'rilikni* va tahlil (analysis) *tushunishni* ta'minlasa,

**feature engineering ishlab chiqarish sharoitida yashovchanlikni (survivability) ta'minlaydi**.

Maqsad qisqa muddatli aniqlikni maksimal darajaga ko'tarish emas, balki quyidagilarga qodir bo'lgan **mustahkam, leakage-free va xavfni hisobga oluvchi feature fazosini** qurish edi:

* Real operatsion xatti-harakatlarni kodlash
* Vaqt va yo'nalishlar bo'yicha umumlashtirish (generalize)
* Taqsimot siljishi (distribution drift) sharoitida barqaror qolish
* Modellar va kelajakdagi dataset-lar o'rtasida xavfsiz qayta ishlatilish

Ushbu bosqichda feature-larga eksperiment artefaktlari emas, balki **infrastruktura** sifatida qaraladi.

---

## 2. Feature Engineering falsafasi

Barcha feature-lar ustidagi ishlar beshta qat'iy muhandislik tamoyillariga asoslandi:

### 2.1 Vaqt bo'yicha xavfsizlik (Zero Leakage)

* Hech bir feature buyurtma berilgan vaqtda mavjud bo'lmagan ma'lumotlardan foydalanishi mumkin emas.
* Forward aggregation, rolling target statistics yoki yetkazib berishdan keyingi signallar (post-delivery signals) ishlatilmaydi.
* Barcha guruh statistikasi **tarixiy jihatdan xavfsiz oynalar** (historically safe windows) yordamida hisoblanadi.

> Metrikalarni "aldash" (cheating) orqali yaxshilaydigan har qanday feature, natija qanchalik yuqori bo'lishidan qat'i nazar, rad etiladi.

---

### 2.2 Operatsion interpretativlik (Tushunarlilik)

Har bir feature **real dunyo mexanizmiga** mos kelishi shart:

* Tirbandlik (Traffic congestion)
* Transport vositasi cheklovlari
* Yo'nalish beqarorligi (Route instability)
* Atrof-muhit stresi

Agar feature operatsion menejerga tushuntirib berilmasa, u xavfli deb hisoblanadi.

---

### 2.3 Ordinal yolg'onlarning yo'qligi (No Ordinal Lies)

Kategorik holatlar (tirbandlik, ob-havo, transport turlari) **raqamli kattaliklar emas**.

* "Medium traffic" (o'rtacha tirbandlik) "Low" va "High" o'rtasidagi yarim yo'l emas.
* "Truck" (yuk mashinasi) "Van"dan chiziqli ravishda og'irroq emas.

Soxta chiziqlilikni (linearity) yuklaydigan joylarda ordinal encoding-dan qasddan voz kechildi.

---

### 2.4 Entropiyadan xabardorlik (Entropy Awareness)

Quyidagi xususiyatlarga ega feature-lar:

* Nolga yaqin variatsiya (Near-zero variance)
* Doimiy xatti-harakat (Constant behavior)
* Permutation importance-ning yo'qligi

shunchaki o'chirib tashlanmadi, balki audit qilish imkoniyati uchun **hujjatlashtirildi**.

---

### 2.5 O'rtacha qiymatni optimallashtirishdan ko'ra xavfga sezgirlik

Logistika tizimlarining muvaffaqiyatsizligi o'rtacha qiymatda emas, balki **taqsimot chekkalarida (tails)** sodir bo'ladi.

Feature dizayni quyidagilarga qaratilgan:

* Volatillik (Volatility)
* Shartli muvaffaqiyatsizlik rejimlari (Conditional failure modes)
* Asimmetrik xato xarajatlari (kechikish > erta yetkazib berish)

---

## 3. Feature Engineering arxitekturasi sharhi

Feature-larni ishlab chiqish **ko'p bosqichli bloklarda** amalga oshirildi, ularning har biri alohida signal qatlamini qo'shdi:

| Qatlam | Fokus | Maqsad |
| --- | --- | --- |
| Temporal | Vaqt dinamikasi | Uzilishlarsiz davriylik |
| Spatial | Yo'nalish intellekti | Tarixiy yo'nalish xatti-harakati |
| Operational | Transport va muhit | Shartli stressni kodlash |
| Risk-Aware | Volatillik va o'zaro ta'sirlar | Tail-riskni kamaytirish |
| Stability | Feature yashovchanligi | Drift-ga tayyorgarlik |

Har bir bosqich kuzatuvchanlikni (traceability) ta'minlash uchun **materializatsiya qilingan dataset versiyasini** taqdim etdi.

---

## 4. Bosqich 2.3.1 — Temporal Signal Encoding

**Notebook:** `Feauture_Engineering_BLOCK-2.3.1.ipynb`

### 4.1 Motivatsiya

Vaqt chiziqli emas, balki siklikdir:

* 23-soat 12-soatga qaraganda 0-soatga yaqinroq.
* Mavsumiy naqshlar takrorlanadi.

Sodda kodlashlar (naive encodings) modellarni chalg'itadigan sun'iy uzilishlarni (discontinuities) keltirib chiqaradi.

---

### 4.2 Amalga oshirilgan feature-lar

#### Siklik kodlashlar (Cyclic Encodings)

* Kun soati → `sin(hour)`, `cos(hour)`
* Oy → `sin(month)`, `cos(month)`

Ushbu usul feature fazosida **burchakli uzviylikni** (angular continuity) saqlaydi.

#### Binar Temporal Flag-lar

* Dam olish kuni indikatori (Weekend indicator)
* Tungi yetkazib berish indikatori
* Tig'iz vaqt (Peak traffic) oynasi flag-lari

---

### 4.3 Natija

* Temporal tekislik (smoothness) yaxshilandi.
* Chegaraviy artefaktlar kamaydi.
* Modellarga davriy xatti-harakatlarni tabiiy ravishda o'rganish imkonini berdi.

Hech bir bosqichda target ma'lumotlaridan foydalanilmadi.

---

## 5. Bosqich 2.3.2 — Fazoviy va yo'nalishli intellekt (Spatial & Route Intelligence)

**Notebook:** `Spatial_Feature_Engineering.ipynb`

### 5.1 Motivatsiya

Faqat masofaning o'zi yetkazib berish xarakterini belgilamaydi.

Bir xil uzunlikdagi ikkita yo'nalish quyidagilar sababli keskin farq qilishi mumkin:

* Infratuzilma sifati
* Shahar zichligi
* Tarixiy tirbandlik naqshlari

---

### 5.2 Yaratilgan fazoviy feature-lar

* `route_id` (kelib chiqish → manzil)
* Yo'nalish chastotasi (tarixiy foydalanish)
* Yo'nalish darajasidagi o'rtacha masofa
* Uzoq masofali yo'nalish indikatori (Long-haul)
* Yo'nalish o'rtacha qiymatiga nisbatan normallashtirilgan masofa

Barcha statistika **forward-looking leakage-siz** hisoblandi.

---

### 5.3 Asosiy dizayn cheklovi

Hech bir yo'nalish feature-i quyidagilarni ishlatmaydi:

* Yetkazib berish vaqti (Delivery time)
* Kelajakdagi kuzatuvlar
* Target leakage proksi-lari

Yo'nalish feature-lari natijalarni emas, balki **strukturaviy geografiyani** kodlaydi.

---

### 5.4 Natija

* "Barqaror" va "mo'rt" (fragile) yo'nalishlarni farqlash imkoniyati yaratildi.
* Tarixiy jihatdan volatil bo'lgan yo'llarda haddan tashqari ishonchni (overconfidence) kamaytirdi.
* Ko'rilmagan namunalarda (unseen samples) umumlashtirish yaxshilandi.

---

## 6. Bosqich 2.3.3 — Operatsion va transport vositalarining o'zaro ta'siri

**Notebook:** `Operational_&_Vehicle_Interaction_FE.ipynb`

### 6.1 Motivatsiya

Transport vositalari atrof-muhitga bir xil javob bermaydi.

Masalan:

* Yuk mashinalari (trucks) tirbandlikda keskin samaradorlikni yo'qotadi.
* Ob-havo yengil transport vositalariga (light vehicles) ko'proq ta'sir qiladi.
* Masofa stresi transport vositasining mosligiga bog'liq.

Bular mustaqil o'zgaruvchilar emas, balki **o'zaro ta'sir effektlari** (interaction effects) hisoblanadi.

---

### 6.2 Yaratilgan Interaction signallari

* Transport vositasi × masofa muvofiqligi
* Transport vositasi × tirbandlik stress indikatorlari
* Transport vositasi × ob-havo sezgirligi flag-lari
* Kompozit operatsion stress indekslari

Ushbu feature-lar modellarga o'rtacha ko'rsatkichlarni emas, balki **shartli fizikani** (conditional physics) o'rganish imkonini beradi.

---

### 6.3 Natija

* Chiziqli bo'lmagan operatsion xatti-harakatlar aniqlandi.
* Og'ir transport vositalari uchun tizimli kam baholash (underestimation) kamaydi.
* Aralash tirbandlik sharoitida mustahkamlik yaxshilandi.

---

## 7. Maqsadli ishlab chiqarish darajasidagi (Production-Grade) yaxshilanishlar

Xatolar diagnostikasidan so'ng, uchta **yuqori ta'sirli arxitektura yangilanishlari** kiritildi.

---

### 7.1 Yo'nalishga xos tirbandlik volatilligi (Route-Specific Traffic Volatility)

**Feature:** `(route_id, traffic_level)` bo'yicha guruhlangan yetkazib berish vaqtining standard deviation-i.

#### Asoslantirish

O'rtacha harakatlanish vaqti xavfni yashiradi.
Ba'zi yo'nalishlar ma'lum bir tirbandlik sharoitida tabiatan beqarordir.

#### Ta'sir

* O'tkazib yuborilgan kechikishlar (Type II errors) kamaydi.
* Recall **96.6%** gacha yaxshilandi.
* Model faqat kutilmani emas, balki **noaniqlikni** (uncertainty) o'rgandi.

---

### 7.2 Og'ir transport vositasi × Tirbandlik o'zaro ta'siri flag-i

**Feature:** `is_heavy_traffic_truck`

#### Asoslantirish

Empirik diagnostika shuni ko'rsatdiki, yuk mashinalari o'rtacha tirbandlikda **~30% yuqori xato darajasiga** ega edi.
Ushbu interaction (o'zaro ta'sir) modelning o'zi xulosa qilishini kutmasdan, aniq kodlandi.

#### Ta'sir

* False negatives (noto'g'ri salbiy natijalar) **29%** ga kamaydi.
* Tirbandlik sharoitida bashorat qilish xavfsizligi oshdi.

---

### 7.3 Yuqori aniqlikdagi (High-Fidelity) One-Hot Encoding

Quyidagilarga qo'llanildi:

* Traffic level
* Vehicle type
* Weather conditions

#### Nima uchun

Ordinal encoding noto'g'ri raqamli munosabatlarni yuklagan edi.

One-hot encoding quyidagilarga imkon beradi:

* Mustaqil vazn (weighting) berish
* Chiziqli bo'lmagan qaror chegaralari (nonlinear decision boundaries)
* Tozaroq tree splits (daraxt kesimlari)

#### Ta'sir

* Accuracy **94.3%** da barqarorlashdi.
* Modelning "mo'rtligi" (brittleness) kamaydi.
* Cross-split (bo'linishlararo) izchillik yaxshilandi.

---

## 8. Feature Selection, barqarorlik va Drift-ga tayyorgarlik

**Notebook:** `Feature_Stability_and_Drift_Readiness_analysis.ipynb`

### 8.1 Metodologiya

* Vaqtga asoslangan (time-aware) 80/20 split
* Gradient Boosting Regressor
* **Held-out ma'lumotlarda** permutation importance tahlili
* Ichki importance metrikalari bilan o'zaro tekshirish

---

### 8.2 Hujjatlashtirilgan past qiymatli feature-lar

Quyidagi feature-lar:

* Nolga yaqin entropiya
* Permutation signalining yo'qligi
* Barqarorlikka hissa qo'shmaslik ko'rsatkichlarini namoyish etdi.

O'chirilmagan, balki hujjatlashtirilgan (audit uchun):

* `night_peak_conflict`
* `is_return_route`
* `route_std_distance`
* `city_pair_complexity`

Bu **audit qilinuvchanlik va ilmiy halollikni** saqlaydi.

---

### 8.3 Drift-ga tayyorgarlik

* Feature taqsimotlari vaqt bo'yicha tahlil qilindi.
* Dominant signallar barqarorligi tekshirildi.
* Masofadan kelib chiqqan feature-lar uchun proksi-xavflar hujjatlashtirildi.

---

## 9. Yakuniy feature fazosi xarakteristikalari

### Dataset xulosasi

* ~70,000 yozuv
* ~28 ta yuqori signalli feature-lar
* Yetishmayotgan qiymatlar mavjud emas
* Vaqt bo'yicha xavfsiz (Time-safe)
* Model-agnostik

### Feature kategoriyalari

* Temporal (siklik, kategorik)
* Spatial (yo'nalishni hisobga oluvchi)
* Operational (transport va muhit)
* Risk-aware (volatillik va o'zaro ta'sirlar)

---

## 10. Ushbu bosqichda erishilgan natijalar

Ushbu feature engineering bosqichi datasetni quyidagidan:

> **"O'rtacha yetkazib berish vaqtini bashorat qilish"**

quyidagiga aylantirdi:

> **"Operatsion xavfni aniq hisobga olgan holda yetkazib berish vaqtini baholash."**

U quyidagilarni o'rnatdi:

* Feature-lar qonuniyligi (legitimacy)
* Leakage-ga immunitet
* Operatsion realizm
* Ishlab chiqarishda yashovchanlik (production survivability)

---

## 11. Yakuniy bayonot

Modellar o'zgaradi.

Algoritmlar rivojlanadi.

Metrikalar tebranadi.

**Tartibga solingan feature fazosi - bu vaqt o'tishi bilan qiymati ortib boradigan yagona aktivdir.**

---
