import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

from auth_utils import register_user, login_user, log_activity

# --------------------------
# Load models and data
# --------------------------
@st.cache_data
def load_data_models():
    X_train, X_test, y_train, y_test, preprocessor = joblib.load(r"C:\Users\Suyash Tambe\Desktop\spectra_xai_project\data\adult_prepared.pkl")
    feature_names = preprocessor.get_feature_names_out()  # dense array features
    xgb_model = joblib.load(r"C:\Users\Suyash Tambe\Desktop\spectra_xai_project\models\xgb_model.pkl")
    dt_model = joblib.load(r"C:\Users\Suyash Tambe\Desktop\spectra_xai_project\models\dt_model.pkl")
    return X_train, X_test, y_train, y_test, preprocessor, feature_names, xgb_model, dt_model

X_train, X_test, y_train, y_test, preprocessor, feature_names, xgb_model, dt_model = load_data_models()
X_test_dense = X_test.toarray() if hasattr(X_test, "toarray") else X_test


model_comp = pd.read_csv(r"C:\Users\Suyash Tambe\Desktop\spectra_xai_project\data\model_comparison.csv")


# User Authentication



# Sidebar: User Authentication
st.sidebar.title("🔐 User Authentication")
auth_action = st.sidebar.radio("Select Action", ["Login", "Register"])

if auth_action == "Register":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Register"):
        success, msg = register_user(username, password)
        st.sidebar.success(msg) if success else st.sidebar.error(msg)

else:  
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        success, user_id, msg = login_user(username, password)
        if success:
            st.session_state.user_id = user_id
            st.sidebar.success(f"Logged in as {username}")
        else:
            st.sidebar.error(msg)

# Proceed only if logged in
if "user_id" in st.session_state:
    st.title(" AI Explainer Dashboard")
    st.markdown("Explore why the AI model made a specific prediction on the UCI Adult dataset.")

    # Sidebar: Sample Selection
    st.sidebar.title(" Sample Selection")
    sample_ids = list(range(X_test_dense.shape[0]))
    sample_display = [f"Index {i}" for i in sample_ids]
    selected_sample = st.sidebar.selectbox("Select a Test Sample", sample_display)
    sample_index = int(selected_sample.split()[1])
    st.sidebar.write("Selected sample index:", sample_index)

    log_activity(st.session_state.user_id, "Selected sample", sample_index)

    # Sidebar: Model comparison
    st.sidebar.subheader("📊 Model Comparison")
    st.sidebar.dataframe(model_comp)

    # Sidebar: Explain what 0/1 means
    st.sidebar.subheader(" Class Meaning")
    st.sidebar.markdown("""
    **Class 0:** <=50K income  
    **Class 1:** >50K income
    """)


    sample = X_test_dense[sample_index].reshape(1, -1)
    xgb_pred_proba = xgb_model.predict_proba(sample)[0,1]
    xgb_pred = xgb_model.predict(sample)[0]
    dt_pred = dt_model.predict(sample)[0]

    
    # Predictions
    
    st.subheader(" Model Predictions")
    st.write(f"**XGBoost Prediction:** {xgb_pred} with probability {xgb_pred_proba:.2f}")
    st.write(f"**Decision Tree Prediction:** {dt_pred}")

    # SHAP Explanation
    
    st.subheader(" Human-Readable SHAP Explanation")
    explainer = shap.Explainer(xgb_model)
    shap_values = explainer(X_test_dense[sample_index].reshape(1, -1))

    shap_df = pd.DataFrame({
        "Feature": feature_names,
        "SHAP Value": shap_values.values[0],
    })
    shap_df["Effect"] = np.where(shap_df["SHAP Value"] >= 0, "Increased", "Decreased")
    shap_df["|SHAP Value|"] = np.abs(shap_df["SHAP Value"])
    shap_df = shap_df.sort_values("|SHAP Value|", ascending=False).drop(columns="|SHAP Value|")
    st.dataframe(shap_df.reset_index(drop=True))


    # Section: Graphs
   
    with st.expander("📊 SHAP Graph "):
        if st.button("Show Summary Plot"):
            shap_values_all = explainer.shap_values(X_test_dense[:1000])
            fig, ax = plt.subplots(figsize=(10,5))
            shap.summary_plot(shap_values_all, X_test_dense[:1000], feature_names=feature_names, show=False)
            st.pyplot(fig)

    
    # Section: Trust & Safety
   
    with st.expander("⚖️ Trust & Safety Insights"):
        sensitive_features = ["age", "sex", "race"]
        st.write("Sensitive features considered for fairness:", sensitive_features)
        st.write("We can analyze SHAP values to check if sensitive features heavily influence predictions.")
        # Highlight if any sensitive feature is in top 5 SHAP contributions
        sorted_features = sorted(zip(feature_names, shap_values.values[0]), key=lambda x: abs(x[1]), reverse=True)
        top_feats = [f[0] for f in sorted_features[:5]]
        sensitive_influence = [f for f in top_feats if f in sensitive_features]
        if sensitive_influence:
            st.warning(f"Sensitive features influencing prediction: {sensitive_influence}")
        else:
            st.success("No sensitive features in top SHAP contributions for this sample.")

    #  Show full feature importance
   
    if st.checkbox("Show full SHAP feature importance (bar plot)"):
        shap_values_all = explainer.shap_values(X_test_dense[:1000])
        fig, ax = plt.subplots(figsize=(10,5))
        shap.summary_plot(shap_values_all, X_test_dense[:1000], feature_names=feature_names, plot_type="bar", show=False)
        st.pyplot(fig)
