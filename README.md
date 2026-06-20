# ❤️ Heart Disease Risk Prediction using Machine Learning

## Overview

This project uses Machine Learning to predict the likelihood of heart disease based on a patient's medical information. The application helps assess heart disease risk by analyzing various health indicators and providing a prediction along with confidence probabilities.

A user-friendly Streamlit web application has been developed to allow users to enter their health information and receive instant predictions.

---

## Problem Statement

Heart disease is one of the leading causes of death worldwide. Early identification of high-risk patients can help healthcare professionals take preventive measures and improve patient outcomes.

The objective of this project is to build a machine learning model capable of predicting whether a patient is at risk of heart disease using clinical and demographic data.

---

## Dataset

**Heart Disease Prediction Dataset**

The dataset contains patient information including:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope

**Target Variable**

* 0 → No Heart Disease
* 1 → Heart Disease

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## Machine Learning Workflow

### 1. Data Preprocessing

* Handled categorical variables using One-Hot Encoding
* Feature scaling using StandardScaler
* Train-test split for model evaluation

### 2. Model Training

The following supervised learning algorithms were evaluated:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Naive Bayes
* Decision Tree
* Support Vector Machine (SVM)

### 3. Model Selection

Models were compared using performance metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

The best-performing model was selected and saved as a machine learning pipeline.

---

## Streamlit Application Features

* Interactive user interface
* Medical parameter input forms
* Real-time prediction
* Probability scores for both classes
* Heart disease risk assessment
* Integrated preprocessing pipeline

---

## Project Structure

```text
Heart_Disease_Prediction/
│
├── app.py
├── best_model.pkl
├── columns1.pkl
├── heartpro.ipynb
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Malaika-Ansar/Heart_Disease_Prediction.git
```

Move into the project directory:

```bash
cd Heart_Disease_Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Example Prediction Output

The application provides:

* Heart Disease Probability (%)
* No Heart Disease Probability (%)
* Final Risk Assessment

Example:

```text
Heart Disease Probability: 82.4%

Prediction:
⚠️ High Risk of Heart Disease
```

---

## Future Improvements

* Hyperparameter tuning using GridSearchCV
* Random Forest implementation
* XGBoost implementation
* Cross-validation analysis
* SHAP explainability visualizations
* Feature importance analysis
* Cloud deployment

---

## Author

**Malaika Ansar**

Machine Learning Enthusiast | Software Engineering Student

GitHub: https://github.com/Malaika-Ansar

## ⚠️ Disclaimer

This project is intended for educational and learning purposes only. It is not a medical diagnostic tool and should not replace professional medical advice.


