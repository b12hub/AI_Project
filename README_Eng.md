# 🚚 Risk-Aware Logistics Delivery Time Dataset  
### A Production-Grade Feature Engineering, Validation & Audit Pipeline

> **Thesis**  
> This repository operationalizes a core principle of applied machine learning:  
> **models fail not because of algorithms—but because datasets lie.**  
>
> This project transforms raw logistics data into a **risk-aware, leakage-free, auditable, model-ready dataset** explicitly designed for *real operational uncertainty*, not leaderboard demos.


# Project's Roadmap

```mermaid
---

config:
  look: classic
  layout: dagre
  theme: neutral
---
%%{init: {'theme': 'neutral'}}%%
flowchart LR
 subgraph B0["📋 BLOK 0: Loyihani Boshlash"]
        B0A["🎯 Biznes Maqsadlarini Belgilash<br>• Kechikishlarni 20% kamaytirish<br>• Xarajatlarni 15% optimallashtirish<br>• Mijozlar mamnunligini oshirish"]
        B0B@{ label: "📝 Loyiha Doirasi va Muvaffaqiyat Mezonlari<br>• MVP xususiyatlari<br>• KPI'lar belgilash<br>• Vaqt jadvali rejalashtirish" }
        B0C["🛠 Texnologiya Steki Tanlash<br>• Python, Pandas, Scikit-learn<br>• Jupyter Notebooks<br>• Vizualizatsiya vositalari"]
  end
 subgraph B1A["Real-time API'lar"]
        B1A1@{ label: "🌦 OpenWeatherMap API<br>• Harorat<br>• Yog'ingarchilik<br>• Shamol tezligi<br>• Ko'rinish" }
        B1A2@{ label: "🚦 Google Maps/Here Traffic API<br>• Tirbandlik darajasi<br>• Yo'l holati<br>• Hodisa xabarlari<br>• Jonli tezlik ma'lumoti" }
        B1A3@{ label: "🗺 Distance Matrix API<br>• Marshrut masofasi<br>• Muqobil marshrutlar<br>• To'lovli yo'llar<br>• Taxminiy sayohat vaqti" }
  end
 subgraph B1B["Ichki Tizimlar"]
        B1B1@{ label: "🚛 Logistika ERP/TMS<br>• Jo'natma yozuvlari<br>• Mashina tafsilotlari<br>• Haydovchi ma'lumoti<br>• Yuk spesifikatsiyalari" }
        B1B2@{ label: "⏱ GPS Kuzatuv Ma'lumoti<br>• Real-time joylashuv<br>• Tezlik naqshlari<br>• Ishlovsiz vaqt<br>• Marshrutga rioya qilish" }
        B1B3@{ label: "💰 Moliya Tizimlari<br>• Yoqilg'i xarajatlari<br>• Texnik xizmat xarajatlari<br>• Mehnat xarajatlari<br>• Daromad ma'lumoti" }
  end
 subgraph B1C["Tashqi Ma'lumotlar Bazalari"]
        B1C1@{ label: "📅 Taqvim/Bayram Ma'lumoti<br>• Davlat bayramlari<br>• Maktab jadvalari<br>• Maxsus tadbirlar" }
        B1C2@{ label: "🏭 Sanoat Standartlari<br>• O'rtacha yetkazib berish vaqtlari<br>• Standart xarajatlar<br>• Ish faoliyati metrikalari" }
  end
 subgraph B1["🌐 BLOK 1: Ma'lumot Yig'ish va Integratsiya"]
    direction LR
        B1A
        B1B
        B1C
        B1D@{ label: "🔄 Ma'lumot Integratsiya Quvuri<br>• API jadvali<br>• Xatolarni qayta ishlash<br>• Ma'lumotlarni tekshirish" }
        B1E@{ label: "🗄 Xom Ma'lumotlar Ombori<br>• PostgreSQL/MongoDB<br>• JSON/CSV fayllar<br>• Bulutli saqlash (S3)" }
  end
 subgraph B2D["📊 Rivojlangan Vizualizatsiya"]
        B2D1@{ label: "📉 Vaqt Seriyasi Tahlili<br>• Vaqt bo'yicha yetkazib berish naqshlari<br>• Mavsumiylik aniqlash" }
        B2D2["🗺 Geografik Tahlil<br>• Marshrut zichlik xaritalari<br>• Issiq nuqtalarni aniqlash"]
        B2D3["🔗 Munosabatlar Tahlili<br>• Juftlik grafiklari<br>• Issiqlik xaritalari<br>• Tarqalish matritsalari"]
  end
 subgraph B2["📊 BLOK 2: Tadqiqot Ma'lumotlar Tahlili"]
        B2A@{ label: "📦 Xom Ma'lumotlar To'plami<br>• 35,000-70,000 qator<br>• 15-25 xususiyat<br>• 6-12 oy davri" }
        B2B@{ label: "📋 Ma'lumotlar Profili<br>• Ustun turlari va toifalari<br>• Noyob qiymatlar soni<br>• Xotira ishlatish tahlili" }
        B2C@{ label: "📈 Statistik Tahlil<br>• Markaziy tendentsiya o'lchovlari<br>• Dispersiya metrikalari<br>• Taqsimot shakllari<br>• Korrelyatsiya matritsasi" }
        B2D
        B2E["🧠 Biznes Tushunchalarini Yaratish<br>• Eng band yetkazib berish vaqtlari<br>• Yuqori xarajatli marshrutlar<br>• Tez-tez kechikish sabablari"]
  end
 subgraph B3["🧹 BLOK 3: Ma'lumotlar Sifati va Tozalash"]
        B3A@{ label: "🔍 Ma'lumotlar Sifatini Baholash<br>• To'liqlikni tekshirish<br>• Izchillikni tekshirish<br>• Aniqlikni tasdiqlash" }
        B3B{{"❓ Yetishmayotgan Qiymatlarni Tahlil<br>• Naqshlarni aniqlash (MCAR/MAR/MNAR)"}}
        B3C1@{ label: "To'ldirish Usullari<br>• Raqamli uchun o'rtacha/median<br>• Kategoriyalar uchun moda<br>• KNN to'ldirish" }
        B3C2@{ label: "Qatorni O'chirish<br>• To'liq bo'lmagan yozuvlarni olib tashlash<br>• Namuna vakilligini tekshirish" }
        B3C3@{ label: "Rivojlangan To'ldirish<br>• MICE (Ko'p To'ldirish)<br>• Modelga asoslangan to'ldirish" }
        B3D@{ label: "🚨 Chetdan Qiymatlarni Aniqlash va Davolash<br>• IQR usuli (25-75 persentil)<br>• Z-ball tahlili (±3σ)<br>• Ajratilgan o'rmon<br>• Sohaga asoslangan chegaralar" }
        B3E@{ label: "🧽 Ma'lumotlar Izchilligi<br>• Dublikatlarni olib tashlash<br>• Ma'lumot turi mos kelmasligini tuzatish<br>• Formatlarni standartlashtirish<br>• Biznes qoidalarini tekshirish" }
        B3F@{ label: "✅ Tozalangan Ma'lumotlar To'plami<br>• Hujjatlashtirilgan o'zgarishlar<br>• Versiyani boshqarish<br>• Sifat hisoboti" }
  end
 subgraph B4A["Vaqtga Oid Xususiyatlar"]
        B4A1["⏱ Vaqt Komponentlari<br>• Kunduzgi soat (tsiklik kodlash)<br>• Hafta kuni<br>• Oy/Chorak<br>• Dam olish kuni/bayrammi"]
        B4A2@{ label: "📅 Vaqtga Asoslangan Ko'rsatkichlar<br>• Eng band soat (7-9 ertalab, 5-7 kechqurun)<br>• Ish tushgan soat bayrog'i<br>• Mavsumiy ko'rsatkichlar" }
  end
 subgraph B4B["Fazoviy Xususiyatlar"]
        B4B1@{ label: "🗺 Marshrut Xususiyatlari<br>• Masofa toifalari<br>• Shahar/qishloq tasnifi<br>• Balandlik o'zgarishlari" }
        B4B2@{ label: "📍 Joylashuv Xususiyatlari<br>• Kelib chiqish/borish zonalari<br>• Magistral yo'llarga yaqinlik<br>• Tirbandlik zichligi bo'lgan hududlar" }
  end
 subgraph B4C["Operatsion Xususiyatlar"]
        B4C1@{ label: "🚛 Mashina va Yuk<br>• Mashina yoshi va turi<br>• Yuk og'irligi nisbati<br>• Mo'rtlik indeksi<br>• Maxsus qayta ishlash talabi" }
        B4C2["👤 Inson Omillari<br>• Haydovchi tajriba darajasi<br>• Smena vaqti<br>• Oldingi ish faoliyati"]
  end
 subgraph B4D["Olingan Xususiyatlar"]
        B4D1["📊 Ish Faoliyati Metrikalari<br>• Tarixiy kechikish ehtimoli<br>• Marshrut samaradorligi balli<br>• Har bir km uchun xarajat tendentsiyasi"]
        B4D2@{ label: "⚠️ Xavf Ko'rsatkichlari<br>• Ob-havo xavfi balli<br>• Tirbandlik xavf indeksi<br>• Vaqt bosimi ko'rsatkichi" }
  end
 subgraph B4["🔧 BLOK 4: Feature Engineering"]
    direction LR
        B4A
        B4B
        B4C
        B4D
        B4E@{ label: "🔄 Xususiyatlarni Transformatsiya Qilish<br>• Log transformatsiyasi<br>• Polinom xususiyatlar<br>• O'zaro ta'sir shartlari" }
        B4F[("🧩 Xususiyatlar Matritsasi<br>• 50-100 yaratilgan xususiyat<br>• Xususiyatlar hujjatlari<br>• Versiyani kuzatish")]
  end
 subgraph B5["⚙️ BLOK 5: Ma'lumotlarni Oldindan Qayta Ishlash Quvuri"]
        B5A["🎛 Xususiyatlarni Kodlash<br>• Nominal uchun One-Hot (ob-havo)<br>• Tartibli uchun Label (tirbandlik darajasi)<br>• Yuqori kardinalik uchun Target kodlash"]
        B5B["📏 Xususiyatlarni Masshtablash<br>• SVM/Logistic uchun StandardScaler<br>• Neyron tarmoqlar uchun MinMaxScaler<br>• Chetdan qiymatlarga moyil uchun RobustScaler"]
        B5C@{ label: "⚖️ Sinflarni Muvozanatlash<br>• Ozchilik sinfi uchun SMOTE<br>• Tasodifiy pastga namuna olish<br>• Sinf og'irliklarini moslashtirish" }
        B5D@{ label: "✂️ Ma'lumotlar To'plamini Bo'lish<br>• O'qitish (70%) / Tasdiqlash (15%) / Test (15%)<br>• Vaqtga asoslangan bo'lish<br>• Stratifikatsiyalangan namuna olish" }
        B5E["📦 Quvur Yaratish<br>• sklearn Pipeline<br>• ColumnTransformer<br>• Feature union"]
        B5F@{ label: "🏭 Qayta Ishlangan Ma'lumotlar To'plamlari<br>• X_train, X_val, X_test<br>• y_train, y_val, y_test<br>• Quvur pickle fayli" }
  end
 subgraph B6B1["Klassifikatsiya Vazifasi"]
        B6B1A@{ label: "Ikkilik: Yuk kechikadimi?<br>(Ha/Yo'q)" }
        B6B1B@{ label: "Ko'p sinfli: Kechikish darajasi?<br>(Yo'q, Kichik &lt;30min, Katta &gt;30min)" }
  end
 subgraph B6B2["Regressiya Vazifalari"]
        B6B2A["Yetkazib Berish Vaqtini Bashorat Qilish<br>(daqiqalar)"]
        B6B2B["Umumiy Xarajatni Bashorat Qilish<br>(valyuta)"]
        B6B2C@{ label: "Yoqilg'i Sarfini Bashorat Qilish<br>(litr)" }
  end
 subgraph B6B3["Anomaliyalarni Aniqlash"]
        B6B3A@{ label: "G'ayrioddiy Marshrutni Aniqlash" }
        B6B3B["Xarajat Anomaliyalarini Aniqlash"]
  end
 subgraph B6["🎯 BLOK 6: Muammoni Aniqlash va Model Strategiyasi"]
        B6A@{ label: "Ko'p Vazifali O'rganish Yondashuvi" }
        B6B1
        B6B2
        B6B3
        B6C["🔄 Model Tanlash Matritsasi<br>• Muammo turi xaritalash<br>• Murakkablikni hisobga olish<br>• Tushuntirish imkoniyati ehtiyojlari"]
  end
 subgraph B7A["Bazaviy Modellar"]
        B7A1["📊 Logistic Regression<br>(Klassifikatsiya bazasi)"]
        B7A2["📈 Linear Regression<br>(Regressiya bazasi)"]
        B7A3["📉 Dummy Classifier/Regressor<br>(Tasodifiy/strategik)"]
  end
 subgraph B7B["Daraxtga Asoslangan Modellar"]
        B7B1["🌳 Decision Tree<br>(Maksimal chuqurlik: 5-15)"]
        B7B2["🌲 Random Forest<br>(n_estimators: 100-500)"]
        B7B3["🎯 Gradient Boosting<br>• XGBoost<br>• LightGBM<br>• CatBoost"]
  end
 subgraph B7C["Rivojlangan Modellar"]
        B7C1@{ label: "🧠 Neyron Tarmoqlar<br>• Jadval ma'lumotlari uchun MLP<br>• Birinchi navbatda oddiy arxitektura" }
        B7C2["🔄 Ansambl Usullari<br>• Ovoz berish klassifikatorlari<br>• Modellarni uyushtirish<br>• Aralashtirish"]
        B7C3["⏱ Vaqt Seriyasi Modellari<br>• Trendlar uchun Prophet<br>• Ketma-ketliklar uchun LSTM"]
  end
 subgraph B7["🤖 BLOK 7: Model Ishlab Chiqish va O'qitish"]
    direction TB
        B7A
        B7B
        B7C
        B7D@{ label: "⚡ Giperparametrlarni Sozlash<br>• GridSearchCV / RandomizedSearchCV<br>• Bayes optimizatsiyasi<br>• O'zaro tekshirish (k=5)" }
        B7E@{ label: "📦 O'qitilgan Modellar<br>• Picklangan model fayllari<br>• O'qitish jurnallari<br>• Versiya metadata" }
  end
 subgraph B8A["Klassifikatsiya Metrikalari"]
        B8A1@{ label: "📊 Asosiy Metrikalar<br>• Aniqlik, Precision, Recall<br>• F1-Score (makro/og'irlik)<br>• AUC-ROC egri chizig'i" }
        B8A2["📋 Rivojlangan Metrikalar<br>• Koenning Kappa<br>• Metyus Korrelyatsiyasi<br>• Log Loss"]
        B8A3@{ label: "🎭 Adashuv Matritsasi Tahlili<br>• Noto'g'ri ijobiy/salbay stavkalari<br>• Sinf bo'yicha ish faoliyati" }
  end
 subgraph B8B["Regressiya Metrikalari"]
        B8B1@{ label: "📏 Xato Metrikalari<br>• MAE, MSE, RMSE<br>• MAPE (O'rtacha Mutloq Foiz)<br>• SMAPE (Simmetrik MAPE)" }
        B8B2["📐 Moslik Metrikalari<br>• R² (Determinatsiya koeffitsienti<br>• Moslashtirilgan R²<br>• Izohlab berilgan dispersiya"]
        B8B3["📉 Qoldiq Tahlili<br>• Xatolarning taqsimoti<br>• Geteroskedastiklikni tekshirish"]
  end
 subgraph B8C["Biznes Metrikalari"]
        B8C1["💰 Xarajatni Tejash Bahosi<br>• Bashorat qilingan vs haqiqiy xarajatlar<br>• Optimallashtirish potentsiali"]
        B8C2["⏱ Vaqtni Tejash Hisobi<br>• Samaradorlik yaxshilanishi<br>• SLA ga rioya qilish darajasi"]
        B8C3@{ label: "🎯 Qaror Ta'siri<br>• Noto'g'ri ijobiy xarajat tahlili<br>• Xavfni kamaytirish miqdori" }
  end
 subgraph B8["📈 BLOK 8: Keng Qamrovli Modelni Baholash"]
    direction LR
        B8A
        B8B
        B8C
        B8D@{ label: "📊 O'zaro tekshirish Natijalari<br>• Qatlamlar bo'yicha o'rtacha ball<br>• Dispersiya tahlili<br>• Barqarorlikni baholash" }
        B8E[("📑 Baholash Hisoboti<br>• Modelni solishtirish jadvali<br>• Statistik ahamiyat<br>• Tavsiyalar")]
  end
 subgraph B9["🔍 BLOK 9: Modelni Tushuntirish va Tushunchalar"]
        B9A["🎯 Xususiyatlar Muhimligini Tahlil Qilish<br>• Daraxtga asoslangan muhimlik<br>• SHAP qiymatlari<br>• Almashtirish muhimligi"]
        B9B@{ label: "📊 Qisman Bog'liqlik Grafiklari<br>• Individual xususiyat ta'siri<br>• O'zaro ta'sir effektlari<br>• Qaror chegaralari" }
        B9C["🧠 Biznes Qoidalarini Olish<br>• Daraxtlardan agar-shunda qoidalari<br>• Qaror chegaralari<br>• Muhim omillar"]
        B9D["📈 Agar-shunda Tahlili<br>• Ssenariy simulyatsiyasi<br>• Sezgirlik tahlili<br>• Zararsizlanish nuqtalari"]
        B9E["⚠️ Xavf Omillarini Aniqlash<br>• Yuqori kechikish ehtimoli shartlari<br>• Xarajat oshishi trigerlari<br>• Tor joylarni tahlil qilish"]
        B9F@{ label: "💡 Amalga Oshirish Mumkin Bo'lgan Tushunchalar<br>• Takomillashtirish uchun ustuvor sohalar<br>• Tez yutuqlarni aniqlash<br>• Strategik tavsiyalar" }
  end
 subgraph B10["🚀 BLOK 10: Ishlatishga Tayyorlash"]
        B10A@{ label: "📦 Modelni Paketlash<br>• Bashorat quvurini yaratish<br>• API o'rash (FastAPI/Flask)<br>• Docker konteynerizatsiyasi" }
        B10B["⚡ Ish Faoliyatini Optimallashtirish<br>• Model kvantizatsiyasi<br>• Partiyali bashorat sozlash<br>• Kesh strategiyasi"]
        B10C@{ label: "🔒 Kuzatish Framework<br>• Ma'lumotlar surilishini aniqlash<br>• Kontseptsiya surilishini kuzatish<br>• Ish faoliyati pasayishi ogohlantirishlari" }
        B10D@{ label: "📋 Ishlatish Hujjatlari<br>• API hujjatlari<br>• Foydalanuvchi qo'llanmasi<br>• Texnik xizmat ko'rsatish qo'llanmasi" }
        B10E[("🎯 Ishlab Chiqarishga Tayyor Paket<br>• 1.0-versiya chiqarish<br>• Orqaga qaytish strategiyasi<br>• A/B test rejasi")]
  end
 subgraph B11["✅ BLOK 11: Yakuniy Yetkazib Berishlar va Topshirish"]
        B11A@{ label: "📄 Texnik Hujjatlar<br>• To'liq kod hujjatlari<br>• Arxitektura diagrammalari<br>• Ma'lumotlar lug'ati" }
        B11B["🎓 Akademik Yetkazib Berishlar<br>• Tadqiqot maqolasi/hisobot<br>• Taqdimot slaydlari<br>• Manba kodi ombori"]
        B11C@{ label: "📊 Biznes Hisobotlari<br>• Ijrochi xulosa<br>• ROI tahlili<br>• Amalga oshirish yo'l xaritasi" }
        B11D@{ label: "🔧 Operatsion Vositalar<br>• Jupyter daftarlari<br>• O'qitish skriptlari<br>• Utility funktsiyalari" }
        B11E@{ label: "🔄 Doimiy Takomillashtirish Rejasi<br>• Fikr-mulohaza mexanizmlari<br>• Modelni qayta o'qitish jadvali<br>• Xususiyat yangilash quvuri" }
        B11F(["🎉 Loyiha Tugallandi<br>va Topshiriq Topshirildi"])
  end
    Start(["🚚<br>Transport va Logistika<br>AI Tizimi"]) L_Start_B0_0@--> B0
    B0A L_B0A_B0B_0@--> B0B
    B0B L_B0B_B0C_0@--> B0C
    B0 L_B0_B1_0@--> B1
    B1A L_B1A_B1D_0@--> B1D
    B1B L_B1B_B1D_0@--> B1D
    B1C L_B1C_B1D_0@--> B1D
    B1D L_B1D_B1E_0@--> B1E
    B1 L_B1_B2_0@--> B2
    B2A L_B2A_B2B_0@--> B2B
    B2B L_B2B_B2C_0@--> B2C
    B2C L_B2C_B2D_0@--> B2D
    B2D L_B2D_B2E_0@--> B2E
    B2 L_B2_B3_0@--> B3
    B3B L_B3B_B3C1_0@-- &lt;5% yetishmayapti --> B3C1
    B3B L_B3B_B3C2_0@-- >30% yetishmayapti --> B3C2
    B3B L_B3B_B3C3_0@-- "5-30% yetishmayapti" --> B3C3
    B3C1 L_B3C1_B3D_0@--> B3D
    B3C2 L_B3C2_B3D_0@--> B3D
    B3C3 L_B3C3_B3D_0@--> B3D
    B3D L_B3D_B3E_0@--> B3E
    B3E L_B3E_B3F_0@--> B3F
    B3 L_B3_B4_0@--> B4
    B4A L_B4A_B4E_0@--> B4E
    B4B L_B4B_B4E_0@--> B4E
    B4C L_B4C_B4E_0@--> B4E
    B4D L_B4D_B4E_0@--> B4E
    B4E L_B4E_B4F_0@--> B4F
    B4 L_B4_B5_0@--> B5
    B5A L_B5A_B5B_0@--> B5B
    B5B L_B5B_B5C_0@--> B5C
    B5C L_B5C_B5D_0@--> B5D
    B5D L_B5D_B5E_0@--> B5E
    B5E L_B5E_B5F_0@--> B5F
    B5 L_B5_B6_0@--> B6
    B6A L_B6A_B6B1_0@--> B6B1 & B6B2 & B6B3
    B6B1 L_B6B1_B6C_0@--> B6C
    B6B2 L_B6B2_B6C_0@--> B6C
    B6B3 L_B6B3_B6C_0@--> B6C
    B6 L_B6_B7_0@--> B7
    B7A L_B7A_B7D_0@--> B7D
    B7B L_B7B_B7D_0@--> B7D
    B7C L_B7C_B7D_0@--> B7D
    B7D L_B7D_B7E_0@--> B7E
    B7 L_B7_B8_0@--> B8
    B8A L_B8A_B8D_0@--> B8D
    B8B L_B8B_B8D_0@--> B8D
    B8C L_B8C_B8D_0@--> B8D
    B8D L_B8D_B8E_0@--> B8E
    B8 L_B8_B9_0@--> B9
    B9A L_B9A_B9B_0@--> B9B
    B9B L_B9B_B9C_0@--> B9C
    B9C L_B9C_B9D_0@--> B9D
    B9D L_B9D_B9E_0@--> B9E
    B9E L_B9E_B9F_0@--> B9F
    B9 L_B9_B10_0@--> B10
    B10A L_B10A_B10B_0@--> B10B
    B10B L_B10B_B10C_0@--> B10C
    B10C L_B10C_B10D_0@--> B10D
    B10D L_B10D_B10E_0@--> B10E
    B10 L_B10_B11_0@--> B11
    B11A L_B11A_B11F_0@--> B11F
    B11B L_B11B_B11F_0@--> B11F
    B11C L_B11C_B11F_0@--> B11F
    B11D L_B11D_B11F_0@--> B11F
    B11E L_B11E_B11F_0@--> B11F

    B0B@{ shape: rect}
    B1A1@{ shape: rect}
    B1A2@{ shape: rect}
    B1A3@{ shape: rect}
    B1B1@{ shape: rect}
    B1B2@{ shape: rect}
    B1B3@{ shape: rect}
    B1C1@{ shape: rect}
    B1C2@{ shape: rect}
    B1D@{ shape: rect}
    B1E@{ shape: cylinder}
    B2D1@{ shape: rect}
    B2A@{ shape: cylinder}
    B2B@{ shape: rect}
    B2C@{ shape: rect}
    B3A@{ shape: rect}
    B3C1@{ shape: rect}
    B3C2@{ shape: rect}
    B3C3@{ shape: rect}
    B3D@{ shape: rect}
    B3E@{ shape: rect}
    B3F@{ shape: cylinder}
    B4A2@{ shape: rect}
    B4B1@{ shape: rect}
    B4B2@{ shape: rect}
    B4C1@{ shape: rect}
    B4D2@{ shape: rect}
    B4E@{ shape: rect}
    B5C@{ shape: rect}
    B5D@{ shape: rect}
    B5F@{ shape: cylinder}
    B6B1A@{ shape: rect}
    B6B1B@{ shape: rect}
    B6B2C@{ shape: rect}
    B6B3A@{ shape: rect}
    B6A@{ shape: hexagon}
    B7C1@{ shape: rect}
    B7D@{ shape: rect}
    B7E@{ shape: cylinder}
    B8A1@{ shape: rect}
    B8A3@{ shape: rect}
    B8B1@{ shape: rect}
    B8C3@{ shape: rect}
    B8D@{ shape: rect}
    B9B@{ shape: rect}
    B9F@{ shape: cylinder}
    B10A@{ shape: rect}
    B10C@{ shape: rect}
    B10D@{ shape: rect}
    B11A@{ shape: rect}
    B11C@{ shape: rect}
    B11D@{ shape: rect}
    B11E@{ shape: rect}
     B1:::data
     B2:::data
     B3:::data
     B4:::data
     B5:::data
     B6:::analysis
     B7:::analysis
     B8:::analysis
     B9:::analysis
     B10:::model
     B11:::deploy,deliver
    classDef data fill:#E3F2FD,stroke:#1976D2
    classDef analysis fill:#F3E5F5,stroke:#7B1FA2
    classDef model fill:#E8F5E8,stroke:#388E3C
    classDef deploy fill:#FFF3E0,stroke:#F57C00
    classDef deliver fill:#FFEBEE,stroke:#D32F2F
    style B0A stroke:#2962FF,fill:#FFFFFF
    style B0B stroke:#2962FF,fill:#FFFFFF
    style B0C stroke:#2962FF,fill:#FFFFFF
    style B1A1 stroke:#2962FF,fill:#FFFFFF
    style B1A2 stroke:#2962FF,fill:#FFFFFF
    style B1A3 stroke:#2962FF,fill:#FFFFFF
    style B1B1 stroke:#2962FF,fill:#FFFFFF
    style B1B2 stroke:#2962FF,fill:#FFFFFF
    style B1B3 stroke:#2962FF,fill:#FFFFFF
    style B1C1 stroke:#2962FF,fill:#FFFFFF
    style B1C2 stroke:#2962FF,fill:#FFFFFF
    style B1A stroke:#00C853,fill:#FFFFFF
    style B1B stroke:#00C853,fill:#FFFFFF
    style B1C fill:#FFFFFF
    style B1D stroke:#2962FF,fill:#FFFFFF
    style B1E stroke:#2962FF,fill:#FFFFFF
    style B2D1 stroke:#2962FF,fill:#FFFFFF
    style B2D2 stroke:#2962FF,fill:#FFFFFF
    style B2D3 stroke:#2962FF,fill:#FFFFFF
    style B2A stroke:#2962FF,fill:#FFFFFF
    style B2B stroke:#2962FF,fill:#FFFFFF
    style B2C stroke:#2962FF,fill:#FFFFFF
    style B2D stroke:#00C853,fill:#FFFFFF
    style B2E stroke:#2962FF,fill:#FFFFFF
    style B3A stroke:#2962FF,fill:#FFFFFF
    style B3B stroke:#2962FF,fill:#FFFFFF
    style B3C1 stroke:#2962FF,fill:#FFFFFF
    style B3C2 stroke:#2962FF,fill:#FFFFFF
    style B3C3 stroke:#2962FF,fill:#FFFFFF
    style B3D stroke:#2962FF,fill:#FFFFFF
    style B3E stroke:#2962FF,fill:#FFFFFF
    style B3F stroke:#2962FF,fill:#FFFFFF
    style B4A1 stroke:#2962FF,fill:#FFFFFF
    style B4A2 stroke:#2962FF,fill:#FFFFFF
    style B4B1 stroke:#2962FF,fill:#FFFFFF
    style B4B2 stroke:#2962FF,fill:#FFFFFF
    style B4C1 stroke:#2962FF,fill:#FFFFFF
    style B4C2 stroke:#2962FF,fill:#FFFFFF
    style B4D1 stroke:#2962FF,fill:#FFFFFF
    style B4D2 stroke:#2962FF,fill:#FFFFFF
    style B4A stroke:#00C853,fill:#FFFFFF
    style B4B stroke:#00C853,fill:#FFFFFF
    style B4C stroke:#00C853,fill:#FFFFFF
    style B4D stroke:#00C853,fill:#FFFFFF
    style B4E stroke:#00C853,fill:#FFFFFF
    style B4F stroke:#00C853,fill:#FFFFFF
    style B5A stroke:#FFD600,fill:#FFFFFF
    style B5B stroke:#FFD600,fill:#FFFFFF
    style B5C stroke:#FFD600,fill:#FFFFFF
    style B5D stroke:#FFD600,fill:#FFFFFF
    style B5E stroke:#FFD600,fill:#FFFFFF
    style B5F stroke:#FFD600,fill:#FFFFFF
    style B6B1A stroke:#FFD600,fill:#FFFFFF
    style B6B1B stroke:#FFD600,fill:#FFFFFF
    style B6B2A stroke:#FFD600,fill:#FFFFFF
    style B6B2B stroke:#FFD600,fill:#FFFFFF
    style B6B2C stroke:#FFD600,fill:#FFFFFF
    style B6B3A stroke:#FFD600,fill:#FFFFFF
    style B6B3B stroke:#FFD600,fill:#FFFFFF
    style B6A stroke:#FFD600,fill:#FFFFFF
    style B6B1 stroke:#FFD600,fill:#FFFFFF
    style B6B2 stroke:#FFD600,fill:#FFFFFF
    style B6B3 stroke:#FFD600,fill:#FFFFFF
    style B6C stroke:#FFD600,fill:#FFFFFF
    style B7A1 stroke:#FFD600,fill:#FFFFFF
    style B7A2 stroke:#FFD600,fill:#FFFFFF
    style B7A3 stroke:#FFD600,fill:#FFFFFF
    style B7B1 stroke:#FFD600,fill:#FFFFFF
    style B7B2 stroke:#FFD600,fill:#FFFFFF
    style B7B3 stroke:#FFD600,fill:#FFFFFF
    style B7C1 stroke:#FFD600,fill:#FFFFFF
    style B7C2 stroke:#FFD600,fill:#FFFFFF
    style B7C3 stroke:#FFD600,fill:#FFFFFF
    style B7A stroke:#FFD600,fill:#FFFFFF
    style B7B stroke:#FFD600,fill:#FFFFFF
    style B7C stroke:#FFD600,fill:#FFFFFF
    style B7D stroke:#FFD600,fill:#FFFFFF
    style B7E stroke:#FFD600,fill:#FFFFFF
    style B8A1 stroke:#D50000,fill:#FFFFFF
    style B8A2 stroke:#D50000,fill:#FFFFFF
    style B8A3 stroke:#D50000,fill:#FFFFFF
    style B8B1 stroke:#D50000,fill:#FFFFFF
    style B8B2 stroke:#D50000,fill:#FFFFFF
    style B8B3 stroke:#D50000,fill:#FFFFFF
    style B8C1 stroke:#D50000,fill:#FFFFFF
    style B8C2 stroke:#D50000,fill:#FFFFFF
    style B8C3 stroke:#D50000,fill:#FFFFFF
    style B8A stroke:#D50000,fill:#FFFFFF
    style B8B stroke:#D50000,fill:#FFFFFF
    style B8C stroke:#D50000,fill:#FFFFFF
    style B8D stroke:#D50000,fill:#FFFFFF
    style B8E stroke:#D50000,fill:#FFFFFF
    style B9A stroke:#D50000,fill:#FFFFFF
    style B9B stroke:#D50000,fill:#FFFFFF
    style B9C stroke:#D50000,fill:#FFFFFF
    style B9D stroke:#D50000,fill:#FFFFFF
    style B9E stroke:#D50000,fill:#FFFFFF
    style B9F stroke:#D50000,fill:#FFFFFF
    style B10A stroke:#D50000,fill:#FFFFFF
    style B10B stroke:#D50000,fill:#FFFFFF
    style B10C stroke:#D50000,fill:#FFFFFF
    style B10D stroke:#D50000,fill:#FFFFFF
    style B10E stroke:#D50000,fill:#FFFFFF
    style B11A stroke:#D50000,fill:#FFFFFF
    style B11B stroke:#D50000,fill:#FFFFFF
    style B11C stroke:#D50000,fill:#FFFFFF
    style B11D stroke:#D50000,fill:#FFFFFF
    style B11E stroke:#D50000,fill:#FFFFFF
    style B11F fill:#00C853,color:white,stroke:#00C853
    style Start fill:#4CAF50,color:white,stroke:#00C853
    style B0 fill:#00C853,color:#FFFFFF
    style B1 fill:#00C853,color:#FFFFFF
    style B2 fill:#00C853,color:#FFFFFF
    style B3 fill:#00C853,color:#FFFFFF
    style B4 fill:#00C853,color:#FFFFFF
    style B5 fill:#FFD600,stroke:#FFD600
    style B6 fill:#FFD600,stroke:#FFD600
    style B7 fill:#FFD600,stroke:#FFD600
    style B8 stroke:#FFCDD2,fill:#D50000,color:#FFFFFF
    style B9 stroke:#FFCDD2,fill:#D50000,color:#FFFFFF
    style B10 stroke:#FFCDD2,fill:#D50000,color:#FFFFFF
    style B11 fill:#D50000,color:#FFFFFF
    linkStyle 0 stroke:#00C853,fill:none
    linkStyle 1 stroke:#2962FF,fill:none
    linkStyle 2 stroke:#2962FF,fill:none
    linkStyle 3 stroke:#00C853,fill:none
    linkStyle 4 stroke:#2962FF,fill:none
    linkStyle 5 stroke:#2962FF,fill:none
    linkStyle 6 stroke:#2962FF,fill:none
    linkStyle 7 stroke:#2962FF,fill:none
    linkStyle 8 stroke:#00C853,fill:none
    linkStyle 9 stroke:#2962FF,fill:none
    linkStyle 10 stroke:#2962FF,fill:none
    linkStyle 11 stroke:#2962FF,fill:none
    linkStyle 12 stroke:#2962FF,fill:none
    linkStyle 13 stroke:#00C853,fill:none
    linkStyle 14 stroke:#2962FF,fill:none
    linkStyle 15 stroke:#2962FF,fill:none
    linkStyle 16 stroke:#2962FF,fill:none
    linkStyle 17 stroke:#2962FF,fill:none
    linkStyle 18 stroke:#2962FF,fill:none
    linkStyle 19 stroke:#2962FF,fill:none
    linkStyle 20 stroke:#2962FF,fill:none
    linkStyle 21 stroke:#2962FF,fill:none
    linkStyle 22 stroke:#00C853,fill:none
    linkStyle 23 stroke:#2962FF,fill:none
    linkStyle 24 stroke:#2962FF,fill:none
    linkStyle 25 stroke:#2962FF,fill:none
    linkStyle 26 stroke:#2962FF,fill:none
    linkStyle 27 stroke:#2962FF,fill:none
    linkStyle 28 stroke:#00C853,fill:none
    linkStyle 29 stroke:#D50000,fill:none
    linkStyle 30 stroke:#D50000,fill:none
    linkStyle 31 stroke:#D50000,fill:none
    linkStyle 32 stroke:#D50000,fill:none
    linkStyle 33 stroke:#D50000,fill:none
    linkStyle 34 stroke:#D50000,fill:none
    linkStyle 35 stroke:#D50000,fill:none
    linkStyle 36 stroke:#D50000,fill:none
    linkStyle 37 stroke:#D50000,fill:none
    linkStyle 38 stroke:#D50000,fill:none
    linkStyle 39 stroke:#D50000,fill:none
    linkStyle 40 stroke:#D50000,fill:none
    linkStyle 41 stroke:#D50000,fill:none
    linkStyle 42 stroke:#D50000,fill:none
    linkStyle 43 stroke:#D50000,fill:none
    linkStyle 44 stroke:#D50000,fill:none
    linkStyle 45 stroke:#D50000,fill:none
    linkStyle 46 stroke:#D50000,fill:none
    linkStyle 47 stroke:#FFFFFF,fill:none
    linkStyle 48 stroke:#FFFFFF,fill:none
    linkStyle 49 stroke:#FFFFFF,fill:none
    linkStyle 50 stroke:#FFFFFF,fill:none
    linkStyle 51 stroke:#D50000,fill:none
    linkStyle 52 stroke:#FFFFFF,fill:none
    linkStyle 53 stroke:#FFFFFF,fill:none
    linkStyle 54 stroke:#FFFFFF,fill:none
    linkStyle 55 stroke:#FFFFFF,fill:none
    linkStyle 56 stroke:#FFFFFF,fill:none
    linkStyle 57 stroke:#D50000,fill:none
    linkStyle 58 stroke:#FFFFFF,fill:none
    linkStyle 59 stroke:#FFFFFF,fill:none
    linkStyle 60 stroke:#FFFFFF,fill:none
    linkStyle 61 stroke:#FFFFFF,fill:none
    linkStyle 62 stroke:#D50000,fill:none
    linkStyle 63 stroke:#FFFFFF,fill:none
    linkStyle 64 stroke:#FFFFFF,fill:none
    linkStyle 65 stroke:#FFFFFF,fill:none
    linkStyle 66 stroke:#FFFFFF,fill:none
    linkStyle 67 stroke:#FFFFFF,fill:none

    L_Start_B0_0@{ animation: fast } 
    L_B0A_B0B_0@{ animation: fast } 
    L_B0B_B0C_0@{ animation: fast } 
    L_B0_B1_0@{ animation: fast } 
    L_B1A_B1D_0@{ animation: fast } 
    L_B1B_B1D_0@{ animation: fast } 
    L_B1C_B1D_0@{ animation: fast } 
    L_B1D_B1E_0@{ animation: fast } 
    L_B1_B2_0@{ animation: fast } 
    L_B2A_B2B_0@{ animation: fast } 
    L_B2B_B2C_0@{ animation: fast } 
    L_B2C_B2D_0@{ animation: fast } 
    L_B2D_B2E_0@{ animation: fast } 
    L_B2_B3_0@{ animation: fast } 
    L_B3B_B3C1_0@{ animation: fast } 
    L_B3B_B3C2_0@{ animation: fast } 
    L_B3B_B3C3_0@{ animation: fast } 
    L_B3C1_B3D_0@{ animation: fast } 
    L_B3C2_B3D_0@{ animation: fast } 
    L_B3C3_B3D_0@{ animation: fast } 
    L_B3D_B3E_0@{ animation: fast } 
    L_B3E_B3F_0@{ animation: fast } 
    L_B3_B4_0@{ animation: fast } 
    L_B4A_B4E_0@{ animation: fast } 
    L_B4B_B4E_0@{ animation: fast } 
    L_B4C_B4E_0@{ animation: fast } 
    L_B4D_B4E_0@{ animation: fast } 
    L_B4E_B4F_0@{ animation: fast } 
    L_B4_B5_0@{ animation: fast } 
    L_B5A_B5B_0@{ animation: fast } 
    L_B5B_B5C_0@{ animation: fast } 
    L_B5C_B5D_0@{ animation: fast } 
    L_B5D_B5E_0@{ animation: fast } 
    L_B5E_B5F_0@{ animation: fast } 
    L_B5_B6_0@{ animation: fast } 
    L_B6A_B6B1_0@{ animation: fast } 
    L_B6A_B6B2_0@{ animation: fast } 
    L_B6A_B6B3_0@{ animation: fast } 
    L_B6B1_B6C_0@{ animation: fast } 
    L_B6B2_B6C_0@{ animation: fast } 
    L_B6B3_B6C_0@{ animation: fast } 
    L_B6_B7_0@{ animation: fast } 
    L_B7A_B7D_0@{ animation: fast } 
    L_B7B_B7D_0@{ animation: fast } 
    L_B7C_B7D_0@{ animation: fast } 
    L_B7D_B7E_0@{ animation: fast } 
    L_B7_B8_0@{ animation: fast } 
    L_B8A_B8D_0@{ animation: fast } 
    L_B8B_B8D_0@{ animation: fast } 
    L_B8C_B8D_0@{ animation: fast } 
    L_B8D_B8E_0@{ animation: fast } 
    L_B8_B9_0@{ animation: fast } 
    L_B9A_B9B_0@{ animation: fast } 
    L_B9B_B9C_0@{ animation: fast } 
    L_B9C_B9D_0@{ animation: fast } 
    L_B9D_B9E_0@{ animation: fast } 
    L_B9E_B9F_0@{ animation: fast } 
    L_B9_B10_0@{ animation: fast } 
    L_B10A_B10B_0@{ animation: fast } 
    L_B10B_B10C_0@{ animation: fast } 
    L_B10C_B10D_0@{ animation: fast } 
    L_B10D_B10E_0@{ animation: fast } 
    L_B10_B11_0@{ animation: fast } 
    L_B11A_B11F_0@{ animation: fast } 
    L_B11B_B11F_0@{ animation: fast } 
    L_B11C_B11F_0@{ animation: fast } 
    L_B11D_B11F_0@{ animation: fast } 
    L_B11E_B11F_0@{ animation: fast }
```


---

## 📌 Executive Summary (TL;DR)

Delivery time prediction is **not** a vanilla regression task.

In real logistics systems:
- Errors are **asymmetric**
- Delays compound operational risk
- Routes behave non-stationarily
- Vehicles interact with traffic in non-linear ways
- Temporal leakage silently invalidates models

This project addresses those realities by building a **dataset-first ML foundation**, not a model-first experiment.

### What This Repository Delivers

✔ A multi-stage **data cleaning & validation pipeline**  
✔ A **leakage-audited feature engineering framework**  
✔ Route-aware, vehicle-aware, and risk-aware features  
✔ Explicit dataset lineage & version control  
✔ A **model-agnostic, production-safe dataset**  

### What It Intentionally Avoids

✖ Premature model optimization  
✖ Deployment-specific assumptions  
✖ Dashboard-driven overfitting  

> **Outcome:**  
> A dataset that shifts delivery time prediction from *average estimation* to **risk-aware forecasting under uncertainty**.

---

## 🎯 Problem Definition & System Context

### Operational Reality

In logistics, prediction errors are **not symmetric**:

| Scenario | Business Impact |
|--------|----------------|
| Early delivery | Minor inefficiency |
| Late delivery | SLA breach, trust loss, cost escalation |

Most ML pipelines optimize **mean error**, while logistics systems fail in the **tails**.

This project reframes delivery time prediction as a **risk-sensitive regression problem** rather than a purely statistical exercise.

---

### Core System Challenges

| Challenge | Why It Breaks Naive Models |
|--------|----------------------------|
| Traffic | Categorical labels hide non-linear behavior |
| Vehicles | Different dynamics under congestion |
| Routes | Historical instability & variance |
| Time | Leakage inflates offline metrics |
| Encoding | Ordinal assumptions fabricate signal |

The dataset must encode **operational physics**, not spreadsheet correlations.

---

### Target Variable

- **`delivery_time_hours`**
- Continuous regression target
- Evaluated with **risk awareness**, not just RMSE

> The objective is not “best average prediction”  
> but **robust, defensible performance under operational stress**.

---

## 🧭 Project Scope & Explicit Boundaries

### Included in Scope

✅ Raw data ingestion & auditing  
✅ Structural and logical cleaning  
✅ Multi-phase feature engineering  
✅ Leakage & temporal validation  
✅ Feature stability & drift readiness  
✅ Final dataset materialization  

### Explicitly Out of Scope

❌ Model deployment pipelines  
❌ Real-time inference systems  
❌ Monitoring or alerting dashboards  

> This separation preserves **dataset portability, auditability, and long-term reuse** across models and teams.

---

## 🗂 Repository Structure

```map
├── Dataset/
│   ├── raw_data.csv
│   ├── clean_data_v1.csv
│   ├── clean_data_v2.csv
│   ├── feature_data_v1.csv
│   ├── feature_data_v2.csv
│   ├── feature_data_v3.csv
│   ├── feature_data_v4.csv
│   ├── final_dataset.csv
│   └── model_ready_data.csv
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
│   ├── Cleaning_Report.md
│   └── Analysis_Report.md
│
└── Visualizations/
    ├── comparison_analysis.png
    └── data_quality_viz.png
```
--- 
Here is the converted Markdown version of your documentation. I have structured it for maximum readability using tables, task lists, and clear hierarchical headings.

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

The raw dataset is intentionally treated as untrusted:

* **Temporal ordering** is not guaranteed.
* **Categorical variables** imply false ordinality.
* **Routes** collapse history into single values.
* **Risk signals** are entirely absent.
* **Leakage potential** is non-trivial.

> [!CAUTION]
> **Conclusion:** Raw data is not model-safe by default and must be audited before use.

---

## 📥 Dataset Lineage & Versioning Strategy

This project enforces strict dataset immutability and versioning. Every transformation stage produces a new dataset, preserves upstream artifacts, and enables full backward traceability.

### Dataset Evolution Pipeline

| Stage | Artifact | Purpose |
| --- | --- | --- |
| **Raw Ingestion** | `raw_data.csv` | Untouched source |
| **Cleaning v1** | `clean_data_v1.csv` | Schema & null handling |
| **Cleaning v2** | `clean_data_v2.csv` | Logical validation |
| **Feature v1** | `feature_data_v1.csv` | Temporal foundations |
| **Feature v2** | `feature_data_v2.csv` | Spatial & route context |
| **Feature v3** | `feature_data_v3.csv` | Operational interactions |
| **Feature v4** | `feature_data_v4.csv` | Risk-aware enrichment |
| **Final** | `final_dataset.csv` | Audited & documented |
| **Model-Ready** | `model_ready_data.csv` | Encoded & selection-ready |
| **Optimized** |  `final_dataset_CLEANED.csv` | Cleaned & Optimizes | 

### Why This Matters

This lineage enables:

1. Feature regression analysis
2. Model failure attribution
3. Reproducible experimentation
4. Safe production rollback

---

## 🧼 Data Cleaning & Structural Validation

### Objective

Transform raw logistics records into a structurally valid, logically consistent dataset before introducing any modeling assumptions.

### Cleaning Principles

Cleaning was deliberately conservative:

* No target-aware filtering
* No statistical smoothing
* No aggressive row deletion
* No premature feature pruning

### Key Cleaning Actions

* [x] Enforced strict schemas and dtypes
* [x] Validated temporal fields
* [x] Normalized categorical vocabularies
* [x] Removed impossible distances
* [x] Verified city-pair consistency

Every cleaning step is reversible, documented, and auditable.

### Artifacts

* `Data_Cleaning.ipynb`
* `Data_Quality_Validation.ipynb`
* `Documentations/Cleaning_Report.md`

---

## 🔍 Exploratory Analysis & Error Surface Mapping

### Purpose

Expose where and why naive delivery models fail, not just how well they score.

### Key Observations

* **Error distributions** are heavy-tailed.
* **Medium traffic** exhibits unexpected delay spikes.
* **Certain routes** show persistent volatility.
* **Distance** explains baseline time—but not delay risk.

### Strategic Insight

> Optimizing average error hides operational failure. Logistics systems break in the tails. Feature engineering must focus there.

### Artifacts

* `Data_Analsis.ipynb`
* `Baseline_Modeling_and_Error_Diagnostics.ipynb`

---

## 🧠 Feature Engineering Framework (Design Doctrine)

All feature engineering adheres to four non-negotiable rules:

1. **Zero Temporal Leakage**
* No future aggregation
* No post-delivery statistics


2. **No Ordinal Lies**
* Categorical variables are treated as categorical
* No fabricated linearity


3. **No Low-Entropy Pollution**
* Dead features are documented, not hidden


4. **Operational Interpretability**
* Every feature maps to a real mechanism



**Note:** If a feature cannot be explained operationally, it does not belong.

---
## 🧱 Feature Engineering — Phase Breakdown

This project adopts a **multi-phase, explicitly audited feature engineering strategy**.  
Each phase introduces *orthogonal signal*, validated in isolation before being allowed downstream.

Feature engineering is treated as **system design**, not feature hoarding.

---

### Phase 2.3.1 — Temporal Signal Encoding  
**Notebook:** `Feauture_Engineering_BLOCK-2.3.1.ipynb`

Raw timestamps are **not directly model-consumable**. Naively extracting hour or month creates artificial discontinuities (e.g., 23 → 0).

To avoid this, time is encoded as **cyclical structure**, preserving periodic continuity.

#### Implemented Features
- Hour-of-day cyclic encoding (`sin`, `cos`)
- Month-of-year cyclic encoding
- Weekend indicators
- Night-operation flags
- Peak-hour congestion markers

#### Design Intent
- Preserve temporal periodicity
- Avoid ordinal leakage
- Allow models to learn **time rhythms**, not time labels

> Time is not linear in operations.  
> These encodings allow models to “feel” the clock rather than read it.

---

### Phase 2.3.2 — Spatial & Route Intelligence  
**Notebook:** `Spatial_Feature_Engineering.ipynb`

Logistics systems do not operate on isolated trips—they operate on **routes with memory**.

This phase introduces **route-aware context** while maintaining strict leakage control.

#### Engineered Constructs
- `route_id` (origin–destination abstraction)
- Route frequency counts
- Route-level average distance
- Long-haul route indicators

#### Leakage Safeguard
All route statistics are computed:
- Using **historical data only**
- Without access to the current order’s target
- Without forward-looking aggregation

> Route intelligence provides *context*, not prophecy.

---

### Phase 2.3.3 — Operational & Vehicle Interaction Features  
**Notebook:** `Operational_&_Vehicle_Interaction_FE.ipynb`

Most delivery failures are not caused by single variables, but by **interactions**.

This phase encodes how vehicles behave **under specific operational stressors**.

#### Interaction Dimensions
- Vehicle × distance suitability
- Vehicle × traffic stress response
- Vehicle × weather sensitivity
- Composite operational stress indices

#### Why This Matters
A truck performing well on highways may fail in dense traffic.  
A van may excel in cities but degrade over long-haul routes.

> These features allow models to learn **conditional behavior**, not population averages.

---

## 🚀 Targeted Dataset Enhancements (Production-Grade Layer)

After baseline modeling and error diagnostics, three **surgical, high-impact enhancements** were introduced.

These were not speculative features—they were **error-driven corrections**.

---

### 1️⃣ Route-Specific Traffic Volatility

**Feature:**  
Standard deviation of delivery time grouped by `(route_id, traffic_level)`

#### Rationale
Mean delivery time hides risk.

Some routes are:
- Stable but slow
- Fast but volatile
- Highly sensitive to traffic shifts

This feature explicitly encodes **uncertainty**, not just expectation.

#### Observed Impact
- Significant reduction in missed late deliveries
- Recall increased to **96.6%**
- Models began learning *risk contours*, not averages

---

### 2️⃣ Heavy Vehicle × Traffic Interaction Flag

**Feature:** `is_heavy_traffic_truck`

#### Rationale
Error diagnostics revealed:
- Trucks under medium traffic experienced ~**30% higher error rates**
- This interaction was weakly learned implicitly

Rather than hoping the model discovers this, the interaction is **made explicit**.

#### Observed Impact
- False negatives reduced by **29%**
- Improved robustness in congested conditions
- More stable predictions across traffic regimes

---

### 3️⃣ High-Fidelity One-Hot Encoding

**Applied To**
- `traffic_level`
- `vehicle_type`
- `weather`

#### Why This Matters
Ordinal encoding implies:
> “Medium traffic is halfway between low and high.”

Operationally, this is false.

#### Results
- Nonlinear models gained expressive freedom
- Validation stability improved
- Accuracy stabilized at **94.3%**
- Reduced variance across random seeds

---

## 🧪 Feature Selection, Stability & Drift Readiness

### Evaluation Methodology
Feature selection was conducted as a **robustness exercise**, not a pruning exercise.

- Time-aware 80/20 split
- Gradient Boosting Regressor
- Permutation importance evaluated on **unseen data**
- Cross-referenced with gain-based importance

### Explicitly Identified Low-Value Features  
*(Documented — not silently removed)*

- `night_peak_conflict`
- `is_return_route`
- `route_std_distance`
- `city_pair_complexity`

These features exhibited:
- Near-zero entropy
- No permutation signal
- No contribution to generalization

> Low-value features are **reported**, not buried.

### Artifact
- `Feature_Stability_and_Drift_Readiness_analysis.ipynb`

---

## 📦 Final Dataset Characteristics

### Dataset Summary
- ~70,000 records
- ~28 high-signal, validated features
- Zero missing values
- Temporal safety guaranteed
- Model-agnostic design

### Feature Taxonomy
- **Temporal:** cyclical & categorical time signals
- **Spatial:** route-aware intelligence
- **Operational:** vehicle–environment interactions
- **Risk-Aware:** volatility & stress indicators

### Intended Downstream Usage
- Regression models
- Gradient boosting frameworks
- Probabilistic forecasting
- Delay-risk classification layers

---

## 🔐 Validation, Audits & Safeguards

This dataset has passed:
- Temporal leakage audits
- Feature evolution tracking
- Stability testing across time splits
- Distribution shift readiness checks

> Downstream modeling can proceed **without hidden structural traps**.

---

## ⚠️ Known Constraints & Design Assumptions

- Traffic data is categorical, not real-time telemetry
- Route behavior assumed stationary within observation window
- No external GPS, IoT, or sensor feeds
- No online learning or adaptive retraining

These are **explicit architectural constraints**, not oversights.

---

## 🛠 What Remains Intentionally Out of Scope

This repository ends at the **dataset boundary**.

Planned downstream extensions include:
- Model training pipelines
- Prediction interval estimation
- Calibration analysis
- Cost-sensitive loss functions
- Production monitoring & drift alerts

These steps are **downstream by design**, not missing work.

---

## 📌 Final Statement

This project does not attempt to chase benchmark scores.

It establishes:
- Data trust
- Feature legitimacy
- Operational realism
- Scientific reproducibility

**Models will change.  
Infrastructure will evolve.  
A disciplined dataset endures.**

---
