# Data Flow Diagram

**Project:** Credit Card Approval Prediction

---

## Level 0 — Context Diagram

```
                    Applicant Details
                    (15 input fields)
        ┌──────┐         │
        │      │─────────▼─────────────────────────────────┐
        │ User │    Credit Card Approval Prediction System  │
        │      │◄──────────────────────────────────────────┘
        └──────┘    Approval Result + Confidence Score
```

**External Entity:** User (Credit Analyst / Applicant)
**Process:** Credit Card Approval Prediction System
**Output:** Approved / Rejected with Confidence %

---

## Level 1 — Detailed DFD

```
                        ┌──────────────┐
                        │     USER     │  (External Entity)
                        └──────┬───────┘
                               │ Applicant Details Form
                               ▼
                    ┌──────────────────────┐
              ┌────►│  1. Form Validation  │
              │     │  (templates/         │
              │     │   predict.html +     │
              │     │   script.js)         │
              │     └──────────┬───────────┘
         Error│               │ Validated Inputs
         Msg  │               ▼
              │     ┌──────────────────────┐
              └─────│  2. Preprocessing    │◄──── [DS1] encoder.pkl
                    │  (app.py →           │◄──── [DS2] scaler.pkl
                    │  preprocess_input()) │
                    └──────────┬───────────┘
                               │ Scaled Feature Vector
                               ▼
                    ┌──────────────────────┐
                    │  3. ML Inference     │◄──── [DS3] model.pkl
                    │  (Random Forest      │◄──── [DS4] metadata.pkl
                    │   model.predict())   │
                    └──────────┬───────────┘
                               │ Prediction + Confidence
                               ▼
                    ┌──────────────────────┐
                    │  4. Result Display   │────► [DS5] Session History
                    │  (templates/         │
                    │   predict.html +     │
                    │   history.html)      │
                    └──────────┬───────────┘
                               │ Approved/Rejected Card
                               ▼
                        ┌──────────────┐
                        │     USER     │
                        └──────────────┘
```

### Data Stores

| ID | Name | Contents |
|---|---|---|
| DS1 | encoder.pkl | LabelEncoders for 5 categorical features |
| DS2 | scaler.pkl | StandardScaler fitted on 14 numeric features |
| DS3 | model.pkl | Trained Random Forest classifier |
| DS4 | metadata.pkl | Model comparison metrics + feature column order |
| DS5 | Session Storage | Last 10 prediction results (browser session only) |

### Symbol Legend

| Symbol | Meaning |
|---|---|
| Rectangle (USER) | External Entity |
| Rounded Rectangle | Process |
| [DS#] | Data Store |
| Arrow | Data Flow |
