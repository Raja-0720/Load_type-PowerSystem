⚡ Power Load Type Prediction System

An end-to-end AI application that predicts power system load conditions (Light, Medium, Maximum) using machine learning and a Streamlit web interface.

Project Overview

Power system load prediction is crucial for efficient energy planning, system reliability, and reducing operational risks.
This project builds a machine learning model that predicts the load type of a power system using historical energy usage, reactive power, environmental, and time-based features.

The trained model is deployed as a real-time Streamlit web application for interactive predictions.

Features

✔ Predicts Light / Medium / Maximum Load
✔ Time-aware ML model
✔ Handles class imbalance
✔ Dark themed modern UI
✔ Real-time prediction using Streamlit
✔ Production-ready serialized model

Machine Learning Details

| Component                | Description                           |
| ------------------------ | ------------------------------------- |
| Problem Type             | Multi-Class Classification            |
| Algorithm                | Random Forest (Class-Weighted)        |
| Scaling                  | StandardScaler                        |
| Class Imbalance Handling | `class_weight='balanced'`             |
| Evaluation Metrics       | Accuracy, Precision, Recall, F1-Score |


Input Features

Feature
Usage (kWh)
Lagging Reactive Power
Leading Reactive Power
CO2 Emission
Lagging Power Factor
Leading Power Factor
Month
Hour

Streamlit Web App

The model is deployed as a dark themed web UI that allows users to input parameters and instantly get predictions.

Tech Stack

Python

Pandas, NumPy

Scikit-learn

Streamlit

Pickle

Project Structure

Power-Load-Predictor/
│
├── app.py
├── load_type_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md

