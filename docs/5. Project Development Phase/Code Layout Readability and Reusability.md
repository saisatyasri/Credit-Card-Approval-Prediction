# Code Layout Readability and Reusability

**Project:** Credit Card Approval Prediction

---

## Code Quality Checklist

| # | Quality Criterion | Status | Evidence |
|---|---|---|---|
| 1 | **Consistent Indentation** | ✅ Pass | All Python files use 4-space indentation; HTML templates use 2-space indentation consistently |
| 2 | **Meaningful File Names** | ✅ Pass | `train_model.py`, `app.py`, `preprocess_input()`, `build_target()`, `engineer_features()` — all self-descriptive |
| 3 | **Meaningful Variable Names** | ✅ Pass | `BAD_STATUSES`, `CATEGORICAL_COLS`, `NUMERIC_COLS`, `scale_pos_weight`, `IS_UNEMPLOYED` — no ambiguous single-letter names |
| 4 | **Modular Function Design** | ✅ Pass | `train_model.py` split into: `load_data()`, `build_target()`, `engineer_features()`, `preprocess()`, `train_all_models()`, `save_plots()` |
| 5 | **Single Responsibility** | ✅ Pass | Each function handles one task; `app.py` handles routing only, preprocessing is isolated in `preprocess_input()` |
| 6 | **Reusable Preprocessing** | ✅ Pass | `encoder.pkl` and `scaler.pkl` are shared between training (`train_model.py`) and inference (`app.py`) — single source of truth |
| 7 | **No Redundant Code** | ✅ Pass | Model training loop avoids copy-paste; model comparison is data-driven via the `models` dict |
| 8 | **Error Handling** | ✅ Pass | `MODELS_LOADED` flag in `app.py` prevents crashes when PKL files are missing; Flask handles invalid routes gracefully |

**Overall Code Quality Rating: 5 / 5**

---

## Project File Structure

```
Credit Card Approval Prediction/
├── app.py                          # Flask web application (4 routes)
├── train_model.py                  # ML training pipeline
├── requirements.txt                # Python dependencies
├── Procfile                        # Gunicorn start command for Render
├── render.yaml                     # Render deployment configuration
├── .gitignore                      # Excludes data/, .env, __pycache__
│
├── templates/                      # Jinja2 HTML templates
│   ├── base.html                   # Shared layout: navbar, Bootstrap CDN
│   ├── index.html                  # Dashboard: model stats + scenario cards
│   ├── predict.html                # Prediction form + result display
│   └── history.html                # Session history listing
│
├── static/
│   ├── css/style.css               # Banking theme: navy + gold CSS variables
│   └── js/script.js                # Scenario pre-fill + confidence bar JS
│
├── models/                         # Trained model artifacts (committed to git)
│   ├── model.pkl                   # Best model: Random Forest
│   ├── scaler.pkl                  # StandardScaler (fitted on training data)
│   ├── encoder.pkl                 # LabelEncoders (5 categorical features)
│   └── metadata.pkl                # Model comparison dict + feature column order
│
├── notebooks/
│   └── Credit_Card_Approval_Analysis.ipynb  # EDA + model experimentation
│
└── docs/                           # 8-phase project documentation (this folder)
```
