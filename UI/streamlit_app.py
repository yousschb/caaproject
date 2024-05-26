import streamlit as st
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from st_pages import Page, show_pages, add_page_title

# Page configuration
st.set_page_config(
    page_title="Home Monitoring App",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "[GitHub](https://github.com/Romainnnnnn/Project_Cloud_and_Advanced_Analytics_2024)"
    }
)

show_pages(
    [
        Page("streamlit_app.py", "Welcome", "🏠"),
        Page("pages/home_monitoring.py", "Home Monitoring", "🏠"),
        Page("pages/historical_data.py", "Historical Data", "🌎"),
        Page("pages/weather_forecast.py", "Forecast", "🌤️"),
    ]
)
# Function to get data from Flask
def get_data_from_flask(url_path):
    URL = "https://backendproject-q7qdvoyxja-oa.a.run.app/" + url_path
    response = requests.get(URL)
    return response.json()

# Centered title and welcome message
st.markdown("<h1 style='text-align: center;'>Welcome to Home Monitoring App</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'><img src='https://www.g4s.com/en-sa/-/media/g4s/saudiarabia/images/modules/newsandcontent/ess/s_home_monitoring_systems.ashx' width='300'></div>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center;'>
        <h3>Monitor your home's indoor conditions effortlessly.</h3>
        <ul style='list-style-position: inside;'>
            <li>Track temperature, humidity, and CO2 levels.</li>
            <li>Get real-time data and forecasts.</li>
            <li>Ensure a healthy living environment.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Load data into session state
if 'last_record' not in st.session_state:
    st.session_state['last_record'] = get_data_from_flask('last_record')

if 'forecast' not in st.session_state:
    st.session_state['forecast'] = get_data_from_flask('forecast')

if 'last_record' not in st.session_state:
    st.session_state['last_record'] = get_data_from_flask('last_record')

st.markdown("***")


# FOOTER

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button('View Historical Data  🌎'):
        st.switch_page('pages/historical_data.py') 
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button('View Forecast  🌤️'):
        st.switch_page('pages/weather_forecast.py')
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button('Home Monitoring  🏠'):
        st.switch_page('pages/home_monitoring.py')
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("***")
st.markdown("<div style='text-align: center;'>For more information, visit our <a href='https://github.com/Romainnnnnn/Project_Cloud_and_Advanced_Analytics_2024'>GitHub repository</a>.</div>", unsafe_allow_html=True)
