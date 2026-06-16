# ❤️ Heart Disease Prediction App

A Machine Learning-based web application that predicts the likelihood of heart disease using patient health information. The application is built with **Streamlit** and uses a trained **Naive Bayes Pipeline** for prediction.

## 🚀 Features

* Predict heart disease risk instantly
* User-friendly Streamlit interface
* Automatic preprocessing through a Scikit-learn Pipeline
* Displays prediction probabilities
* Uses multiple health indicators for assessment

## 📊 Input Features

The model uses the following information:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG Results
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak (ST Depression)
* ST Slope

## 🤖 Model

The application uses a **Naive Bayes Classifier** trained on a heart disease dataset.

The deployed model is saved as a Scikit-learn Pipeline that automatically handles preprocessing and prediction.

## 📂 Project Structure

```text
.
├── app.py
├── model_NB_pipeline.pkl
├── columns.pkl
└── README.md
```

## 🛠️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

### Install dependencies

```bash
pip install streamlit pandas scikit-learn joblib
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

## 📈 Prediction Output

The model provides:

* Probability of Heart Disease
* Probability of No Heart Disease
* Final Risk Assessment

## ⚠️ Disclaimer

This project is intended for educational and learning purposes only. It is not a medical diagnostic tool and should not replace professional medical advice.

## 👩‍💻 Author

Developed as a Machine Learning project using Python, Scikit-learn, and Streamlit.
