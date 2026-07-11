# Proposed Solution

**Project:** Credit Card Approval Prediction

---

## Executive Summary

We developed an end-to-end machine learning pipeline that ingests real-world credit application data from Kaggle, trains four classification models, and serves predictions through a Flask web application deployed on Render. The system enables any credit analyst to enter applicant details and receive an instant, objective Approved/Rejected decision with a confidence percentage — eliminating the subjectivity and latency of manual review.

---

## Project Overview

| Attribute | Detail |
|---|---|
| **Project Name** | Credit Card Approval Prediction |
| **Objective** | Predict credit card approval outcome using ML on historical applicant and credit behavior data |
| **Scope** | Data ingestion → Target engineering → Feature engineering → Model training → Web app → Render deployment |
| **Dataset** | Kaggle: `rikdifos/credit-card-approval-prediction` (application_record.csv: 438,557 rows; credit_record.csv: 1,048,575 rows) |
| **Live URL** | https://credit-card-approval-prediction-ra22.onrender.com |
| **GitHub Repository** | https://github.com/karthik-ganti/Credit-Card-Approval-Prediction |

---

## Problem Statement

| Attribute | Detail |
|---|---|
| **Problem** | Manual credit card approval processes are slow, costly, and inconsistent. Banks process thousands of applications daily but rely on rules-based or purely judgment-driven methods. |
| **Impact** | High operational cost, approval delays for applicants, increased risk of bad loans due to manual error, and inability to scale operations without proportional hiring. |
| **Beneficiaries** | Credit analysts (faster workflow), applicants (faster decision), bank management (reduced risk, lower cost) |

---

## Proposed Solution Approach

| Component | Detail |
|---|---|
| **Approach** | Supervised binary classification — trained on historical approval decisions labeled from real-world credit behavior (STATUS codes). |
| **Target Variable** | STATUS 1-5 (30+ days past due) → Rejected (0); STATUS 0/C/X → Approved (1). Applicants with only X-status (no credit history evaluated) are excluded. |
| **Models Trained** | Logistic Regression, Decision Tree, Random Forest (selected as best), XGBoost |
| **Best Model** | Random Forest — 81.91% accuracy, 0.89 ROC-AUC, with class_weight='balanced' to handle 87%/13% class imbalance |
| **Key Features** | AGE_YEARS, YEARS_EMPLOYED, IS_UNEMPLOYED (sentinel flag), INCOME_PER_MEMBER, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, OCCUPATION_TYPE, AMT_INCOME_TOTAL, CNT_CHILDREN, CNT_FAM_MEMBERS, FLAG_OWN_CAR, FLAG_OWN_REALTY, contact flags |

---

## Resource Requirements

| Resource | Specification |
|---|---|
| **Language** | Python 3.12 |
| **ML Libraries** | Scikit-learn 1.8.0, XGBoost 3.2.0, Joblib 1.5.3 |
| **Web Framework** | Flask 3.1.2, Gunicorn 21.2.0 |
| **Data Processing** | Pandas 2.3.3, NumPy 2.3.4 |
| **Visualization** | Matplotlib 3.10.9, Seaborn 0.13.2 |
| **Deployment** | Render (free tier), GitHub (version control) |
| **Dataset** | Kaggle API (rikdifos/credit-card-approval-prediction) |
