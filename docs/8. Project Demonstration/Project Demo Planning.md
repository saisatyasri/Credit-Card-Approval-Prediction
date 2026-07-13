# Project Demo Planning

**Project:** Credit Card Approval Prediction

---

## Demo Agenda

| # | Segment | Presenter | Duration | Content |
|---|---|---|---|---|
| 1 | **Introduction** | sirisha | 2 min | Project goal, problem statement, team introduction |
| 2 | **Problem & Dataset** | satya sri | 3 min | Credit approval challenges, Kaggle dataset overview, EDA insights |
| 3 | **ML Pipeline** | prasanna+sravya | 5 min | Feature engineering, model training, class imbalance handling, Random Forest selection |
| 4 | **Live Application Demo** | hans raj | 4 min | Full walkthrough: Dashboard → Scenario Cards → Predict Form → Result → History |
| 5 | **Architecture & Deployment** | sirisha | 2 min | 3-layer architecture, GitHub → Render CI/CD, live URL |
| 6 | **Future Plans** | Vivek | 1 min | Hyperparameter tuning, IBM Watson ML, user authentication |
| 7 | **Q&A** | All | 3 min | Panel responds to questions |
| | **Total** | | **20 min** | |

---

## Pre-Demo Checklist

| Item | Responsible | Status |
|---|---|---|
| Confirm live URL is active (warm up Render) | Joy | Visit URL 5 min before demo starts |
| Prepare low/mid/high risk test scenarios | Karthik | Scenario cards are built into the UI |
| Test prediction form end-to-end | Nandini | Run 3 test predictions, verify result display |
| Prepare backup screenshots (if internet fails) | Uma | Screenshot of dashboard, predict form, result, history |
| Share GitHub link in presentation | Karthik | https://github.com/karthik-ganti/Credit-Card-Approval-Prediction |
| Ensure laptop display resolution is legible | Joy | 1280×720 minimum resolution |

---

## Demo Flow — Live Application

```
1. Open: https://credit-card-approval-prediction-ra22.onrender.com
   → Show dashboard: model comparison table + hero section

2. Click "Low Risk" scenario card
   → Form fills automatically

3. Click "Predict Approval"
   → Result: Approved (green card, ~80%+ confidence)
   → Explain the confidence score and animated bar

4. Go back → Click "High Risk" scenario
   → Submit prediction
   → Result: Rejected (red card, ~75%+ confidence)

5. Navigate to History (/history)
   → Show 2 predictions logged
   → Expand one card to show all input details

6. Click "Clear History"
   → History resets to 0 entries
```

---

## Contingency Plan

| Risk | Mitigation |
|---|---|
| Render cold start takes too long | Open live URL 10 minutes before demo to warm up the server |
| Internet connectivity issue | Use screenshots + run `python app.py` locally as fallback |
| Form submission error | Reload page and retry; fallback to showing training notebook |
