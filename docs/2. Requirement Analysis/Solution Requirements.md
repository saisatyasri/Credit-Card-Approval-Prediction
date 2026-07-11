# Solution Requirements

**Project:** Credit Card Approval Prediction

---

## Functional Requirements (FR)

| S.No | Category | Requirement | Description |
|---|---|---|---|
| FR-1 | Authentication | No login required | The application is publicly accessible; no user account is needed to make predictions |
| FR-2 | Input Interface | Applicant detail form | System must accept 15 applicant inputs: gender, age, income, income type, employment years, occupation, education, family status, housing type, children count, family members, car ownership, property ownership, and contact flags |
| FR-3 | External Interfaces | Kaggle dataset ingestion | Training pipeline must read application_record.csv and credit_record.csv from the data/ directory |
| FR-4 | Transactions | End-to-end prediction pipeline | System must preprocess inputs (encode + scale), run ML inference, and return result within 2 seconds |
| FR-5 | Reporting | Model comparison dashboard | Home page must display accuracy and ROC-AUC for all 4 trained models, highlighting the best model |
| FR-6 | Reporting | Prediction history | System must store and display the last 10 predictions made in the current browser session |
| FR-7 | Business Rules | Target variable logic | STATUS codes 1-5 (30+ days past due) → Rejected (0); codes 0, C, X → Approved (1) |
| FR-8 | Compliance | No PII storage | No personally identifiable information is stored; all prediction history is session-only and cleared on browser close |

---

## Non-Functional Requirements (NFR)

| S.No | Category | Requirement | Target Metric |
|---|---|---|---|
| NFR-1 | Performance | Prediction response time | < 2 seconds from form submission to result display |
| NFR-2 | Scalability | Concurrent users | Render auto-scales; application is stateless (session storage only) |
| NFR-3 | Security | Data protection | No sensitive data stored on server; HTTPS enforced by Render |
| NFR-4 | Reliability | Uptime | 99% uptime on Render free tier; sleeps after 15 min inactivity |
| NFR-5 | Usability | Responsive design | Mobile + desktop compatible via Bootstrap 5.3 responsive grid |
| NFR-6 | Maintainability | Auto-deployment | Any push to GitHub master branch triggers automatic Render redeployment |
