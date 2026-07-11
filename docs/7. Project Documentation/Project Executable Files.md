# Project Executable Files

**Project:** Credit Card Approval Prediction

---

## Submission Checklist

| # | Deliverable | Status | Location |
|---|---|---|---|
| 1 | Source code — ML training pipeline | ✅ | `train_model.py` |
| 2 | Source code — Flask web application | ✅ | `app.py` |
| 3 | HTML templates | ✅ | `templates/` (base, index, predict, history) |
| 4 | CSS theme | ✅ | `static/css/style.css` |
| 5 | JavaScript functionality | ✅ | `static/js/script.js` |
| 6 | Trained model artifact | ✅ | `models/model.pkl` (Random Forest) |
| 7 | Preprocessing artifacts | ✅ | `models/scaler.pkl`, `models/encoder.pkl` |
| 8 | Model comparison metadata | ✅ | `models/metadata.pkl` |
| 9 | EDA + experimentation notebook | ✅ | `notebooks/Credit_Card_Approval_Analysis.ipynb` |
| 10 | Python dependencies | ✅ | `requirements.txt` |
| 11 | Render deployment config | ✅ | `Procfile`, `render.yaml` |
| 12 | Project documentation (8 phases) | ✅ | `docs/` folder |
| 13 | Project README | ✅ | `README.md` |

---

## Project Folder Structure

```
Credit Card Approval Prediction/
├── app.py
├── train_model.py
├── requirements.txt
├── Procfile
├── render.yaml
├── .gitignore
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   └── history.html
│
├── static/
│   ├── css/style.css
│   └── js/script.js
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── encoder.pkl
│   └── metadata.pkl
│
├── notebooks/
│   └── Credit_Card_Approval_Analysis.ipynb
│
└── docs/
    ├── 1. Brainstorming & Ideation/
    ├── 2. Requirement Analysis/
    ├── 3. Project Design Phase/
    ├── 4. Project Planning Phase/
    ├── 5. Project Development Phase/
    ├── 6. Project Testing/
    ├── 7. Project Documentation/
    └── 8. Project Demonstration/
```

---

## Deployment Details

| Attribute | Detail |
|---|---|
| **Live URL** | https://credit-card-approval-prediction-ra22.onrender.com |
| **GitHub Repository** | https://github.com/karthik-ganti/Credit-Card-Approval-Prediction |
| **Hosting Platform** | Render (free tier) |
| **WSGI Server** | Gunicorn 21.2.0 |
| **Start Command** | `gunicorn app:app` |
| **Auto-Deploy Trigger** | Push to `master` branch on GitHub |

---

## How to Run Locally

```bash
# Step 1: Clone the repository
git clone https://github.com/karthik-ganti/Credit-Card-Approval-Prediction.git
cd Credit-Card-Approval-Prediction

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Place dataset files in data/ directory
#   data/application_record.csv
#   data/credit_record.csv
# (Download from: https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction)

# Step 4: Train the model (generates models/*.pkl)
python train_model.py

# Step 5: Start the Flask application
python app.py
# Open: http://127.0.0.1:5000
```
