import streamlit as st
import requests
from datetime import datetime
import json

st.set_page_config(
    page_title="Home Monitoring",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': " [GitHub](https://github.com/Romainnnnnn/Project_Cloud_and_Advanced_Analytics_2024)"
    }
)

def get_data_from_flask(url_path):
    URL = "https://backendproject-q7qdvoyxja-oa.a.run.app/" + url_path
    response = requests.get(URL)
    return response.json()

if 'last_record' not in st.session_state:
    st.session_state['last_record'] = get_data_from_flask('last_record')

last_record = st.session_state['last_record']

string_data = last_record['data']
data = json.loads(string_data)


adate = data['date']['0'] / 1000
date_obj = datetime.utcfromtimestamp(adate)

date = date_obj.strftime("%d-%m-%Y")
time = data['time']['0']
indoor_temp = data['indoor_temp']['0']
indoor_humidity = data['indoor_humidity']['0']
indoor_co2 = data['indoor_co2']['0']

st.title("Indoor Conditions Monitoring")

st.markdown("***")

st.write(f"**Recorded at:** {time} on {date}")

st.markdown("***")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Indoor Temperature")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfED-3BLG4QiOVM3kueDC9eYhUTI9aN7XM9A&s", width=70)
    st.metric(label="Temperature (°C)", value=f"{indoor_temp}°C")

with col2:
    st.header("Indoor Humidity")
    st.image("https://cdn-icons-png.flaticon.com/512/4148/4148460.png", width=70)
    st.metric(label="Humidity (%)", value=f"{indoor_humidity}%")

with col3:
    st.header("Indoor CO2 Levels")
    st.image("https://icons.veryicon.com/png/o/education-technology/agricultural-facilities/co2.png", width=70)
    st.metric(label="CO2 (ppm)", value=f"{indoor_co2} ppm")

st.markdown("""
    <style>
    .stMetric { 
        text-align: center; 
        font-size: 24px; 
        font-weight: bold; 
    }
    .stHeader, .stTitle { 
        text-align: center; 
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("***")
st.write("Data provided by indoor monitoring system.")


# FOOTER

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button('View Historical Data'):
        st.switch_page('pages/historical_data.py') 
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button('View Forecast'):
        st.switch_page('pages/weather_forecast.py')
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button('Home Monitoring'):
        st.switch_page('pages/home_monitoring.py')
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("***")
st.markdown("<div style='text-align: center;'>For more information, visit our <a href='https://github.com/Romainnnnnn/Project_Cloud_and_Advanced_Analytics_2024'>GitHub repository</a>.</div>", unsafe_allow_html=True)
