# Scalability and Future Plan

**Project:** Credit Card Approval Prediction

---

## Current Scalability

The application is designed to be stateless and horizontally scalable:

| Attribute | Current Design |
|---|---|
| **State storage** | Browser session only — no server-side database required |
| **Model serving** | PKL files loaded into memory at startup — instant inference |
| **Web server** | Gunicorn WSGI — supports multiple worker processes |
| **Deployment** | Render auto-scales web workers on traffic spikes |
| **CI/CD** | GitHub push triggers Render auto-redeploy — zero-downtime updates |

---

## Future Enhancements

### Phase 2: Model Improvements
| Enhancement | Description | Priority |
|---|---|---|
| Hyperparameter tuning | GridSearchCV/RandomizedSearch for Random Forest (n_estimators, max_depth, min_samples_split) | High |
| Ensemble stacking | Stack LR + RF + XGBoost predictions for higher accuracy | Medium |
| SHAP explanations | Add SHAP feature importance to explain why each applicant was approved/rejected | High |
| Periodic retraining | Automate model retraining on updated credit data quarterly | Medium |

### Phase 3: Infrastructure Upgrades
| Enhancement | Description | Priority |
|---|---|---|
| Database integration | Replace session storage with PostgreSQL to persist prediction history across sessions | High |
| User authentication | Add login system so analysts can maintain individual prediction histories | Medium |
| IBM Watson ML | Migrate model serving from PKL files to IBM Watson ML API for enterprise-grade SLA | Low |
| Docker containerization | Package app in Docker for platform-independent deployment | Medium |

### Phase 4: Feature Additions
| Enhancement | Description | Priority |
|---|---|---|
| Batch prediction | Upload CSV of multiple applicants and get bulk predictions | High |
| Credit bureau API | Integrate with CIBIL/Experian API to fetch real credit scores automatically | Low |
| Audit logging | Log all predictions with timestamp and analyst ID for compliance | Medium |
| PDF report generation | Generate downloadable PDF report for each prediction | Low |

---

## Scalability Roadmap

```
Current (MVP)          Phase 2               Phase 3               Phase 4
─────────────────    ──────────────────    ──────────────────    ──────────────────
Single Flask app  ─► SHAP explanations ─► PostgreSQL DB     ─► Batch predictions
Render free tier     Hyperparameter        User auth             Credit bureau API
Session storage      tuning                Docker                Audit logging
4 ML models          Ensemble stacking     IBM Watson ML         PDF reports
```
