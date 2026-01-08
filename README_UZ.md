# 🚚 Risk-Aware Logistics Delivery Time Dataset

### Ishlab chiqarish darajasidagi (Production-Grade) Feature Engineering, Validatsiya va Audit Pipeline-i

> **Tezis** > Ushbu repozitoriy amaliy machine learning-ning asosiy tamoyilini hayotga tatbiq etadi:
> **modellar algoritmlar tufayli emas, balki ma'lumotlar to'plami noto'g'ri bo'lgani uchun muvaffaqiyatsizlikka uchraydi.** >
> Ushbu loyiha xom logistika ma'lumotlarini **risk-aware (xavfni hisobga oluvchi), leakage-free (sizishsiz), audit qilinadigan va modelga tayyor** ma'lumotlar to'plamiga aylantiradi. U leaderboard demolari uchun emas, balki *haqiqiy operatsion noaniqliklar* uchun maxsus ishlab chiqilgan.

---

## 📌 Executive Summary (Qisqacha xulosa)

Yetkazib berish vaqtini bashorat qilish bu shunchaki oddiy vanilla regression vazifasi **emas**.

Haqiqiy logistika tizimlarida:

* Xatolar **asimmetrikdir**
* Kechikishlar operatsion xavfni kuchaytiradi
* Yo'nalishlar (routes) non-stationary xarakterga ega
* Transport vositalari tirbandlik bilan chiziqli bo'lmagan (non-linear) usullarda o'zaro ta'sir qiladi
* Temporal leakage modellar natijasini soxta ravishda yaxshilab ko'rsatadi

Ushbu loyiha modelga yo'naltirilgan eksperiment emas, balki **dataset-first ML foundation** (ma'lumotlarga asoslangan ML poydevori) qurish orqali ushbu realliklarni hal qiladi.

### Ushbu repozitoriy nimalarni taqdim etadi

✔ Ko'p bosqichli **data cleaning & validation pipeline** ✔ **Leakage-audited feature engineering framework** ✔ Yo'nalish, transport vositasi va xavfni hisobga oluvchi feature-lar

✔ Aniq dataset lineage (nasabnomasi) va versiya nazorati

✔ **Model-agnostik, ishlab chiqarish uchun xavfsiz ma'lumotlar to'plami** ### Nimadan qasddan voz kechilgan

✖ Modellarni muddatidan oldin optimallashtirish

✖ Deployment-ga xos taxminlar

✖ Dashboard-ga yo'naltirilgan overfitting

> **Natija:** > Yetkazib berish vaqtini bashorat qilishni *o'rtacha hisoblashdan* (average estimation), **noaniqlik sharoitida xavfni hisobga oluvchi prognozlashga** (risk-aware forecasting) o'tkazadigan ma'lumotlar to'plami.

---

## 🎯 Muammoning tarifi va tizim konteksti

### Operatsion reallik

Logistikada bashorat qilish xatolari **asimmetrikdir**:

| Ssenariy | Biznesga ta'siri |
| --- | --- |
| Erta yetkazib berish | Kichik samarasizlik |
| Kech yetkazib berish | SLA buzilishi, ishonch yo'qolishi, xarajatlarning keskin oshishi |

Aksariyat ML pipeline-lar **mean error**-ni optimallashtiradi, logistika tizimlari esa **tails** (taqsimot chekkalarida) muvaffaqiyatsizlikka uchraydi.

Ushbu loyiha yetkazib berish vaqtini bashorat qilishni sof statistik mashq emas, balki **risk-sensitive regression problem** (xavfga sezgir regressiya muammosi) sifatida qayta belgilaydi.

---

### Tizimning asosiy qiyinchiliklari

| Qiyinchilik | Nima uchun sodda modellarni ishdan chiqaradi |
| --- | --- |
| Traffic | Categorical label-lar chiziqli bo'lmagan xatti-harakatlarni yashiradi |
| Vehicles | Tirbandlikda har xil dinamikaga ega bo'lishi |
| Routes | Tarixiy beqarorlik va variance |
| Time | Leakage oflayn metrikalarni sun'iy ravishda oshiradi |
| Encoding | Ordinal taxminlar soxta signallarni yuzaga keltiradi |

Ma'lumotlar to'plami elektron jadvaldagi korrelyatsiyalarni emas, balki **operatsion fizikani** (operational physics) kodlashi kerak.

---

### Target Variable (Maqsadli o'zgaruvchi)

* **`delivery_time_hours`**
* Uzluksiz regressiya nishoni
* Faqat RMSE bilan emas, balki **risk awareness** bilan baholanadi

> Maqsad "eng yaxshi o'rtacha bashorat" emas,
> balki **operatsion stress ostida mustahkam va asosli natijadir**.

---

## 🧭 Loyiha ko'lami va aniq chegaralar

### Ko'lamga kiritilgan

✅ Xom ma'lumotlarni qabul qilish va audit qilish

✅ Strukturaviy va mantiqiy tozalash (cleaning)

✅ Ko'p bosqichli feature engineering

✅ Leakage va temporal validatsiya

✅ Feature stability va drift readiness

✅ Yakuniy ma'lumotlar to'plamini shakllantirish

### Ko'lamdan tashqarida

❌ Model deployment pipeline-lari

❌ Real-time inference tizimlari

❌ Monitoring yoki alerting dashboard-lari

> Ushbu ajratish modellar va jamoalar o'rtasida **dataset portability (ko'chuvchanligi), auditability (tekshiriluvchanligi) va uzoq muddatli qayta foydalanishni** ta'minlaydi.

---

## 🗂 Repozitoriy strukturasi

```map
├── Dataset/
│   ├── raw_data.csv
│   ├── clean_data_v1.csv
│   ├── clean_data_v2.csv
│   ├── feature_data_v1.csv
│   ├── feature_data_v2.csv
│   ├── feature_data_v3.csv
│   ├── feature_data_v4.csv
│   ├── final_dataset.csv
    ├── final_dataset_CLEANED.csv
│   └── model_ready_data.csv
│
├── Data_Cleaning.ipynb
├── Data_Quality_Validation.ipynb
├── Data_Analsis.ipynb
├── Leakage_and_Temporal_Audit.ipynb
├── Spatial_Feature_Engineering.ipynb
├── Operational_&_Vehicle_Interaction_FE.ipynb
├── Feature_Stability_and_Drift_Readiness_analysis.ipynb
├── Baseline_Modeling_and_Error_Diagnostics.ipynb
├── Prediction_Intervals_and_Calibration.ipynb
│
├── Documentations/
│   ├── Cleaning_Report.md
│   └── Analysis_Report.md
│
└── Visualizations/
    ├── comparison_analysis.png
    └── data_quality_viz.png

```

---

## 📥 Raw Dataset Overview

**Source Artifact:** `raw_data.csv`

### Core Raw Attributes (Representative)

* `origin_city`
* `destination_city`
* `distance_km`
* `vehicle_type`
* `traffic_level`
* `weather`
* `order_date`
* `delivery_time_hours`

### Known Raw Dataset Limitations

Xom ma'lumotlar to'plami qasddan ishonchsiz deb hisoblanadi:

* **Temporal ordering** (vaqt ketma-ketligi) kafolatlanmagan.
* **Categorical variables** noto'g'ri tartibni (ordinality) ko'rsatishi mumkin.
* **Routes** tarixni bitta qiymatga birlashtiradi.
* **Risk signals** butunlay mavjud emas.
* **Leakage potential** sezilarli darajada mavjud.

> [!CAUTION]
> **Xulosa:** Xom ma'lumotlar sukut bo'yicha model uchun xavfsiz emas va foydalanishdan oldin audit qilinishi kerak.

---

## 📥 Dataset Lineage & Versioning Strategy

Ushbu loyiha ma'lumotlar to'plamining qat'iy immutability (o'zgarmaslik) va versiyalash qoidalariga amal qiladi. Har bir transformatsiya bosqichi yangi dataset yaratadi, dastlabki artefaktlarni saqlaydi va to'liq orqaga qarab kuzatishni (traceability) ta'minlaydi.

### Dataset Evolution Pipeline

| Stage | Artifact | Purpose |
| --- | --- | --- |
| **Raw Ingestion** | `raw_data.csv` | Tegilmagan manba |
| **Cleaning v1** | `clean_data_v1.csv` | Schema va null qiymatlar bilan ishlash |
| **Cleaning v2** | `clean_data_v2.csv` | Mantiqiy validatsiya |
| **Feature v1** | `feature_data_v1.csv` | Temporal asoslar |
| **Feature v2** | `feature_data_v2.csv` | Fazoviy va yo'nalishli kontekst |
| **Feature v3** | `feature_data_v3.csv` | Operatsion o'zaro ta'sirlar |
| **Feature v4** | `feature_data_v4.csv` | Risk-aware boyitish |
| **Final** | `final_dataset.csv` | Audit qilingan va hujjatlashtirilgan |
| **Model-Ready** | `model_ready_data.csv` | Kodlangan (encoded) va tanlashga tayyor |

### Nima uchun bu muhim

Ushbu lineage quyidagilarga imkon beradi:

1. Feature regression tahlili
2. Model xatolarining sababini aniqlash (attribution)
3. Takrorlanuvchi eksperimentlar
4. Ishlab chiqarishda xavfsiz orqaga qaytarish (rollback)

---

## 🧼 Data Cleaning & Structural Validation

### Maqsad

Har qanday model taxminlarini kiritishdan oldin, xom logistika yozuvlarini strukturaviy jihatdan to'g'ri va mantiqiy izchil ma'lumotlar to'plamiga aylantirish.

### Cleaning prinsiplari

Tozalash ishlari qasddan konservativ tarzda amalga oshirildi:

* Target-aware filtering o'tkazilmagan
* Statistik smoothing qo'llanilmagan
* Qatorlarni agressiv o'chirish bo'lmagan
* Feature-larni barvaqt qisqartirish (pruning) bo'lmagan

### Asosiy cleaning harakatlari

* [x] Qat'iy sxemalar va dtypes o'rnatildi
* [x] Temporal field-lar validatsiya qilindi
* [x] Kategorik lug'atlar (vocabularies) normallashtirildi
* [x] Imkonsiz masofalar olib tashlandi
* [x] City-pair (shahar juftligi) muvofiqligi tekshirildi

Har bir tozalash bosqichi qaytarilishi mumkin, hujjatlashtirilgan va audit qilinadigan holatda.

### Artefaktlar

* `Data_Cleaning.ipynb`
* `Data_Quality_Validation.ipynb`
* `Documentations/Cleaning_Report.md`

---

## 🔍 Exploratory Analysis & Error Surface Mapping

### Maqsad

Sodda yetkazib berish modellari nafaqat qanchalik yaxshi natija berishini, balki qayerda va nima uchun muvaffaqiyatsizlikka uchrashini aniqlash.

### Asosiy kuzatuvlar

* **Error distributions** (xatolar taqsimoti) heavy-tailed (og'ir dumli) xarakterga ega.
* **Medium traffic** kutilmagan kechikish portlashlarini ko'rsatadi.
* **Certain routes** (ayrim yo'nalishlar) doimiy volatillikni namoyish etadi.
* **Distance** bazaviy vaqtni tushuntiradi, lekin kechikish xavfini emas.

### Strategik tushuncha

> O'rtacha xatoni optimallashtirish operatsion muvaffaqiyatsizliklarni yashiradi. Logistika tizimlari taqsimotning chekkalarida (tails) buziladi. Feature engineering aynan o'sha yerga e'tibor qaratishi kerak.

### Artefaktlar

* `Data_Analsis.ipynb`
* `Baseline_Modeling_and_Error_Diagnostics.ipynb`

---

## 🧠 Feature Engineering Framework (Dizayn doktrinasi)

Barcha feature engineering to'rtta qat'iy qoidaga amal qiladi:

1. **Zero Temporal Leakage**

* Kelajakdagi ma'lumotlarni agregatsiya qilish yo'q
* Yetkazib berishdan keyingi statistika yo'q

2. **No Ordinal Lies**

* Kategorik o'zgaruvchilar kategorik sifatida qaraladi
* Sun'iy chiziqlilik (linearity) yaratish yo'q

3. **No Low-Entropy Pollution**

* Foydasiz (dead) feature-lar yashirilmaydi, balki hujjatlashtiriladi

4. **Operational Interpretability**

* Har bir feature real mexanizmga mos kelishi kerak

**Eslatma:** Agar feature operatsion jihatdan tushuntirib berilmasa, u to'plamda bo'lishga haqli emas.

---

## 🧱 Feature Engineering — Bosqichma-bosqich tahlil

Ushbu loyiha **ko'p bosqichli, qat'iy audit qilingan feature engineering strategiyasini** qo'llaydi.

Har bir bosqich *orthogonal signal* kiritadi va quyi oqimga (downstream) o'tkazilishidan oldin alohida validatsiya qilinadi.

Feature engineering-ga feature-larni yig'ish emas, balki **tizim dizayni** (system design) sifatida qaraladi.

---

### Bosqich 2.3.1 — Temporal Signal Encoding

**Notebook:** `Feauture_Engineering_BLOCK-2.3.1.ipynb`

Xom vaqt belgilari (timestamps) **bevosita model tomonidan ishlatib bo'lmaydi**. Soat yoki oyni sodda tarzda ajratib olish sun'iy uzilishlarni keltirib chiqaradi (masalan, 23 → 0).

Buning oldini olish uchun vaqt **cyclical structure** sifatida kodlanadi va davriy uzviylik saqlab qolinadi.

#### Amalga oshirilgan feature-lar

* Sutka soati cyclic encoding (`sin`, `cos`)
* Yil oyi cyclic encoding
* Dam olish kuni indikatorlari (weekend indicators)
* Tungi operatsiyalar flag-lari
* Tig'iz payt tirbandligi markerlari

#### Dizayn maqsadi

* Temporal davriylikni saqlash
* Ordinal leakage-dan qochish
* Modellarga vaqt yorliqlarini emas, balki **vaqt ritmlarini** o'rganishga imkon berish

> Operatsiyalarda vaqt chiziqli emas. Ushbu kodlashlar modellarga soatni shunchaki o'qishdan ko'ra, uni "his qilish" imkonini beradi.

---

### Bosqich 2.3.2 — Fazoviy va yo'nalishli intellekt (Spatial & Route Intelligence)

**Notebook:** `Spatial_Feature_Engineering.ipynb`

Logistika tizimlari alohida safarlar bilan emas, balki **xotiraga ega yo'nalishlar** bilan ishlaydi.

Ushbu bosqich qat'iy leakage nazoratini saqlagan holda **route-aware context** kiritadi.

#### Yaratilgan konstruksiyalar

* `route_id` (kelib chiqish-manzil abstraksiyasi)
* Yo'nalish chastotasi hisoblagichlari (frequency counts)
* Yo'nalish darajasidagi o'rtacha masofa
* Uzoq masofali yo'nalish indikatorlari

#### Leakage-dan himoya

Barcha yo'nalish statistikasi quyidagicha hisoblanadi:

* Faqat **tarixiy ma'lumotlardan** foydalangan holda
* Joriy buyurtmaning target qiymatiga kirmagan holda
* Kelajakka qaratilgan agregatsiyalarsiz

> Yo'nalish intellekti bashorat emas, *kontekst* beradi.

---

### Bosqich 2.3.3 — Operatsion va transport vositalarining o'zaro ta'siri

**Notebook:** `Operational_&_Vehicle_Interaction_FE.ipynb`

Yetkazib berishdagi muvaffaqiyatsizliklarning aksariyati bitta o'zgaruvchi tufayli emas, balki **o'zaro ta'sirlar** (interactions) tufayli sodir bo'ladi.

Ushbu bosqich transport vositalarining **maxsus operatsion stressorlar** ostida o'zini qanday tutishini kodlaydi.

#### Interaction o'lchovlari

* Transport vositasi × masofa muvofiqligi
* Transport vositasi × tirbandlikka javob reaksiyasi
* Transport vositasi × ob-havo sezgirligi
* Kompozit operatsion stress indekslari

#### Nima uchun bu muhim

Magistral yo'llarda yaxshi ishlaydigan yuk mashinasi zich tirbandlikda muvaffaqiyatsizlikka uchrashi mumkin. Furgon shaharlarda ustunlikka ega bo'lishi mumkin, ammo uzoq masofali yo'nalishlarda samaradorligi pasayadi.

> Ushbu feature-lar modellarga umumiy o'rtacha ko'rsatkichlarni emas, balki **shartli xatti-harakatlarni** (conditional behavior) o'rganish imkonini beradi.

---

## 🚀 Maqsadli dataset yaxshilanishlari (Ishlab chiqarish darajasidagi qatlam)

Bazaviy modellashtirish va xatolar diagnostikasidan so'ng, uchta **jarrohlik aniqligidagi, yuqori ta'sirli yaxshilanishlar** kiritildi.

Bular spekulyativ feature-lar emas, balki **xatolarga asoslangan tuzatishlar** edi.

---

### 1️⃣ Yo'nalishga xos tirbandlik volatilligi (Route-Specific Traffic Volatility)

**Feature:** `(route_id, traffic_level)` bo'yicha guruhlangan yetkazib berish vaqtining standard deviation-i.

#### Asoslantirish

O'rtacha yetkazib berish vaqti xavfni yashiradi.

Ba'zi yo'nalishlar:

* Barqaror lekin sekin
* Tez lekin beqaror (volatile)
* Tirbandlik o'zgarishlariga juda sezgir

Ushbu feature faqat kutilmani emas, balki **noaniqlikni** aniq kodlaydi.

#### Kuzatilgan ta'sir

* Kechikkan yetkazib berishlarni o'tkazib yuborish sezilarli darajada kamaydi
* Recall **96.6%** gacha oshdi
* Modellar o'rtacha qiymatlarni emas, *xavf konturlarini* o'rganishni boshladi

---

### 2️⃣ Og'ir transport vositasi × Tirbandlik o'zaro ta'siri flag-i

**Feature:** `is_heavy_traffic_truck`

#### Asoslantirish

Xatolar diagnostikasi shuni ko'rsatdiki:

* O'rtacha tirbandlikda yuk mashinalarining **xato darajasi ~30% yuqori** bo'lgan
* Ushbu o'zaro ta'sir model tomonidan bilvosita kuchsiz o'rganilgan

Model buni o'zi kashf qilishini kutishdan ko'ra, ushbu interaction **ochiq-oydin ko'rsatildi**.

#### Kuzatilgan ta'sir

* False negatives (noto'g'ri salbiy natijalar) **29%** ga kamaydi
* Tirbandlik sharoitida mustahkamlik (robustness) yaxshilandi
* Turli tirbandlik rejimlarida barqarorroq bashoratlar

---

### 3️⃣ High-Fidelity One-Hot Encoding

**Quyidagilarga qo'llanildi:**

* `traffic_level`
* `vehicle_type`
* `weather`

#### Nima uchun bu muhim

Ordinal encoding quyidagicha ma'noni beradi:

> "O'rtacha tirbandlik past va yuqori tirbandlikning o'rtasida joylashgan."

Operatsion nuqtai nazardan bu noto'g'ri.

#### Natijalar

* Nochiziqli (nonlinear) modellar ifoda erkinligiga ega bo'ldi
* Validatsiya barqarorligi yaxshilandi
* Accuracy **94.3%** da barqarorlashdi
* Turli random seed-lar bo'yicha variance kamaydi

---

## 🧪 Feature Selection, Stability & Drift Readiness

### Baholash metodologiyasi

Feature selection qisqartirish mashqi emas, balki **mustahkamlik mashqi** (robustness exercise) sifatida o'tkazildi.

* Vaqtga asoslangan (time-aware) 80/20 split
* Gradient Boosting Regressor
* Permutation importance **ko'rilmagan ma'lumotlarda** (unseen data) baholandi
* Gain-based importance bilan o'zaro solishtirildi

### Aniq aniqlangan past qiymatli feature-lar

*(Hujjatlashtirilgan — jim o'chirib tashlanmagan)*

* `night_peak_conflict`
* `is_return_route`
* `route_std_distance`
* `city_pair_complexity`

Ushbu feature-lar quyidagilarni ko'rsatdi:

* Nolga yaqin entropiya
* Permutation signalining yo'qligi
* Generalizatsiyaga hissa qo'shmaslik

> Past qiymatli feature-lar yashirilmaydi, balki **hisobotda ko'rsatiladi**.

### Artefakt

* `Feature_Stability_and_Drift_Readiness_analysis.ipynb`

---

## 📦 Yakuniy ma'lumotlar to'plami tavsifi

### Dataset qisqacha mazmuni

* ~70,000 yozuv
* ~28 ta yuqori signalli, validatsiya qilingan feature-lar
* Nolga teng yetishmayotgan qiymatlar
* Temporal xavfsizlik kafolatlangan
* Model-agnostik dizayn

### Feature taksonomiyasi

* **Temporal:** davriy va kategorik vaqt signallari
* **Spatial:** yo'nalishni hisobga oluvchi intellekt
* **Operational:** transport vositasi va muhit o'zaro ta'siri
* **Risk-Aware:** volatillik va stress indikatorlari

### Kelajakda foydalanish maqsadi

* Regressiya modellari
* Gradient boosting freymvorklari
* Ehtimollik prognozi (probabilistic forecasting)
* Kechikish xavfini klassifikatsiya qilish qatlamlari

---

## 🔐 Validatsiya, Audit va Himoya choralari

Ushbu ma'lumotlar to'plami quyidagilardan o'tdi:

* Temporal leakage auditlari
* Feature evolution kuzatuvi
* Vaqt bo'yicha bo'linishlarda barqarorlik testi
* Distribution shift (taqsimot siljishi) tayyorgarligini tekshirish

> Modellarni yaratish jarayoni **yashirin strukturaviy tuzoqlarsiz** davom etishi mumkin.

---

## ⚠️ Ma'lum cheklovlar va dizayn taxminlari

* Tirbandlik ma'lumotlari real vaqt telemetriyasi emas, balki kategorikdir
* Yo'nalish xatti-harakatlari kuzatuv oynasi ichida statsionar deb hisoblanadi
* Tashqi GPS, IoT yoki sensor ma'lumotlari yo'q
* Online learning yoki adaptiv qayta o'qitish ko'zda tutilmagan

Bular e'tiborsizlik emas, balki **aniq arxitektura cheklovlaridir**.

---

## 🛠 Nimalar qasddan ko'lamdan tashqarida qoldirilgan

Ushbu repozitoriy **dataset chegarasida** tugaydi.

Rejalashtirilgan quyi oqim (downstream) kengaytmalariga quyidagilar kiradi:

* Model training pipeline-lari
* Prediction interval estimation
* Calibration tahlili
* Cost-sensitive loss funksiyalari
* Production monitoring va drift alert-lari

Ushbu bosqichlar qilinmagan ish emas, balki **dizayn bo'yicha quyi oqimga tegishlidir**.

---

## 📌 Yakuniy bayonot

Ushbu loyiha benchmark ballari ortidan quvmaydi.

U quyidagilarni o'rnatadi:

* Ma'lumotlarga ishonch (data trust)
* Feature-lar qonuniyligi (legitimacy)
* Operatsion realizm
* Ilmiy takrorlanuvchanlik (reproducibility)

Modellar o'zgaradi.

Infrastruktura rivojlanadi.

Tartibga solingan ma'lumotlar to'plami esa abadiydir.

---
