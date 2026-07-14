# Project Documentation

**Project:** Credit Card Approval Prediction
**Team:** sirisha, satya,prasanna,sravya,hansraj

---

## Milestone 1: Data Collection

### Dataset Source

The project uses the publicly available **Credit Card Approval Prediction** dataset from Kaggle (CC0 license), published by rikdifos. The dataset contains real anonymized credit application records from a financial institution.

**Dataset:** `rikdifos/credit-card-approval-prediction`

### Files

| File | Rows | Columns | Description |
|---|---|---|---|
| `application_record.csv` | 438,557 | 18 | One row per applicant with demographic and financial attributes |
| `credit_record.csv` | 1,048,575 | 3 | Monthly credit behavior records per applicant (ID, MONTHS_BALANCE, STATUS) |

### Key Columns — application_record.csv

| Column | Type | Description |
|---|---|---|
| ID | Integer | Unique applicant identifier (join key) |
| CODE_GENDER | Categorical | M/F |
| FLAG_OWN_CAR | Categorical | Y/N |
| FLAG_OWN_REALTY | Categorical | Y/N |
| CNT_CHILDREN | Integer | Number of children |
| AMT_INCOME_TOTAL | Float | Annual income |
| NAME_INCOME_TYPE | Categorical | Working, Pensioner, Commercial associate, etc. |
| NAME_EDUCATION_TYPE | Categorical | Higher education, Secondary, Academic degree, etc. |
| NAME_FAMILY_STATUS | Categorical | Married, Single, Separated, etc. |
| NAME_HOUSING_TYPE | Categorical | House/apartment, Rented apartment, etc. |
| DAYS_BIRTH | Integer | Days since birth (negative — older → more negative) |
| DAYS_EMPLOYED | Integer | Days since employment start (365243 = unemployed) |
| OCCUPATION_TYPE | Categorical | Laborers, Core staff, Managers, etc. |
| CNT_FAM_MEMBERS | Float | Number of family members |

### Key Columns — credit_record.csv

| Column | Description |
|---|---|
| ID | Applicant identifier (foreign key) |
| MONTHS_BALANCE | Months relative to current month (0 = current, -1 = last month) |
| STATUS | Credit behavior: 0=no debt, 1=30-59 DPD, 2=60-89 DPD, 3=90-119 DPD, 4=120-149 DPD, 5=150+ DPD, C=closed, X=no credit |

---

## Milestone 2: Exploratory Data Analysis (EDA)

### Key Findings

1. **Gender distribution:** 66.7% Female, 33.3% Male applicants
2. **Car ownership:** 34.3% own a car; 69.8% own real estate
3. **Income distribution:** Right-skewed; median ~₹1,57,500 (scaled from raw USD values)
4. **Age distribution:** Peak applicants aged 35-50 years
5. **Employment duration:** Wide distribution; 365243 sentinel value identifies unemployed applicants
6. **Income type:** Working (52%) and Commercial associate (22%) are most common
7. **Missing values:** OCCUPATION_TYPE has 31.2% missing values — imputed with "Unknown"
8. **Class distribution (post-target engineering):** ~87% Approved, ~13% Rejected

### EDA Notebook

Full EDA with visualizations available in: `notebooks/Credit_Card_Approval_Analysis.ipynb`

Sections: Setup → Data Loading → EDA → Target Engineering → Feature Engineering → Preprocessing → Model Training → Model Comparison → Classification Reports → Best Model Selection

---

## Milestone 3: Feature Engineering & Preprocessing

### Target Variable Engineering

Credit behavior from `credit_record.csv` is mapped to a binary label:

```
STATUS 1-5 (30+ days past due at any point) → Rejected (0)
STATUS 0/C/X only (no late payments)         → Approved (1)
STATUS X only (no credit evaluated)          → Excluded
```

This logic mirrors real-world bank risk assessment: any historical late payment flags the applicant as high-risk.

### Derived Features

| Feature | Formula | Rationale |
|---|---|---|
| AGE_YEARS | `-DAYS_BIRTH / 365` | More interpretable than days; banks care about applicant age |
| YEARS_EMPLOYED | `-DAYS_EMPLOYED / 365` (0 if unemployed) | Employment stability is a strong credit predictor |
| IS_UNEMPLOYED | `1 if DAYS_EMPLOYED == 365243 else 0` | Binary flag for unemployment (sentinel value 365243) |
| INCOME_PER_MEMBER | `AMT_INCOME_TOTAL / CNT_FAM_MEMBERS` | Income adequacy relative to household size |

### Preprocessing Pipeline

1. **Categorical encoding:** `LabelEncoder` applied to 5 categorical columns — saved as `encoder.pkl`
2. **Numerical scaling:** `StandardScaler` applied to 14 numerical columns — saved as `scaler.pkl`
3. **Feature order:** Categorical features first, then numerical — must match exactly at inference time

---

## Milestone 4: Model Training & Comparison

### Class Imbalance Handling

The dataset has an 87%/13% class imbalance (Approved/Rejected). All models use balanced weights:
- Scikit-learn models: `class_weight='balanced'`
- XGBoost: `scale_pos_weight = neg_count / pos_count`

### Model Training Results

| Model | Accuracy | ROC-AUC | Training Notes |
|---|---|---|---|
| Logistic Regression | 74.3% | 0.81 | L2 regularization, max_iter=1000 |
| Decision Tree | 76.8% | 0.77 | Default depth; prone to overfitting |
| **Random Forest** | **81.91%** | **0.89** | n_estimators=100, best overall model |
| XGBoost | 79.5% | 0.87 | scale_pos_weight=6.7 (neg/pos ratio) |

**Best Model:** Random Forest (highest accuracy + ROC-AUC)

All model metrics are saved in `models/metadata.pkl` and displayed on the dashboard.

---

## Milestone 5: Flask Web Application Development

### Application Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Dashboard — model comparison table + scenario cards |
| `/predict` | GET | Blank prediction form |
| `/predict` | POST | Form submission → preprocessing → ML inference → result |
| `/history` | GET | Session history of last 10 predictions |
| `/clear_history` | POST | Clear session history |

### Preprocessing at Inference (`preprocess_input()`)

1. Extract 5 categorical values from form → `LabelEncoder.transform()` → array
2. Extract 14 numerical values from form → `StandardScaler.transform()` → scaled array
3. Concatenate: `[cat_encoded] + [num_scaled]` → 19-element feature vector
4. Reshape to `(1, 19)` → `model.predict()` + `model.predict_proba()`

### Frontend Architecture

- **base.html:** Shared layout with Bootstrap 5.3 CDN, Bootstrap Icons, navbar
- **index.html:** Hero section, model comparison table (from metadata.pkl), scenario cards with JS pre-fill
- **predict.html:** 4-section form (Personal, Financial, Employment, Education & Housing), result card with animated confidence bar
- **history.html:** Summary statistics (approved_count via Jinja2 selectattr), collapsible prediction detail cards
- **style.css:** CSS variables `--primary-blue: #1a3a6b`, `--accent-gold: #c8a84b`, fadeInUp animation for result card
- **script.js:** `SCENARIOS` object, `fillScenario()`, `updateIncomeDisplay()`, `updateUnemployed()`, `animateProgressBars()`

---

## Milestone 6: Deployment

### Render Deployment Configuration

**Procfile:**
```
web: gunicorn app:app
```

**render.yaml:**
```yaml
services:
  - type: web
    name: credit-card-approval-prediction
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

### Deployment Steps

1. Committed all source code + `models/*.pkl` artifacts to GitHub `master` branch
2. Connected GitHub repository to Render via Render dashboard
3. Render automatically installs dependencies and starts Gunicorn on each push to master
4. Application served at: **https://credit-card-approval-prediction-ra22.onrender.com**

### CI/CD Pipeline

Every `git push origin master` triggers:
1. Render detects new commit
2. Pulls latest code
3. Runs `pip install -r requirements.txt`
4. Starts `gunicorn app:app`
5. New deployment live in ~2 minutes
