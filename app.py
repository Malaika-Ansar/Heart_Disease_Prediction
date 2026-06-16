
import streamlit as st
import pandas as pd
import joblib

# Load ONLY pipeline and columns
pipe = joblib.load("model_NB_pipeline.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("Heart Disease Prediction")
st.markdown("Provide the following details to check your heart disease risk:")

# ---------------- INPUTS ----------------
age = st.slider("Age", 18, 100, 40)

sex = st.selectbox("Sex", ["M", "F"])

chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])

resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)

cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)

fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])

resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])

max_hr = st.slider("Max Heart Rate", 60, 220, 150)

exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])

oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)

st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# ---------------- PREDICT ----------------
if st.button("Predict"):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Fill missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns EXACTLY
    input_df = input_df[expected_columns]

    # ================= DEBUG =================
    st.subheader("Input Sent To Model")
    st.dataframe(input_df)

    # 🚀 IMPORTANT: NO SCALING HERE (PIPELINE HANDLES IT)
    prediction = pipe.predict(input_df)[0]

    probabilities = pipe.predict_proba(input_df)[0]

    st.subheader("Prediction Probabilities")

    st.write(f"✅ No Heart Disease Probability: {probabilities[0]*100:.2f}%")
    st.write(f"⚠️ Heart Disease Probability: {probabilities[1]*100:.2f}%")

    st.subheader("Final Prediction")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")