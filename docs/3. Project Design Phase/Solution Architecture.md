# Solution Architecture

**Project:** Credit Card Approval Prediction

---

## Architecture Diagram (3-Layer)

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│                  (Browser — Bootstrap 5)                     │
│                                                             │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐   │
│  │  Dashboard    │  │ Predict Form  │  │   History     │   │
│  │  (index.html) │  │(predict.html) │  │(history.html) │   │
│  │               │  │               │  │               │   │
│  │ • Model stats │  │ • 15 inputs   │  │ • Last 10     │   │
│  │ • Scenario    │  │ • Result card │  │   predictions │   │
│  │   pre-fill    │  │ • Confidence  │  │ • Summary     │   │
│  └───────────────┘  └───────────────┘  └───────────────┘   │
└─────────────────────────────┬───────────────────────────────┘
                              │ HTTP Request
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                          │
│                    (Flask on Render)                         │
│                                                             │
│  ┌──────────────┐   ┌─────────────────┐   ┌─────────────┐  │
│  │ Flask Routes │   │ preprocess_     │   │  Session    │  │
│  │              │   │ input()         │   │  Manager    │  │
│  │ GET  /       │──►│                 │──►│             │  │
│  │ GET  /predict│   │ • LabelEncode   │   │ Max 10      │  │
│  │ POST /predict│   │   categoricals  │   │ predictions │  │
│  │ GET  /history│   │ • StandardScale │   │ stored per  │  │
│  │ POST /clear  │   │   numerics      │   │ browser     │  │
│  └──────────────┘   └─────────────────┘   └─────────────┘  │
└─────────────────────────────┬───────────────────────────────┘
                              │ Feature Vector
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    ML / DATA LAYER                           │
│               (Serialized PKL Artifacts)                     │
│                                                             │
│  ┌──────────────┐  ┌─────────────┐  ┌────────────────────┐  │
│  │  model.pkl   │  │ scaler.pkl  │  │   encoder.pkl      │  │
│  │              │  │             │  │                    │  │
│  │ Random Forest│  │  Standard   │  │  LabelEncoders     │  │
│  │ n_estimators │  │  Scaler     │  │  for 5 categorical │  │
│  │ =100         │  │  (14 num    │  │  columns           │  │
│  │ class_weight │  │  features)  │  │                    │  │
│  │ ='balanced'  │  │             │  │                    │  │
│  └──────────────┘  └─────────────┘  └────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                   metadata.pkl                        │   │
│  │  • Model comparison (LR, DT, RF, XGBoost metrics)   │   │
│  │  • Best model name + accuracy                        │   │
│  │  • Feature column order (cat + num)                  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Deployment Architecture

```
Developer Machine          GitHub (master)          Render (Production)
─────────────────    ──────────────────────    ─────────────────────────────
  Code Changes   ──► git push origin master ──► Auto-deploy triggered
  train_model.py      ↕                         pip install -r requirements.txt
  app.py              CI/CD Pipeline            gunicorn app:app
  templates/                                    Flask app served on HTTPS
  static/
  models/*.pkl
```

---

## Component Summary

| Component | Technology | Purpose |
|---|---|---|
| Web Server | Gunicorn 21.2.0 | WSGI server running Flask on Render |
| Web Framework | Flask 3.1.2 | Routes, session management, template rendering |
| UI Framework | Bootstrap 5.3 | Responsive layout and components |
| ML Model | Random Forest (Scikit-learn 1.8.0) | Binary classification of applicants |
| Preprocessing | StandardScaler + LabelEncoder | Feature normalization and encoding |
| Model Storage | Joblib PKL files | Fast serialization of 4 artifacts |
| Hosting | Render (free tier) | Zero-cost public HTTPS deployment |
| CI/CD | GitHub → Render auto-deploy | Push to master triggers production update |
