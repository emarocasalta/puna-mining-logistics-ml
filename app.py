#Streamlit app
import streamlit as st
import pandas as pd
import joblib

#Page setup
st.set_page_config(page_title="Puna Mining Logistics", page_icon="🚚")

#Load the model
@st.cache_resource

def load_model():
    return joblib.load('mining_logistics_model.joblib')
model = load_model()
 
st.title("🚚 Mining Dispatch Optimizer")
st.markdown("Prediction of times and risks on high altitude routes")

# Sidebar (inputs)
st.sidebar.header("Trip Parameters")
origin = st.sidebar.selectbox("Origin", ["Gral Guemes", "Salta Capital", "San Antonio de los Cobres"])
destiny = st.sidebar.selectbox("Destiny", ["Salar de Pocitos", "Salar del Hombre Muerto", "Tolar Grande", "San Antonio de los Cobres"])
weather = st.sidebar.selectbox("Current weather", ["clear", "white wind", "rain", "snow"])
truck = st.sidebar.selectbox("Unit type", ["bitrain", "semitrailer", "4x4 truck"])
charge = st.sidebar.slider("Charge (tons)", 20.00, 45.00, 30.00)
exp = st.sidebar.slider("Driver experience (years)", 1, 20, 10)

#Calculation logic
distances = {
    ("Gral Guemes", "San Antonio de los Cobres"): 224,
    ("San Antonio de los Cobres", "Salar de Pocitos"): 108,
    ("Salar de Pocitos", "Salar del Hombre Muerto"): 100,
    ("Salta Capital", "San Antonio de los Cobres"): 170,
    ("Gral Guemes", "Salta Capital"): 59,
    ("San Antonio de los Cobres", "Salar del Hombre Muerto"): 200
}

mbsl_destiny = {
    "San Antonio de los Cobres": 3775,
    "Salar de Pocitos": 3650,
    "Salar del Hombre Muerto": 4000,
    "Tolar Grande": 3508,
    "Salta Capital": 1187
}

if st.button("Calculate Shipping Risk"):
    #Get distance (searching both ways)
    dist = distances.get((origin, destiny)) or distances.get((destiny, origin)) or 150
    alt = mbsl_destiny.get(destiny, 3000)
    
    #Input for the model
    input_df = pd.DataFrame([{
        'altitude_destiny_mbsl': alt,
        'distance_km': dist,
        'unit_type': truck,
        'charge_tons': charge,
        'weather': weather,
        'driver_experience_years': exp
    }])
    
    pred_hs = model.predict(input_df)[0]

    #Show results 
    st.divider()
    col1, col2, col3 = st.columns(3)
    
    theorical = dist / 45
    delay = max(0, pred_hs - theorical)
    cost = delay * 500
    
    col1.metric("Predicted Estimated Time Arrival", f"{pred_hs:.2f} hs")
    col2.metric("Estimated Delay", f"{delay:.2f} hs", delta_color='inverse')
    col3.metric("Risk Cost", f"${cost:.0f} USD")
    
    if cost < 300:
        st.success("**Authorized Delivery:** Safe conditions.")
    elif cost < 1000:
        st.warning("**Attention:** Moderate delays are expected. High cost risk.")
    else:
        st.error("**Critical Clearance:** Exit is NOT recommended due high delay cost.")