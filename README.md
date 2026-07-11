# Credit Card Approval Prediction

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-brightgreen)](https://credit-card-approval-prediction-ra22.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-lightgrey)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> An AI-powered web application that predicts credit card approval decisions using machine learning — trained on 438,000+ real applicant records from Kaggle.

**Live Application:** https://credit-card-approval-prediction-ra22.onrender.com

---

## About the Project

Banks receive thousands of credit card applications daily, making manual review time-consuming and error-prone. This project automates the approval decision using machine learning — four classification algorithms (Logistic Regression, Decision Tree, Random Forest, XGBoost) are trained on historical applicant data including income, employment, credit history, and demographics. The best-performing model is integrated into a Flask web application that provides instant Approved/Rejected predictions with confidence scores through an intuitive banking-themed UI.

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│   Dashboard  │  Prediction Form  │  Result  │  History      │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                   APPLICATION LAYER (Flask)                  │
│   Route Handling  →  Form Validation  →  Preprocessing       │
│                   →  Load ML Model   →  Return Result        │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                  MACHINE LEARNING LAYER                      │
│   Logistic Regression  │  Random Forest  ← Best             │
│   Decision Tree        │  XGBoost                           │
│   StandardScaler       │  LabelEncoders  │  metadata.pkl    │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                      DATA LAYER                              │
│   application_record.csv (438K rows)                        │
│   credit_record.csv (1M rows) — Kaggle Dataset              │
└─────────────────────────────────────────────────────────────┘
```

---

## Model Performance Comparison

| Model | Accuracy | ROC-AUC | Status |
|---|---|---|---|
| **Random Forest** | **81.91%** | **0.7252** | Best Model |
| Logistic Regression | 55.83% | 0.5537 | Evaluated |
| Decision Tree | 55.23% | 0.5979 | Evaluated |
| XGBoost | 72.83% | 0.6978 | Evaluated |

> All models trained with `class_weight='balanced'` to handle 87%/13% class imbalance.

---

## Features

| Feature | Description |
|---|---|
| Model Comparison Dashboard | Visual comparison of all 4 models with accuracy bars |
| Prediction Form | 15-field applicant input form with validation |
| Instant Result | Approved/Rejected with animated confidence score bar |
| Prediction History | Last 10 predictions stored in session |
| Scenario Cards | Pre-fill Low / Medium / High risk applicant examples |
| Income Formatter | Real-time currency display as you type |
| Responsive UI | Mobile + desktop compatible (Bootstrap 5) |
| Auto-Deployment | Push to GitHub → Render redeploys automatically |

---

## Project Structure

```
Credit-Card-Approval-Prediction/
├── app.py                  # Flask web application
├── train_model.py          # ML training pipeline
├── requirements.txt        # Python dependencies
├── Procfile                # Render startup command
├── render.yaml             # Render deployment config
├── models/
│   ├── model.pkl           # Trained Random Forest model
│   ├── scaler.pkl          # StandardScaler
│   ├── encoder.pkl         # LabelEncoders dict
│   └── metadata.pkl        # Model comparison metrics
├── templates/
│   ├── base.html           # Master layout
│   ├── index.html          # Dashboard
│   ├── predict.html        # Prediction form + result
│   └── history.html        # Prediction history
├── static/
│   ├── css/style.css       # Banking theme CSS
│   └── js/script.js        # Form helpers + animations
├── notebooks/
│   └── Credit_Card_Approval_Analysis.ipynb  # EDA + training notebook
└── docs/                   # Project documentation (8 phases)
```

---

## Setup & Run Locally

### Prerequisites
- Python 3.12+
- Kaggle account (for dataset download)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/karthik-ganti/Credit-Card-Approval-Prediction.git
cd Credit-Card-Approval-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download dataset (place in data/ folder)
kaggle datasets download -d rikdifos/credit-card-approval-prediction -p data/ --unzip

# 4. Train the models
python train_model.py

# 5. Run the web application
python app.py
```

Visit `http://localhost:5000`

---

## Dataset

| File | Rows | Description |
|---|---|---|
| `application_record.csv` | 438,557 | Applicant demographics and financial info |
| `credit_record.csv` | 1,048,575 | Monthly payment history per applicant |

**Source:** [Kaggle — Credit Card Approval Prediction](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction)
**License:** CC0 1.0 (Public Domain)

### Target Variable Engineering

| STATUS Code | Meaning | Label |
|---|---|---|
| C | Paid off that month | Approved (1) |
| 0 | 1-29 days past due | Approved (1) |
| 1 | 30-59 days past due | **Rejected (0)** |
| 2-5 | 60+ days / bad debt | **Rejected (0)** |
| X | No loan that month | Approved (1) |

---

## Team

| Name | Role | Email |
|---|---|---|
| Karthik Ganti | Team Lead | karthikganti0788@gmail.com |
| Joy Kumar Roy | App Development | 23p31a0522@acet.ac.in |
| Nandini Priya Masina | Data Analysis & EDA | nandinipriyachowdary@gmail.com |
| Kunisetti Uma Nandeswari | Data Preprocessing | umanandeswarik520@gmail.com |
| Kantipudi Vivek Vardhan | Feature Engineering & Models | vivekkantipudi09@gmail.com |

---

## Deployment

Deployed on **Render** (free tier) with automatic GitHub integration.

- **Live URL:** https://credit-card-approval-prediction-ra22.onrender.com
- **Hosting:** Render Web Service (Python 3, Singapore region)
- **Auto-deploy:** Every push to `master` triggers a new deployment

> Note: The free Render instance sleeps after 15 minutes of inactivity. First load may take 30-60 seconds to wake up.

---

## Documentation

Complete project documentation is available in the [`docs/`](docs/) folder, organized into 8 phases matching the IBM Skills Build AI/ML project template:

| Phase | Documents |
|---|---|
| [1. Brainstorming & Ideation](docs/1.%20Brainstorming%20%26%20Ideation/) | Idea Prioritization, Problem Statements, Empathy Map |
| [2. Requirement Analysis](docs/2.%20Requirement%20Analysis/) | Customer Journey Map, DFD, Requirements, Tech Stack |
| [3. Project Design](docs/3.%20Project%20Design%20Phase/) | Problem-Solution Fit, Proposed Solution, Architecture |
| [4. Project Planning](docs/4.%20Project%20Planning%20Phase/) | Sprint Backlog |
| [5. Project Development](docs/5.%20Project%20Development%20Phase/) | Code Quality, Solution Summary, Features |
| [6. Project Testing](docs/6.%20Project%20Testing/) | Performance Testing |
| [7. Project Documentation](docs/7.%20Project%20Documentation/) | Executable Files, Full Documentation |
| [8. Project Demonstration](docs/8.%20Project%20Demonstration/) | Demo Plan, Scalability, Team Roles |

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
