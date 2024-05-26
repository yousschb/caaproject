import streamlit as st
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.set_page_config(
    page_title="Forecast",
    page_icon="🌤️",
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

st.title('Detailed Weather Forecast')

if 'forecast' not in st.session_state:
    st.session_state['forecast'] = get_data_from_flask('forecast') 


if st.session_state['forecast'].get('cod') == '200':
    st.subheader(f"Weather Forecast for Lausanne")

    daily_forecasts = {}
    for entry in st.session_state['forecast']['list']:
        date = datetime.fromtimestamp(entry['dt']).date()
        if date not in daily_forecasts:
            daily_forecasts[date] = []
        daily_forecasts[date].append(entry)

    all_temps = []
    all_dates = []
    for date, forecasts in daily_forecasts.items():
        with st.expander(f"**Date: {date.strftime('%A, %Y-%m-%d')}**"):
            times = []
            temps = []
            icons = []
            num_forecasts = len(forecasts)
            cols = st.columns(num_forecasts)
            for i, forecast in enumerate(forecasts):
                with cols[i]:
                    time = datetime.fromtimestamp(forecast['dt'])
                    temp = forecast['main']['temp']
                    description = forecast['weather'][0]['description'].capitalize()
                    icon_url = get_data_from_flask(f'get_icon/{forecast["weather"][0]["icon"]}')

                    times.append(time)
                    temps.append(temp)
                    icons.append(icon_url)
                    all_dates.append(time)
                    all_temps.append(temp)

                    st.write(f"**Time:** {time.strftime('%H:%M')}")
                    st.write(f"**Temp:** {temp}°C")
                    st.write(f"**Weather:** {description}")
                    st.image(icon_url, width=70)

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(times, temps, marker='o', linestyle='-', color='blue', alpha=0.6, markerfacecolor='red')
            ax.set_xlabel('Time')
            ax.set_ylabel('Temperature (°C)')
            ax.set_title(f'Temperature Variation on {date.strftime("%A, %Y-%m-%d")}')
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            plt.xticks(rotation=45)
            plt.tight_layout()

            st.pyplot(fig)

    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(all_dates, all_temps, linestyle='-', color='blue', alpha=0.6, markerfacecolor='red')
    ax2.set_ylabel('Temperature (°C)')
    ax2.set_title('Temperature Variation')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%A'))
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig2)
else:
    st.error("API error. Please check the API key or try again later.")

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
