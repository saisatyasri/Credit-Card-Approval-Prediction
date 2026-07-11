# Technology Stack

**Project:** Credit Card Approval Prediction

---

## Technology Stack Table

| Layer | Technology Chosen | Version | Justification |
|---|---|---|---|
| **Frontend** | HTML5, Bootstrap 5, JavaScript | Bootstrap 5.3.2 | Responsive, mobile-first design with no heavy frontend framework overhead. Bootstrap provides a professional banking UI out of the box. |
| **Backend** | Python, Flask | Python 3.12, Flask 3.1.2 | Flask is a lightweight, flexible web framework ideal for ML model serving. Python is the standard language for ML pipelines. |
| **ML Engine** | Scikit-learn, XGBoost, Joblib | sklearn 1.8.0, XGBoost 3.2.0 | Industry-standard ML libraries. Scikit-learn provides LR, DT, RF classifiers; XGBoost adds gradient boosting. Joblib handles fast model serialization. |
| **Data Processing** | Pandas, NumPy, Seaborn, Matplotlib | Pandas 2.3.3, NumPy 2.3.4 | Pandas handles large CSV ingestion and preprocessing. NumPy for numerical operations. Seaborn/Matplotlib for EDA visualizations. |
| **Cloud / Hosting** | Render | Free tier | Zero-cost Flask deployment with automatic GitHub integration. Supports Python runtime with Gunicorn WSGI server. Singapore region for low latency. |
| **Version Control** | Git + GitHub | — | Team collaboration, commit history, and CI/CD pipeline. Auto-deploy to Render on every push to master branch. |
| **Dataset Source** | Kaggle | rikdifos/credit-card-approval-prediction | Publicly available, CC0 licensed dataset with 438K+ real applicant records and 1M+ monthly credit records. |
| **Development Tools** | Jupyter Notebook, VS Code | — | Jupyter for EDA and model experimentation. VS Code for application development. |
