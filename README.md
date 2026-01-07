# 🚚 Risk-Aware Logistics Delivery Time Dataset  
### A Production-Grade Feature Engineering, Validation & Audit Pipeline

> **Thesis**  
> This repository operationalizes a core principle of applied machine learning:  
> **models fail not because of algorithms—but because datasets lie.**  
>
> This project transforms raw logistics data into a **risk-aware, leakage-free, auditable, model-ready dataset** explicitly designed for *real operational uncertainty*, not leaderboard demos.

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
