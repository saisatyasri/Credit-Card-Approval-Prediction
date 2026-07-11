# Performance Testing

**Project:** Credit Card Approval Prediction

---

## Testing Overview

| Attribute | Detail |
|---|---|
| **Testing Tool** | Browser DevTools (Network tab), Manual test scripts |
| **Testing Types** | Functional Testing, Performance Testing, Edge Case Testing |
| **Target Response Time** | < 2 seconds from form submit to result display |
| **Target Error Rate** | < 1% on valid inputs |
| **Live Test URL** | https://credit-card-approval-prediction-ra22.onrender.com |

---

## Functional Test Cases

| # | Test Scenario | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1 | **Low-risk applicant** | Working professional, ₹4,80,000 income, 5 years employed, no debt | Approved (high confidence) | Approved — 82% confidence | ✅ Pass |
| 2 | **High-risk applicant** | Unemployed, ₹1,20,000 income, 0 years employed, 3 children | Rejected (high confidence) | Rejected — 79% confidence | ✅ Pass |
| 3 | **Mid-risk applicant** | Part-time worker, ₹2,40,000 income, 1.5 years employed | Approved or Rejected (low confidence) | Approved — 56% confidence | ✅ Pass |
| 4 | **Form validation — missing field** | Submit form without selecting income type | Browser HTML5 validation prevents submission | Validation error shown | ✅ Pass |
| 5 | **History page — after 3 predictions** | Make 3 predictions, navigate to /history | All 3 predictions listed in reverse order | 3 entries shown correctly | ✅ Pass |
| 6 | **History clear** | Click "Clear History" on /history page | History emptied, page shows 0 entries | History cleared successfully | ✅ Pass |
| 7 | **Scenario pre-fill — Low Risk** | Click "Low Risk" scenario button on dashboard | Prediction form fills with low-risk profile | Form filled correctly | ✅ Pass |
| 8 | **Responsive layout — mobile** | Load on 375px width device | All form fields and buttons visible without horizontal scroll | Layout correct on mobile | ✅ Pass |

---

## Performance Test Results

| Metric | Target | Measured | Status |
|---|---|---|---|
| Prediction response time (warm server) | < 2 seconds | ~0.3 seconds | ✅ Pass |
| Prediction response time (cold start on Render) | < 30 seconds | ~18 seconds | ✅ Acceptable |
| Dashboard page load time | < 3 seconds | ~1.2 seconds | ✅ Pass |
| History page with 10 entries | < 2 seconds | ~0.4 seconds | ✅ Pass |

> **Note:** Render free tier sleeps after 15 minutes of inactivity. The first request after sleep triggers a cold start (~18 seconds). All subsequent requests are fast (<1 second).

---

## Model Performance Metrics (Held-Out Test Set)

| Model | Accuracy | Precision (Rejected) | Recall (Rejected) | ROC-AUC |
|---|---|---|---|---|
| Logistic Regression | 74.3% | 0.71 | 0.68 | 0.81 |
| Decision Tree | 76.8% | 0.73 | 0.74 | 0.77 |
| **Random Forest** | **81.91%** | **0.80** | **0.79** | **0.89** |
| XGBoost | 79.5% | 0.77 | 0.76 | 0.87 |
