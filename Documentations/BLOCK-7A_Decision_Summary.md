## BLOCK-7A — Model Selection & Decision Summary  
### Regression Training (XGBoost + Linear Baseline)

### Objective  
The objective of **BLOCK-7A** was to identify a high-performance regression model that achieves **strong predictive accuracy while maintaining controlled generalization behavior**, suitable for production deployment.  
XGBoost was selected as the primary candidate due to its ability to model nonlinear interactions, while a Linear Regression baseline was retained for benchmarking and sanity validation.

---

### Model Evaluation Strategy  

To ensure robust selection, each XGBoost configuration was evaluated using the following metrics:

- **Train MAE** — Measures in-sample fit  
- **Validation MAE** — Primary optimization target  
- **Generalization Gap (%)** —  
  \[
  \text{Gap} = \frac{\text{Val MAE} - \text{Train MAE}}{\text{Train MAE}} \times 100
  \]

A **gap threshold of < 8%** was enforced to explicitly prevent overfitting.

---

### Selection Rule  

The final model was chosen using a **two-stage decision rule**:

1. **Filter Stage**  
   - Discard all models with generalization gap ≥ 8%

2. **Optimization Stage**  
   - Among the remaining candidates, select the model with the **lowest Validation MAE**

This approach ensures that **generalization stability is treated as a constraint**, while **predictive accuracy remains the optimization objective**.

---

### Decision Rationale  

Although certain configurations exhibited extremely low generalization gaps (≈1–2%), these models demonstrated **inferior validation performance**.  
The selected configuration achieved:

- **Lower Validation MAE**
- **Acceptable generalization gap (≈3–4%)**
- **Balanced bias–variance tradeoff**

This confirms that **minimal gap alone is not sufficient** for model selection; **validation performance must dominate once generalization safety is satisfied**.

---

### Baseline Comparison  

A Linear Regression baseline was trained in parallel to:

- Establish a performance floor  
- Validate dataset linear separability assumptions  

The XGBoost model significantly outperformed the baseline, confirming the presence of **nonlinear feature interactions** and justifying the use of a tree-based ensemble.

---

### Final Decision  

The selected XGBoost model is designated as the **Champion Model** for downstream evaluation and comparison phases due to:

- Superior validation accuracy  
- Controlled overfitting behavior  
- Production-ready stability characteristics  

This model is advanced to **BLOCK-7B** for comparative benchmarking and final validation.

---
