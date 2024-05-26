import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(
    page_title="Historical Data",
    page_icon="🌎",
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


def format_date(date):
    adate = date / 1000
    date_obj = datetime.utcfromtimestamp(adate)
    date = date_obj.strftime("%d-%m-%Y")
    return date

st.title('Historical Data')

if 'all_records' not in st.session_state:
    st.session_state['all_records'] = get_data_from_flask('all_records')

df = pd.DataFrame(st.session_state['all_records'])


df['date'] = df['date'].apply(format_date)

df['date_time'] = df['date'] + ' ,' + df['time']

st.subheader("Indoor Conditions Over Time")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Average Temperature (°C)", value=round(df['indoor_temp'].mean(), 2))
    fig, ax = plt.subplots()
    ax.plot(df['date_time'], df['indoor_temp'], label='Indoor Temp (°C)', color='blue')
    ax.set_xlabel('Time')
    ax.set_ylabel('Values')
    interval = len(df) // 7
    ax.set_xticks(df['date_time'][::interval])
    ax.set_xticklabels(df['date_time'][::interval], rotation=45)
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.metric(label="Average Indoor Humidity (%)", value=round(df['indoor_humidity'].mean(), 2))
    fig, ax = plt.subplots()
    ax.plot(df['date_time'], df['indoor_humidity'], label='Indoor Humidity (%)', color='green')
    ax.set_xlabel('Time')
    ax.set_ylabel('Values')
    interval = len(df) // 7
    ax.set_xticks(df['date_time'][::interval])
    ax.set_xticklabels(df['date_time'][::interval], rotation=45)
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with col3:
    st.metric(label="Average Indoor Co2 (ppm)", value=round(df['indoor_co2'].mean(), 2))
    fig, ax = plt.subplots()
    ax.plot(df['date_time'], df['indoor_co2'], label='Indoor C02 (ppm)', color='red')
    ax.set_xlabel('Time')
    ax.set_ylabel('Values')
    interval = len(df) // 7
    ax.set_xticks(df['date_time'][::interval])
    ax.set_xticklabels(df['date_time'][::interval], rotation=45)
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("***")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.subheader("Outdoor Conditions Over Time")
    fig2, ax2 = plt.subplots()
    ax2.plot(df['date_time'], df['outdoor_temp'], label='Outdoor Temp (°C)', color='orange')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Temperature (°C)')
    interval = len(df) // 7
    ax2.set_xticks(df['date_time'][::interval])
    ax2.set_xticklabels(df['date_time'][::interval], rotation=45)
    ax2.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig2)


st.markdown("***")
col1, col2, col3 = st.columns([1, 7, 1])
with col2:
    st.dataframe(df)

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
