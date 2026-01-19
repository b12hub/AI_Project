# Model Suitability Analysis
**Context**: Logistics ETA Prediction
**Author**: Principal Machine Learning Architect

---

## 1. Dataset Characteristics Analysis

Based on the Block-5 preprocessing and Block-6 definitions, the dataset presents specific challenges:

*   **Feature Types**:
    *   **Numerical**: `distance_km`, `traffic_stress`, `efficiency` ratios. (Dense, continuous).
    *   **Categorical (One-Hot)**: `vehicle_type`, `weather`. (Sparse binary).
    *   **High Cardinality**: `route_id`, `destination_city`. (Potentially thousands of unique values).
*   **Non-Linear Interactions**:
    *   **High Probability**: Traffic impact is non-linear with respect to time of day (`is_peak_hour`) and weather. A truck in rain at 5 PM behaves differently than a truck in rain at 3 AM. Linear models will miss this interaction unless manually engineered.
*   **Noise & Outliers**:
    *   Logistics data is inherently stochastic (accidents, random delays).
    *   **Implication**: Models using squared error (RMSE) are sensitive to these "force majeure" outliers. MAE robustness is critical.
*   **Temporal Drift**:
    *   Traffic patterns change seasonally. A model trained on summer data may fail in winter.
    *   **Risk**: Models that over-memorize `route_id` specific patterns (e.g., Random Forest with deep trees) are at high risk of degrading on the **Future Test Set**.

---

## 2. Regression Model Analysis (Target: `delivery_time_hours`)

### A. Linear / Ridge / Lasso
*   **Suitability**: **Low to Moderate**.
*   **Fit**:
    *   **Pros**: Ultra-low latency (<1ms), fully interpretable coefficients.
    *   **Cons**: Fails to capture the critical non-linearities (Traffic × Weather) without massive manual feature crossing.
*   **Bias/Variance**: High Bias (Underfitting), Low Variance.
*   **Verdict**: Use as the **Baseline**. If XGBoost doesn't beat this by 15%, the problem is likely signal-poor, not model-poor.

### B. Random Forest Regressor
*   **Suitability**: **Moderate**.
*   **Fit**:
    *   **Pros**: Handles non-linearities naturally. Robust to outliers (averaging leaf nodes minimizes impact of extreme delays). No scaling strictly required.
    *   **Cons**: **Extrapolation failure**. Trees cannot predict values outside the range of the training set. If future delays are longer than historical max, RF caps the prediction.
    *   **Latency**: High. deeply nested trees require many comparisons. Might breach the 50ms limit if `n_estimators` is high.
*   **Bias/Variance**: Low Bias, High Variance (Risk of overfitting specific routes).

### C. Gradient Boosting (XGBoost / LightGBM)
*   **Suitability**: **High**.
*   **Fit**:
    *   **Pros**: State-of-the-art for tabular data. Can handle missing values (though we preprocessed them). loss functions (MAE-based objectives) can be directly optimized.
    *   **Drift Resistance**: Regularization (L1/L2) and lower depth often generalize better than deep RFs on time-split data.
*   **Latency**: Very fast inference if tree depth is constrained (e.g., `max_depth=6`).
*   **Bias/Variance**: Low Bias, Tunable Variance.

### **Regression Ranking**
1.  **XGBoost/LightGBM** (Best tradeoff)
2.  **Random Forest** (Strong fallback, watch size)
3.  **Linear Regression** (Baseline only)

---

## 3. Classification Model Analysis (Target: Delay Risk)

### A. Logistic Regression
*   **Suitability**: **High (for calibration)**.
*   **Fit**:
    *   Produces well-calibrated probabilities $P(Delayed)$.
    *   Essential for risk scoring (e.g., "70% chance of delay").
*   **Recall**: Hard to tune specific recall without moving thresholds arbitrarily.

### B. Random Forest Classifier
*   **Suitability**: **High**.
*   **Fit**:
    *   **Class Imbalance**: `class_weight='balanced'` works exceptionally well in RF to boost Recall on the minority "Delayed" class.
    *   **Multi-class**: Naturally handles "On-time" vs "Slight" vs "Major" without One-vs-All complexity.

### C. Gradient Boosting Classifier
*   **Suitability**: **Moderate to High**.
*   **Fit**:
    *   Often wins on raw F1-score, but probability calibration can be worse than Logistic Regression without post-processing (Isotonic Regression).
    *   Higher complexity to tune for class imbalance (scale_pos_weight).

### **Classification Ranking**
1.  **Random Forest** (Best specifically for Imbalance/Recall ease)
2.  **XGBoost** (Best raw performance, harder to calibrate)
3.  **Logistic Regression** (Best baseline)

---

## 4. Baseline Comparison Logic

*   **Beating the Mean**:
    *   Any model utilizing `distance_km` **MUST** beat the Mean Predictor. The correlation is physical and strong.
    *   If a model fails here, the feature pipeline is broken.
*   **Beating Linear Regression**:
    *   The 15% improvement target implies capturing **Congestion**.
    *   Linear models see "5pm". Tree models see "5pm on a Friday in Rain".
    *   **Expectation**: XGBoost should beat Linear by ~20-25% MAE due to these interactions.
    *   **Warning**: If XGBoost $\approx$ Linear, it implies traffic/weather features have no predictive power, and traffic is purely random.

---

## 5. Final Recommendation

### Primary Regression Model: **XGBoost (Regressor)**
*   **Justification**:
    *   Directly optimizes non-squared errors (MAE-like objectives available).
    *   Best handling of tabular interactions.
    *   Inference speed is tunable via tree limits to satisfy <50ms.
    *   **Configuration**: Small learning rate ($<0.05$), `max_depth` 4-8, `subsample` 0.8 to prevent overfitting time-splits.

### Fallback Regression Model: **Random Forest**
*   **Trigger**: If XGBoost proves unstable across validation folds or requires excessive tuning time.
*   **Constraint**: Limit `max_depth` and `n_estimators` to ensure latency compliance.

### Primary Classification Model: **Random Forest (Classifier)**
*   **Justification**:
    *   The business priority is **Recall** (catching delays). RF's `class_weight='balanced'` is the most robust "out-of-the-box" method to penalize False Negatives.
    *   Multi-class handling is native and interpretable (voting probability).

### Decision Check against BLOCK-6 Rules
*   **Parsimony**: We start with XGBoost. It is complex, but the expected gain (>20%) justifies it over Linear.
*   **Latency**: XGBoost is generally faster than RF for inference (additive vs averaging many deep trees).
*   **Overfitting**: Both recommended families support strict regularization.

---

**Next Actions**: Proceed to Block-7 Training using **XGBoost** for ETA and **Random Forest** for Risk Class.
