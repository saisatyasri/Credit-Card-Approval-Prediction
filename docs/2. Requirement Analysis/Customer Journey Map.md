# Customer Journey Map

**Project:** Credit Card Approval Prediction
**Customer:** Credit Analyst / Applicant using the prediction web application

---

| | **Stage 1: Application Submission** | **Stage 2: ML Processing** | **Stage 3: Result Delivery** |
|---|---|---|---|
| **Actions** | User opens the web app, navigates to the Predict page, fills in applicant details (income, age, employment, etc.) and clicks "Predict Approval" | Flask backend receives the form, validates inputs, applies preprocessing (encoding + scaling), and passes features to the trained Random Forest model | Model returns Approved/Rejected label with confidence score; result is displayed on the page and saved to session history |
| **Touchpoint** | Web browser → `/predict` page (HTML form with 15 input fields) | Flask route handler → `preprocess_input()` → `model.predict()` | Prediction result card with confidence bar → `/history` page |
| **Customer Thought** | "I hope this is easy to fill in" / "What if I enter something wrong?" | "How long will this take?" | "I want to understand why it was approved/rejected" |
| **Customer Feeling** | Curious, slightly uncertain about what to enter | Anticipatory, brief wait | Relieved (if approved) or concerned (if rejected); informed either way |
| **Process Ownership** | Frontend (templates/predict.html) + JS validation (static/js/script.js) | app.py → preprocess_input() → model.pkl | templates/predict.html result section + templates/history.html |
| **Opportunities** | Add tooltips explaining each field; add field-level validation hints | Show a loading spinner during inference | Add explanation of which factors influenced the decision (feature importance) |
