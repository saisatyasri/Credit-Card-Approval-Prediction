import os
import joblib
import numpy as np
from datetime import datetime
from flask import Flask, render_template, request, session

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')

app = Flask(__name__)
app.secret_key = 'creditai_secret_2024'

# ---------------------------------------------------------------------------
# Load trained artifacts at startup
# ---------------------------------------------------------------------------
try:
    model    = joblib.load(os.path.join(MODEL_DIR, 'model.pkl'))
    scaler   = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
    encoders = joblib.load(os.path.join(MODEL_DIR, 'encoder.pkl'))
    metadata = joblib.load(os.path.join(MODEL_DIR, 'metadata.pkl'))
    MODELS_LOADED = True
except FileNotFoundError:
    MODELS_LOADED = False
    model = scaler = encoders = metadata = None

# ---------------------------------------------------------------------------
# Feature column order — must match train_model.py exactly
# ---------------------------------------------------------------------------
CATEGORICAL_COLS = [
    'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE',
    'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'OCCUPATION_TYPE'
]
NUMERIC_COLS = [
    'CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'AGE_YEARS', 'YEARS_EMPLOYED',
    'IS_UNEMPLOYED', 'FLAG_MOBIL', 'FLAG_WORK_PHONE', 'FLAG_PHONE',
    'FLAG_EMAIL', 'CNT_FAM_MEMBERS', 'INCOME_PER_MEMBER',
    'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY'
]

# ---------------------------------------------------------------------------
# Dropdown choices (must match LabelEncoder classes from training)
# ---------------------------------------------------------------------------
INCOME_TYPES = [
    'Commercial associate', 'Pensioner', 'State servant', 'Student', 'Working'
]
EDU_TYPES = [
    'Academic degree', 'Higher education', 'Incomplete higher',
    'Lower secondary', 'Secondary / secondary special'
]
FAMILY_STATUSES = [
    'Civil marriage', 'Married', 'Separated', 'Single / not married', 'Widow'
]
HOUSING_TYPES = [
    'Co-op apartment', 'House / apartment', 'Municipal apartment',
    'Office apartment', 'Rented apartment', 'With parents'
]
OCCUPATIONS = [
    'Accountants', 'Cleaning staff', 'Cooking staff', 'Core staff', 'Drivers',
    'HR staff', 'High skill tech staff', 'IT staff', 'Laborers',
    'Low-skill Laborers', 'Managers', 'Medicine staff', 'Private service staff',
    'Realty agents', 'Sales staff', 'Secretaries', 'Security staff',
    'Waiters/barmen staff', 'Unknown'
]

FORM_CHOICES = dict(
    income_types=INCOME_TYPES,
    edu_types=EDU_TYPES,
    family_statuses=FAMILY_STATUSES,
    housing_types=HOUSING_TYPES,
    occupations=OCCUPATIONS,
)


# ---------------------------------------------------------------------------
# Preprocessing helper
# ---------------------------------------------------------------------------
def preprocess_input(form):
    """Convert raw form data into a scaled feature vector for prediction."""
    gender       = 1 if form.get('gender') == 'F' else 0
    own_car      = 1 if form.get('own_car')    == 'Y' else 0
    own_realty   = 1 if form.get('own_realty') == 'Y' else 0
    children     = int(form.get('children', 0))
    income       = float(form.get('income', 0))
    age          = int(form.get('age', 30))
    emp_years    = float(form.get('employed_years', 0))
    is_unemployed = 1 if emp_years == 0 else 0
    flag_mobil   = int(form.get('flag_mobil',      1))
    flag_wphone  = int(form.get('flag_work_phone', 0))
    flag_phone   = int(form.get('flag_phone',      0))
    flag_email   = int(form.get('flag_email',      0))
    fam_members  = int(form.get('fam_members', 1))
    income_per_m = income / max(fam_members, 1)

    # Encode categorical features
    cat_encoded = [
        encoders['NAME_INCOME_TYPE'].transform([form.get('income_type', INCOME_TYPES[0])])[0],
        encoders['NAME_EDUCATION_TYPE'].transform([form.get('edu_type', EDU_TYPES[0])])[0],
        encoders['NAME_FAMILY_STATUS'].transform([form.get('family_status', FAMILY_STATUSES[0])])[0],
        encoders['NAME_HOUSING_TYPE'].transform([form.get('housing_type', HOUSING_TYPES[0])])[0],
        encoders['OCCUPATION_TYPE'].transform([form.get('occupation', 'Unknown')])[0],
    ]

    num_raw = [
        children, income, age, emp_years, is_unemployed,
        flag_mobil, flag_wphone, flag_phone, flag_email,
        fam_members, income_per_m, gender, own_car, own_realty
    ]
    num_scaled = scaler.transform([num_raw])[0].tolist()

    return cat_encoded + num_scaled


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route('/')
def index():
    comparison = metadata['comparison'] if MODELS_LOADED else {}
    best_model = metadata['best_model'] if MODELS_LOADED else 'N/A'
    return render_template('index.html',
                           comparison=comparison,
                           best_model=best_model,
                           models_loaded=MODELS_LOADED)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    result = None
    error  = None

    if request.method == 'POST':
        if not MODELS_LOADED:
            error = "Models not loaded. Please run train_model.py first."
        else:
            try:
                features   = preprocess_input(request.form)
                prediction = int(model.predict([features])[0])
                confidence = float(model.predict_proba([features])[0][prediction]) * 100

                label = 'Approved' if prediction == 1 else 'Rejected'
                color = 'success'  if prediction == 1 else 'danger'
                icon  = 'check-circle-fill' if prediction == 1 else 'x-circle-fill'

                result = {
                    'prediction': label,
                    'confidence': round(confidence, 1),
                    'color':      color,
                    'icon':       icon,
                    'timestamp':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'inputs': {
                        'Gender':          'Female' if request.form.get('gender') == 'F' else 'Male',
                        'Age':             request.form.get('age'),
                        'Income':          f"₹{float(request.form.get('income',0)):,.0f}",
                        'Income Type':     request.form.get('income_type'),
                        'Employment':      f"{request.form.get('employed_years',0)} years",
                        'Education':       request.form.get('edu_type'),
                        'Family Status':   request.form.get('family_status'),
                        'Housing':         request.form.get('housing_type'),
                        'Children':        request.form.get('children'),
                        'Family Members':  request.form.get('fam_members'),
                    }
                }

                # Store in session history (cap at 10)
                history = session.get('history', [])
                history.insert(0, result)
                session['history'] = history[:10]
                session.modified = True

            except Exception as exc:
                error = f"Prediction error: {str(exc)}"

    return render_template('predict.html',
                           result=result,
                           error=error,
                           models_loaded=MODELS_LOADED,
                           **FORM_CHOICES)


@app.route('/history')
def history():
    predictions = session.get('history', [])
    return render_template('history.html', history=predictions)


@app.route('/clear_history')
def clear_history():
    session.pop('history', None)
    return history()


# ---------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
