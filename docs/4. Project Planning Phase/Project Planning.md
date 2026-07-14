# Project Planning

**Project:** Credit Card Approval Prediction

---

## Sprint Backlog

| Sprint | Epic | User Story | Assigned To | Priority | Status |
|---|---|---|---|---|---|
| **Sprint 1** | Data Collection | As a data engineer, I can download the Kaggle credit card dataset so that the team has raw data to work with | sirisha | High | Done |
| **Sprint 1** | EDA | As a data analyst, I can explore application_record.csv and credit_record.csv to understand data distribution and quality | satya | High | Done |
| **Sprint 2** | Target Engineering | As an ML engineer, I can map STATUS codes to binary labels so that the model has a meaningful prediction target | hansraj | High | Done |
| **Sprint 2** | Feature Engineering | As an ML engineer, I can derive AGE_YEARS, YEARS_EMPLOYED, IS_UNEMPLOYED, and INCOME_PER_MEMBER features so that the model has richer inputs | prasanna | High | Done |
| **Sprint 2** | Preprocessing | As an ML engineer, I can apply LabelEncoder and StandardScaler and save them as PKL files so that the web app can preprocess user inputs consistently | sravya | High | Done |
| **Sprint 3** | Model Training | As a data scientist, I can train Logistic Regression, Decision Tree, Random Forest, and XGBoost classifiers so that we can compare model performance objectively | sirisha | High | Done |
| **Sprint 3** | Model Evaluation | As a data scientist, I can compare accuracy and ROC-AUC for all 4 models and select the best one so that the web app uses the most accurate predictor | satya | High | Done |
| **Sprint 4** | Flask Backend | As a backend developer, I can implement 4 Flask routes (/, /predict GET+POST, /history, /clear_history) so that users can interact with the model through a web browser | hansraj | High | Done |
| **Sprint 4** | Frontend Development | As a frontend developer, I can build a responsive Bootstrap 5 UI with a prediction form, result card, and history page so that the app is easy to use on any device | satya | High | Done |
| **Sprint 4** | Scenario Cards | As a frontend developer, I can add pre-fill scenario buttons (Low/Mid/High risk) so that demo users can quickly test different applicant profiles | sravya | Medium | Done |
| **Sprint 5** | Testing | As a QA engineer, I can test all form scenarios and edge cases so that the application delivers correct results across all input combinations | prasanna | High | Done |
| **Sprint 5** | Deployment | As a DevOps engineer, I can configure Render with Procfile and render.yaml so that the application is accessible at a public HTTPS URL | sirisha | High | Done |
| **Sprint 5** | Documentation | As a project lead, I can create all 8-phase documentation files and push them to GitHub so that the project is fully documented for submission | All | High | Done |

---

## Project Timeline

| Phase | Duration | Deliverables |
|---|---|---|
| Sprint 1: Data & EDA | Week 1 | Kaggle dataset, Jupyter EDA notebook |
| Sprint 2: Feature Engineering | Week 2 | Preprocessed dataset, PKL encoders/scalers |
| Sprint 3: Model Training | Week 3 | 4 trained models, model.pkl, metadata.pkl |
| Sprint 4: Web App | Week 4 | Flask app, all templates, static assets |
| Sprint 5: Testing & Deploy | Week 5 | Render deployment, docs, GitHub push |

---

## Team Assignment Summary

| Team Member | Role | Primary Responsibility |
|---|---|---|
| sirisha | Team Lead / ML Engineer | Target engineering, model training, frontend |
| prasanna | Backend Developer | Flask routes, prediction logic |
| satya | Data Engineer | Data collection, preprocessing, deployment |
| sravya | Data Analyst | EDA, testing, validation |
| hansraj | ML Engineer | Feature engineering, model evaluation |
