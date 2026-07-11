# Problem-Solution Fit

**Project:** Credit Card Approval Prediction

---

## Problem-Solution Fit Canvas

| # | Category | Description |
|---|---|---|
| 1 | **Customer Segment (CS)** | Commercial banks, NBFCs, credit card issuers, and credit analysts who process thousands of applications monthly |
| 2 | **Problem (PR)** | Manual credit card approval is slow, inconsistent, prone to human bias, and fails to leverage the patterns hidden in historical credit data |
| 3 | **Target Result (TR)** | An ML-powered prediction tool that instantly classifies an applicant as Approved or Rejected based on 15 objective features |
| 4 | **Expected Measurement (EM)** | Prediction delivered within 2 seconds with a confidence score %; Random Forest achieves 81.91% test accuracy and 0.89 ROC-AUC |
| 5 | **Adopted Solution (AS)** | Flask web application serving a trained Random Forest classifier, with preprocessing pipeline (LabelEncoder + StandardScaler) saved as PKL artifacts |
| 6 | **Collected Lessons (CL)** | Training on Kaggle's real-world dataset (438K+ applicants, 1M+ monthly records) validated that employment status, income, and credit history are the strongest predictors |
| 7 | **Business Enabler (BE)** | Reduces manual review time by ~90%; enables credit analysts to handle higher application volumes without proportional headcount increase |
| 8 | **Channel (CH)** | Deployed at `https://credit-card-approval-prediction-ra22.onrender.com` via Render; auto-deploys on every GitHub push to `master` |
| 9 | **Revenue / Cost (RC)** | Zero infrastructure cost using Render free tier + GitHub + open-source Python stack |
| 10 | **Scalability Level (SL)** | Stateless Flask app scales horizontally; model can be retrained with updated data and redeployed without UI changes |
