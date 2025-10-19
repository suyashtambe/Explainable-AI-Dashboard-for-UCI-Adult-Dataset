# 🎯 Spectra xAI Dashboard

> An Explainable AI (xAI) Prototype for UCI Adult Dataset

## 📌 Quick Links
- [Overview](#-project-overview)
- [Dataset](#-dataset)
- [Features](#-features)
- [Setup](#-installation--setup)
- [Usage](#-usage)
- [Structure](#-folder-structure)
- [Security](#-security--ethics)

## 🔍 Project Overview

The Spectra xAI Dashboard empowers users to understand AI decisions through:

✨ **Key Capabilities**:
- 🔄 Interactive sample selection from UCI Adult dataset
- 📊 XGBoost predictions with probability scores
- 📈 Global feature importance visualization via SHAP
- 🎯 Local SHAP explanations in human-readable format
- ⚖️ Fairness monitoring for sensitive features
- 🔐 Secure authentication system (optional)

> **Why It Matters**: Explainable AI enhances trust, transparency, and fairness in AI systems, allowing users to validate and understand model decisions.

## 📊 Dataset

**Source**: UCI Adult Dataset

| Metric | Value |
|--------|--------|
| Samples | 32,561 |
| Features | 14 input + 1 target |
| Target Classes | 0 (≤50K) / 1 (>50K) |

### Feature Types:
- **Categorical**:
  - workclass
  - education
  - marital-status
  - occupation
  - relationship
  - race
  - sex
  - native-country

- **Numerical**:
  - age
  - fnlwgt
  - education-num
  - capital-gain
  - capital-loss
  - hours-per-week

## 🌟 Features

1. **Model Predictions**
   - XGBoost predictions
   - Probability scores
   
2. **Explanations**
   - Global SHAP summary plots
   - Local SHAP feature influence tables
   
3. **Safety & Security**
   - Sensitive feature monitoring
   - User authentication system

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/spectra-xai-dashboard.git
cd spectra-xai-dashboard
```

### 2. Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

### 3. Dependencies
```bash
pip install -r requirements.txt
```

**Required Packages**:
- streamlit
- shap
- xgboost
- scikit-learn
- pandas
- numpy
- matplotlib
- sqlite3

### 4. Launch Dashboard
```bash
streamlit run dashboard/app.py
```

## 💻 Usage

### Dashboard Navigation
- **Sidebar**: Sample selection & model metrics
- **SHAP Section**: Feature importance & local explanations
- **Trust & Safety**: Sensitive feature monitoring
- **Authentication**: User registration & login

## 📁 Folder Structure
```
spectra-xai-dashboard/
├─ data/
│   └─ adult_prepared.pkl
├─ dashboard/
│   ├─ app.py
│   └─ auth_utils.py
├─ notebooks/
│   └─ shap_lime.ipynb
├─ requirements.txt
└─ README.md
```

## 📦 Deliverables

### 📚 Documentation
- [x] GitHub Repository
- [x] Setup Instructions
- [x] Technical Report (2-3 pages)
- [ ] Demo Video (3-5 min)

### 🔒 Security & Ethics

- **Monitored Features**: age, sex, race
- **Transparency**: SHAP explanations
- **Security**: Authentication system
- **Accountability**: Action logging

---

> **Note**: This prototype focuses on SHAP explanations for clarity, though Decision Tree and LIME explanations are implemented in the codebase.
