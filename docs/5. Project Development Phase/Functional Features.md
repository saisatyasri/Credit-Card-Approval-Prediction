# Functional Features

**Project:** Credit Card Approval Prediction

---

## Feature List

| # | Feature Name | Description | Location |
|---|---|---|---|
| 1 | **Model Comparison Dashboard** | Home page displays accuracy and ROC-AUC for all 4 trained models (LR, DT, RF, XGBoost) in a comparison table, highlighting Random Forest as the best model | templates/index.html + app.py `/` route |
| 2 | **15-Field Applicant Prediction Form** | Input form captures: income type, income amount, education, family status, housing type, occupation, age, employment years, children count, family members, gender, car/property ownership, and 4 contact flags | templates/predict.html |
| 3 | **Instant Prediction Result** | After form submission, displays Approved (green) or Rejected (red) result card with animated confidence progress bar and probability percentage | templates/predict.html result section |
| 4 | **Prediction History** | Stores and displays the last 10 predictions made in the current browser session, with collapsible detail cards showing all input values | templates/history.html + Flask session |
| 5 | **Scenario Pre-Fill Cards** | Three buttons on the dashboard (Low Risk / Mid Risk / High Risk) that automatically fill the prediction form with representative applicant profiles for demo purposes | templates/index.html + static/js/script.js |
| 6 | **Real-Time Income Formatter** | As the user types annual income, a display label shows the formatted value (e.g., "₹4,80,000 / year") in real time using JavaScript | static/js/script.js `updateIncomeDisplay()` |
| 7 | **Employment Status Auto-Toggle** | When the user selects "Unemployed" as income type, the employment years field automatically resets to 0 and IS_UNEMPLOYED flag is set to 1 | static/js/script.js `updateUnemployed()` |
| 8 | **Responsive Banking UI** | Bootstrap 5 responsive grid ensures the app works on mobile, tablet, and desktop. Navy + gold banking color theme with Font Awesome icons | static/css/style.css (--primary-blue, --accent-gold) |
| 9 | **History Clear** | Button on the History page sends POST to `/clear_history`, resets Flask session, and redirects to empty history — allows starting fresh | templates/history.html + app.py `/clear_history` route |
| 10 | **Graceful Error Handling** | If model PKL files are missing (e.g., first clone without training), `MODELS_LOADED=False` prevents crashes and shows a user-friendly error message | app.py `MODELS_LOADED` flag |
