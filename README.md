Spectra xAI Dashboard

Explainable AI (xAI) Prototype for UCI Adult Dataset

This project demonstrates an interactive dashboard for understanding why an AI model makes a specific prediction. It uses XGBoost for prediction and SHAP for explainability. The dashboard allows users to explore both global and local feature influences, improving transparency, trust, and ethical AI practices.

Table of Contents

Project Overview

Dataset

Features

Installation & Setup

Usage

Folder Structure

Deliverables

Security & Ethics

Notes

Project Overview

The Spectra xAI Dashboard allows users to:

Select any test sample from the UCI Adult dataset.

See the XGBoost model prediction and its probability.

Visualize global feature importance via SHAP.

View local SHAP explanations in human-readable form.

Monitor sensitive features for fairness.

Optional: Secure login with registration for authorized access.

Why it matters:
Explainable AI increases trust, transparency, and fairness in AI systems. Users can understand and validate model decisions.

Dataset

Source: UCI Adult Dataset

Number of Samples: 32,561

Features: 14 input features + 1 target

Feature Types:

Categorical: workclass, education, marital-status, occupation, relationship, race, sex, native-country

Numerical: age, fnlwgt, education-num, capital-gain, capital-loss, hours-per-week

Target Variable:

0 → Income ≤ 50K

1 → Income > 50K

Note on indices: Sample indices (0,1,2,…) in the dashboard refer to rows in the test dataset.

Features

Model Predictions: XGBoost prediction with probability.

Global Feature Importance: SHAP summary plots.

Local Explanation: SHAP table showing how features increase or decrease prediction probability.

Trust & Safety: Highlights sensitive features and their influence on predictions.

Cybersecurity: Optional user login with registration.

Installation & Setup

Follow these steps to set up the project on your local machine:

1. Clone the Repository
git clone https://github.com/<your-username>/spectra-xai-dashboard.git
cd spectra-xai-dashboard

2. Create a Virtual Environment (Recommended)
python -m venv venv


Windows:

venv\Scripts\activate


Linux / Mac:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt


Dependencies include:

streamlit

shap

xgboost

scikit-learn

pandas

numpy

matplotlib

sqlite3 (built-in Python library for authentication)

4. Prepare Dataset

Ensure the preprocessed data file data/adult_prepared.pkl exists. If not, run the preprocessing notebook in notebooks/ to generate it.

5. Run the Dashboard
streamlit run dashboard/app.py


Open the link in your browser (default: http://localhost:8501)

Use the sidebar to select test samples and explore model explanations.

Optional: Register/login to access the secure prototype.

Usage

Sidebar:

Select test sample index

View model comparison (accuracy, F1-score)

Understand what 0 and 1 depict (≤50K and >50K income)

SHAP Section:

Expand to see global feature importance plots

View local explanations table

Trust & Safety Section:

Monitor influence of sensitive features such as age, sex, race

User Authentication:

Register a new account

Login to access the dashboard

Folder Structure - example
spectra-xai-dashboard/
│
├─ data/
│   └─ adult_prepared.pkl          # Preprocessed dataset
│
├─ dashboard/
│   ├─ app.py                      # Streamlit app
│   ├─ auth_utils.py               # User authentication utilities
│   
│
├─ notebooks/
│   └─ shap_lime.ipynb        # SHAP explanation notebook
│
├─ requirements.txt
└─ README.md

Deliverables

GitHub Repository

Code, notebooks, scripts

README with setup instructions

Short Report (2–3 pages)

Problem understanding & rationale

Design & implementation

Results & observations

Security, ethical, and governance considerations

Optional Demo Video (3–5 min)

Screen recording showing sample selection, SHAP explanations, and model predictions

Security & Ethics

Sensitive Features: age, sex, and race are monitored for fairness.

Explainability: SHAP increases transparency.

Secure Access: Optional login system ensures only authorized users interact with the model.

Audit Trails: User actions logged for accountability.

Notes

In the prototype, Decision Tree and LIME explanations were implemented in code but not included in the interactive dashboard for simplicity.

SHAP provides human-readable explanations to make the model predictions understandable.