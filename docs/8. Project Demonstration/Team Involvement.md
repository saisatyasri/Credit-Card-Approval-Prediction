# Team Involvement

**Project:** Credit Card Approval Prediction

---

## Team Members & Contributions

| # | Name | Role | Primary Contributions | Contribution % |
|---|---|---|---|---|
| 1 | **Sirisha Medisetti** | Team Lead / ML Engineer | Project coordination, target variable engineering, model training, Flask frontend (templates, CSS, JS), Render deployment, GitHub repository management | 30% |
| 2 | **Sai Satya Sri  Mutyala** | Backend Developer | Flask route implementation, `preprocess_input()` function, prediction history logic, form-to-model integration, session management | 20% |
| 3 | **Rekha Prasanna Nagabathula** | Data Engineer / DevOps | Kaggle dataset acquisition, data cleaning, preprocessing pipeline (StandardScaler, LabelEncoder), Render deployment configuration (Procfile, render.yaml) | 20% |
| 4 | **Hans Raj Mortha** | Data Analyst / QA | Exploratory Data Analysis (EDA notebook — 11 sections), feature distribution visualizations, functional testing (8 test cases), documentation review | 15% |
| 5 | **Sravya Sri Nakkalapudi** | ML Engineer | Feature engineering (AGE_YEARS, YEARS_EMPLOYED, IS_UNEMPLOYED, INCOME_PER_MEMBER), XGBoost training with scale_pos_weight, model comparison evaluation, metadata.pkl generation | 15% |

---

## Story Assignment by Team Member

| Team Member | Stories Assigned |
|---|---|
| Sirisha Medisetti | S1, S3, S7, S11, S14, S15, S17, S18, S20 |
| Sai Satya Sri  Mutyala | S4, S8, S9, S10, S19 |
| Rekha Prasanna Nagabathula | S2, S5, S12, S16 |
| Hans Raj Mortha | S6, S13 |
| Sravya Sri Nakkalapudi| S7 (shared), S8 (shared), S11 (shared) |

> Story IDs correspond to the sprint backlog in `docs/4. Project Planning Phase/Project Planning.md`

---

## Team Reflection

The project was completed in 5 sprints over 5 weeks. The most challenging aspect was handling the extreme class imbalance in the original dataset (initially 98.5% Approved / 1.5% Rejected). The team solved this by:
1. Expanding the definition of "bad" status to include STATUS=1 (30-59 days past due)
2. Excluding applicants with only X-status (no evaluated credit history)
3. Applying `class_weight='balanced'` to all Scikit-learn models
4. Applying `scale_pos_weight = neg/pos ratio` to XGBoost

This brought the class balance to 87%/13% and Random Forest accuracy from ~65% to 81.91%.
