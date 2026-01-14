# BLOCK-6: Problem Definition & Model Strategy

**Author**: Principal Machine Learning Architect
**Date**: 2026-01-14
**Status**: DRAFT LOCAL

---

## 1. Problem Framing (Core ML Tasks)

This system addresses three distinct machine learning problems to optimize logistics operations.

### A. Regression (Primary Task)
**Target**: `delivery_time_hours` (Continuous)
**Goal**: Minimize the error between predicted and actual delivery times.
**Business Value**:
- Accurate ETAs improve customer satisfaction.
- Enables precise scheduling and fleet optimization.
- Reduces idle time and overtime costs for drivers.

### B. Classification (Operational Task)
**Target**: Derived categorical status from `delivery_time_hours` vs `expected_time_no_traffic`.
**Goal**: flag deliveries at risk of varying degrees of delay.

1.  **Binary Classification**:
    - **Classes**: `On-time` vs `Delayed`
    - **Threshold**: `Derived Actual > Expected + Buffer` (e.g., 15 mins)

2.  **Multi-class Classification**:
    - **Class 0: On-time**: `Actual <= Expected`
    - **Class 1: Slight Delay**: `Expected < Actual < Expected + 0.5h`
    - **Class 2: Major Delay**: `Actual >= Expected + 0.5h`
    - **Use Case**: Prioritizing intervention for "Major Delay" production tickets.

### C. Anomaly Detection (Risk & Monitoring)
**Target**: Outlier detection in feature space and error space.
**Scope**:
- **Unusual Routes**: Distance/Time mismatches.
- **Abnormal Delays**: Deliveries taking 3x standard deviation > mean.
- **Cost/Time Outliers**: Extreme values that might skew training or indicate fraud/accidents.
**Production Role**: Acts as a "Check Engine" light to trigger manual review or exclude data from automated retraining.

---

## 2. Baseline Models (Non-Negotiable)

Baselines provide the minimum performance floor. Any complex model must significantly outperform these to justify deployment.

### Regression Baselines
1.  **Mean Predictor**: Predicts the global average of `delivery_time_hours` from train set.
    - *Purpose*: Measures absolute zero-skill level.
2.  **Linear Regression**: Standard OLS on scaled features.
    - *Purpose*: Establishes linear separability and feature importance directionality.
    - *Success*: If a complex model doesn't beat OLS by >5%, OLS is preferred for interpretability.

### Classification Baselines
1.  **DummyClassifier**: Always predicts the most frequent class (e.g., "On-time").
    - *Purpose*: Checks class imbalance impact.
2.  **Logistic Regression**: Simple linear decision boundary.
    - *Purpose*: Baseline for probability calibration.

---

## 3. Candidate Model Families

| Task | Model | Why It Fits | Risk |
| :--- | :--- | :--- | :--- |
| **Regression** | **Linear / Ridge / Lasso** | High interpretability, fast inference, robust to noise. | **Underfitting**: likely misses complex traffic patterns. |
| **Regression** | **Random Forest** | Captures non-linear interactions (e.g., Rush Hour × Rain) without scaling. | **Overfitting**: can memorize unique routes if distinct count is high. |
| **Regression** | **XGBoost / LightGBM** | SOTA for tabular data; handles missing values and complex splits best. | **Complexity**: Harder to tune; "black box" nature. |
| **Classification** | **Logistic Regression** | Provides well-calibrated probabilities for risk scoring. | Limited expressiveness for complex decision boundaries. |
| **Classification** | **Random Forest** | Robust to outliers and inherently handles multi-class well. | Large model size can increase latency. |
| **Anomaly** | **Isolation Forest** | Efficiently identifies anomalies in high-dimensional space; unsupervised. | **Hard Thresholds**: defining "contamination" factor is rigorous. |

---

## 4. Evaluation Metrics (Locked)

### Regression
*   **MAE (Mean Absolute Error) [PRIMARY]**:
    *   *Why*: Logistics operates in "real minutes". An error of 10 minutes is 10 minutes. RMSE penalizes outliers (squares errors), which might be unfair if the outlier is a true "force majeure" event. MAE is more robust and business-interpretable.
*   **RMSE (Root Mean Square Error)**:
    *   *Why*: Secondary metric to detect large variance/outliers.
*   **R² (Coefficient of Determination)**:
    *   *Why*: Explanatory power only (variance explained).

### Classification
*   **Precision / Recall**:
    *   *Business Context*:
        *   **False Positive (Type I)**: Predicting delay when on-time. Cost: Unnecessary specific intervention.
        *   **False Negative (Type II)**: Predicting on-time when delayed. Cost: **High** (Customer anger, SLA breach).
    *   *Focus*: Recall on "Delayed" class is prioritized.
*   **F1-Score (Macro)**: Balances performance across all classes.

### Anomaly Detection
*   **Alert Rate**: % of instances flagged.
*   **Precision**: % of flags that are truly actionable/abnormal (requires manual sampling).

---

## 5. Validation Strategy (Time-Aware)

**CRITICAL RULE**: NO RANDOM SHUFFLING.

### Methodology
1.  **Temporal Splitting**:
    *   Strict adherence to `Order Date`.
    *   **Train**: Past Data (70%)
    *   **Validation**: Recent Past (15%)
    *   **Test**: Future (15%)
2.  **Why Time-Based?**:
    *   Logistics patterns evolve (seasonality, road changes, fleet updates).
    *   Random K-Fold leaks future traffic patterns into the past, inflating metrics (Look-ahead Bias).
3.  **Reuse BLOCK-5**:
    *   The split indices generated in Block 5 must be identically applied here.

---

## 6. Model Selection Decision Rules

1.  **Parsimony Principle**:
    *   If `MAE(Linear) ≈ MAE(XGBoost)` (within 2%), choose **Linear**.
2.  **Stability Check**:
    *   If `Metric(Train) >> Metric(Validation)` (>15% gap), the model is overfitting. **DISQUALIFY**.
3.  **Latency Constraint**:
    *   Inference time must be < 50ms per record on CPU.
4.  **Baseline Beat**:
    *   Final model must improve MAE by at least **15%** over Mean Predictor.

---

## 7. Deliverables of BLOCK-6

*   [x] **Problem Definitions**: Regression (ETA), Classification (Delay Risk), Anomaly (Health).
*   [x] **Target Formulations**: Defined thresholds for delays.
*   [x] **Baseline Expectations**: Mean/OLS/Dummy established.
*   [x] **Approved Model Families**: Linear, RF, GBM, Isolation Forest.
*   [x] **Approved Metrics**: MAE (Primary), Precision/Recall.
*   [x] **Go/No-Go Criteria**: 15% improvement over baseline required for BLOCK-7.

**Next Step**: Prepare for **BLOCK-7: Model Training & Tuning** using these definitions.
