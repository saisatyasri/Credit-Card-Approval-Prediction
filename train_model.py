import os
import warnings
import pandas as pd
import numpy as np
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, roc_auc_score, classification_report, confusion_matrix
)
from xgboost import XGBClassifier

warnings.filterwarnings('ignore')

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATA_DIR  = os.path.join(BASE_DIR, 'data')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
os.makedirs(MODEL_DIR, exist_ok=True)

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

FEATURE_COLS = CATEGORICAL_COLS + NUMERIC_COLS


def load_data():
    app_path    = os.path.join(DATA_DIR, 'application_record.csv')
    credit_path = os.path.join(DATA_DIR, 'credit_record.csv')

    if not os.path.exists(app_path) or not os.path.exists(credit_path):
        raise FileNotFoundError(
            "Dataset files not found in data/ folder.\n"
            "Download from Kaggle:\n"
            "  kaggle datasets download -d rikdifos/credit-card-approval-prediction -p data/ --unzip\n"
            "Or manually place application_record.csv and credit_record.csv in the data/ folder."
        )

    app_df    = pd.read_csv(app_path)
    credit_df = pd.read_csv(credit_path)
    print(f"Application records : {app_df.shape[0]:,} rows, {app_df.shape[1]} columns")
    print(f"Credit records      : {credit_df.shape[0]:,} rows, {credit_df.shape[1]} columns")
    return app_df, credit_df


def build_target(credit_df):
    """
    Engineer binary target from monthly payment STATUS history.

    Bad applicant (TARGET=0): ever had STATUS '1'-'5' (30+ days past due).
    Good applicant (TARGET=1): only 'C' (paid off) or '0' (≤29 days) — clean history.
    Applicants with only 'X' (no loan ever) are excluded — no credit history to judge.

    Using '1'-'5' as bad gives a realistic class balance and matches real bank criteria
    (most banks reject applicants with any 30+ day late payment in their credit history).
    """
    bad_statuses  = {'1', '2', '3', '4', '5'}
    good_statuses = {'C', '0'}

    def applicant_label(statuses):
        statuses_str = set(str(s) for s in statuses)
        if statuses_str.issubset({'X'}):
            return -1  # No loan history — exclude
        if any(s in bad_statuses for s in statuses_str):
            return 0   # Rejected
        return 1       # Approved

    target = (
        credit_df.groupby('ID')['STATUS']
        .apply(applicant_label)
        .reset_index()
        .rename(columns={'STATUS': 'TARGET'})
    )
    # Drop applicants with no loan history
    target = target[target['TARGET'] != -1].copy()

    print(f"\nTarget distribution:\n{target['TARGET'].value_counts().to_string()}")
    print(f"  Approval rate : {target['TARGET'].mean()*100:.1f}%")
    print(f"  Rejection rate: {(1-target['TARGET'].mean())*100:.1f}%")
    return target


def engineer_features(app_df):
    df = app_df.copy()

    # Convert negative day counts to positive years
    df['AGE_YEARS'] = (-df['DAYS_BIRTH'] / 365).astype(int)

    # 365243 is the sentinel value for unemployed in this dataset
    df['IS_UNEMPLOYED']  = (df['DAYS_EMPLOYED'] == 365243).astype(int)
    df['YEARS_EMPLOYED'] = df['DAYS_EMPLOYED'].apply(
        lambda x: 0.0 if x == 365243 else round(-x / 365, 2)
    )

    df['INCOME_PER_MEMBER'] = df['AMT_INCOME_TOTAL'] / (df['CNT_FAM_MEMBERS'].clip(lower=1))

    # Binary encode gender and ownership flags
    df['CODE_GENDER']    = (df['CODE_GENDER']    == 'F').astype(int)
    df['FLAG_OWN_CAR']   = (df['FLAG_OWN_CAR']   == 'Y').astype(int)
    df['FLAG_OWN_REALTY']= (df['FLAG_OWN_REALTY'] == 'Y').astype(int)

    df.drop(columns=['DAYS_BIRTH', 'DAYS_EMPLOYED'], inplace=True)
    return df


def preprocess(df):
    # Fill missing OCCUPATION_TYPE with 'Unknown'
    df['OCCUPATION_TYPE'] = df['OCCUPATION_TYPE'].fillna('Unknown')

    encoders = {}
    for col in CATEGORICAL_COLS:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le

    scaler = StandardScaler()
    df[NUMERIC_COLS] = scaler.fit_transform(df[NUMERIC_COLS])

    return df, scaler, encoders


def train_all_models(X_train, X_test, y_train, y_test):
    # Scale positive weight for XGBoost to handle class imbalance
    neg = (y_train == 0).sum()
    pos = (y_train == 1).sum()
    spw = round(neg / pos, 2)   # scale_pos_weight = minority/majority (inverted for XGB)
    spw_xgb = round(pos / neg, 2)  # XGB: weight of positive class relative to negative

    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42,
                                                   class_weight='balanced'),
        'Decision Tree':       DecisionTreeClassifier(max_depth=8, random_state=42,
                                                      class_weight='balanced'),
        'Random Forest':       RandomForestClassifier(n_estimators=100, max_depth=10,
                                                      random_state=42, n_jobs=-1,
                                                      class_weight='balanced'),
        'XGBoost':             XGBClassifier(n_estimators=100, max_depth=6,
                                             learning_rate=0.1, eval_metric='logloss',
                                             scale_pos_weight=spw,
                                             random_state=42, n_jobs=-1, verbosity=0),
    }

    results = {}
    print("\n--- Model Training ---")
    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        acc     = accuracy_score(y_test, y_pred)
        auc     = roc_auc_score(y_test, y_prob)
        results[name] = {
            'model':    model,
            'accuracy': acc,
            'roc_auc':  auc,
            'report':   classification_report(y_test, y_pred),
            'cm':       confusion_matrix(y_test, y_pred),
        }
        print(f"  Accuracy : {acc*100:.2f}%")
        print(f"  ROC-AUC  : {auc:.4f}")
        print(results[name]['report'])

    return results


def save_plots(results, X_test, y_test):
    """Save model comparison plots to models/ folder."""
    from sklearn.metrics import roc_curve

    names    = list(results.keys())
    acc_vals = [results[n]['accuracy'] for n in names]
    auc_vals = [results[n]['roc_auc']  for n in names]

    # Accuracy & AUC comparison bar chart
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    colors = ['#1a3a6b', '#2d5aa8', '#3d7fcb', '#c8a84b']
    axes[0].bar(names, [v * 100 for v in acc_vals], color=colors)
    axes[0].set_title('Model Accuracy Comparison', fontsize=13, fontweight='bold')
    axes[0].set_ylabel('Accuracy (%)')
    axes[0].set_ylim(50, 100)
    axes[0].tick_params(axis='x', rotation=15)
    for i, v in enumerate(acc_vals):
        axes[0].text(i, v * 100 + 0.5, f'{v*100:.2f}%', ha='center', fontsize=10)

    axes[1].bar(names, auc_vals, color=colors)
    axes[1].set_title('Model ROC-AUC Comparison', fontsize=13, fontweight='bold')
    axes[1].set_ylabel('ROC-AUC Score')
    axes[1].set_ylim(0.5, 1.0)
    axes[1].tick_params(axis='x', rotation=15)
    for i, v in enumerate(auc_vals):
        axes[1].text(i, v + 0.005, f'{v:.4f}', ha='center', fontsize=10)

    plt.tight_layout()
    plt.savefig(os.path.join(MODEL_DIR, 'model_comparison.png'), dpi=150, bbox_inches='tight')
    plt.close()

    # Confusion matrices (2×2 grid)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    for ax, name in zip(axes.flatten(), names):
        cm = results[name]['cm']
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                    xticklabels=['Rejected', 'Approved'],
                    yticklabels=['Rejected', 'Approved'])
        ax.set_title(f'{name}\nAccuracy: {results[name]["accuracy"]*100:.2f}%',
                     fontweight='bold')
        ax.set_ylabel('Actual')
        ax.set_xlabel('Predicted')
    plt.tight_layout()
    plt.savefig(os.path.join(MODEL_DIR, 'confusion_matrices.png'), dpi=150, bbox_inches='tight')
    plt.close()

    # ROC curves — all models on one plot
    roc_colors = ['#1a3a6b', '#e74c3c', '#27ae60', '#f39c12']
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot([0, 1], [0, 1], 'k--', lw=1, label='Random Classifier')
    for (name, res), color in zip(results.items(), roc_colors):
        fpr, tpr, _ = roc_curve(y_test, res['model'].predict_proba(X_test)[:, 1])
        ax.plot(fpr, tpr, label=f"{name} (AUC={res['roc_auc']:.3f})", color=color, lw=2)

    ax.set_xlabel('False Positive Rate', fontsize=12)
    ax.set_ylabel('True Positive Rate', fontsize=12)
    ax.set_title('ROC Curves — All Models', fontsize=13, fontweight='bold')
    ax.legend(loc='lower right')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(MODEL_DIR, 'roc_curves.png'), dpi=150, bbox_inches='tight')
    plt.close()

    print("\nPlots saved to models/")


def main():
    global X_test_global

    print("=" * 55)
    print("  Credit Card Approval Prediction — Model Training")
    print("=" * 55)

    # 1. Load
    app_df, credit_df = load_data()

    # 2. Build target
    target_df = build_target(credit_df)

    # 3. Merge application data with target
    df = app_df.merge(target_df, on='ID', how='inner')
    df.drop(columns=['ID'], inplace=True)
    print(f"\nMerged dataset     : {df.shape[0]:,} records")

    # 4. Feature engineering
    df = engineer_features(df)

    # 5. Preprocess
    df_proc, scaler, encoders = preprocess(df[FEATURE_COLS + ['TARGET']])

    X = df_proc[FEATURE_COLS]
    y = df_proc['TARGET']

    # 6. Train / test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    X_test_global = X_test
    print(f"Train size: {len(X_train):,}  |  Test size: {len(X_test):,}")

    # 7. Train all models
    results = train_all_models(X_train, X_test, y_train, y_test)

    # 8. Select best model
    best_name  = max(results, key=lambda k: results[k]['accuracy'])
    best_model = results[best_name]['model']
    print(f"\n{'='*55}")
    print(f"  Best model: {best_name}")
    print(f"  Accuracy  : {results[best_name]['accuracy']*100:.2f}%")
    print(f"  ROC-AUC   : {results[best_name]['roc_auc']:.4f}")
    print(f"{'='*55}")

    # 9. Save artifacts
    joblib.dump(best_model, os.path.join(MODEL_DIR, 'model.pkl'))
    joblib.dump(scaler,     os.path.join(MODEL_DIR, 'scaler.pkl'))
    joblib.dump(encoders,   os.path.join(MODEL_DIR, 'encoder.pkl'))

    comparison = {
        name: {'accuracy': r['accuracy'], 'roc_auc': r['roc_auc']}
        for name, r in results.items()
    }
    joblib.dump(
        {'comparison': comparison, 'best_model': best_name, 'feature_cols': FEATURE_COLS},
        os.path.join(MODEL_DIR, 'metadata.pkl')
    )

    # 10. Save plots
    try:
        save_plots(results, X_test, y_test)
    except Exception as e:
        print(f"Note: Could not save plots ({e})")

    print("\nArtifacts saved to models/:")
    print("  model.pkl, scaler.pkl, encoder.pkl, metadata.pkl")
    print("\nRun 'python app.py' to start the web application.")


if __name__ == '__main__':
    main()
