import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Power Load Predictor", layout="centered")

# Load model
model = pickle.load(open("load_type_model.pkl", "rb"))

st.markdown("<h1 style='color:white;'>⚡ Power Load Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gray;'>Predict power system load condition</p>", unsafe_allow_html=True)

usage = st.number_input("Usage (kWh)")
lag_reactive = st.number_input("Lagging Reactive Power (kVarh)")
lead_reactive = st.number_input("Leading Reactive Power (kVarh)")
co2 = st.number_input("CO2 Emission")
lag_pf = st.number_input("Lagging Power Factor")
lead_pf = st.number_input("Leading Power Factor")
month = st.selectbox("Month", list(range(1,13)))
hour = st.selectbox("Hour", list(range(0,24)))

if st.button("🔮 Predict Load Type"):
    input_data = np.array([[usage, lag_reactive, lead_reactive, co2,
                             lag_pf, lead_pf, month, hour]])

    pred = model.predict(input_data)[0]

    if pred == "Light_Load":
        st.success("🟢 Light Load")
    elif pred == "Medium_Load":
        st.warning("🟡 Medium Load")
    else:
        st.error("🔴 Maximum Load")
