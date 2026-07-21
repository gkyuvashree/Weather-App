import streamlit as st
import requests
from datetime import datetime
from config import API_KEY

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon=None,
    layout="wide"
)

# ---------------- DESIGN SYSTEM / CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap');

:root {
    --bg-ink: #05070d;
    --surface: rgba(255, 255, 255, 0.045);
    --surface-strong: rgba(255, 255, 255, 0.07);
    --border: rgba(148, 163, 184, 0.14);
    --text-primary: #eef2f8;
    --text-muted: #8b96a8;
    --accent-sky: #4fd1ff;
    --accent-amber: #ffb86b;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* App background */
.stApp {
    background:
        radial-gradient(circle at 12% -10%, rgba(79, 209, 255, 0.08), transparent 45%),
        radial-gradient(circle at 88% 110%, rgba(255, 184, 107, 0.06), transparent 40%),
        var(--bg-ink);
    font-family: 'Inter', sans-serif;
}

/* Global text */
h1, h2, h3, h4, h5, p, label, span, div {
    color: var(--text-primary);
}

h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif;
}

/* Header */
.app-header {
    text-align: center;
    margin-bottom: 6px;
    animation: fadeInUp 0.5s ease both;
}

.app-eyebrow {
    color: var(--accent-sky);
    letter-spacing: 3px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.app-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 42px;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin: 0;
}

.app-subtitle {
    color: var(--text-muted);
    font-size: 15px;
    margin-top: 6px;
    margin-bottom: 30px;
}

/* Search row */
div[data-testid="stHorizontalBlock"] {
    align-items: center;
}

div[data-testid="InputInstructions"] {
    display: none;
}

div[data-testid="stTextInput"] input {
    background: var(--surface) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 12px 16px !important;
    font-family: 'Inter', sans-serif;
}

div[data-testid="stTextInput"] input:focus {
    border: 1px solid var(--accent-sky) !important;
    box-shadow: 0 0 0 1px rgba(79, 209, 255, 0.3) !important;
}

div[data-testid="InputInstructions"] {
    display: none !important;
}

.stButton button {
    background: linear-gradient(135deg, #2563eb, #4fd1ff);
    color: #05070d;
    border: none;
    border-radius: 14px;
    height: 46px;
    font-size: 15px;
    font-weight: 700;
    width: 100%;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(79, 209, 255, 0.25);
}

/* Location pill */
.location-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 8px 18px;
    border-radius: 999px;
    font-size: 14px;
    color: var(--text-muted);
    margin-bottom: 18px;
    animation: fadeInUp 0.5s ease 0.05s both;
}

/* Hero card */
.hero-card {
    display: grid;
    grid-template-columns: 1fr 1.4fr 1fr;
    align-items: center;
    gap: 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 28px;
    padding: 30px 40px;
    backdrop-filter: blur(20px);
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.35);
    animation: fadeInUp 0.55s ease 0.08s both;
}

.hero-icon-col { text-align: center; }

.hero-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 84px;
    height: 84px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(79, 209, 255, 0.16), rgba(255, 184, 107, 0.12));
    border: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 1px;
    color: var(--accent-sky);
}

.hero-center { text-align: center; border-left: 1px solid var(--border); border-right: 1px solid var(--border); }

.hero-temp {
    font-family: 'JetBrains Mono', monospace;
    font-size: 56px;
    font-weight: 600;
    line-height: 1;
    margin: 0;
}

.hero-condition {
    color: var(--text-muted);
    font-size: 16px;
    margin-top: 8px;
    text-transform: capitalize;
}

.hero-right { text-align: right; padding-right: 6px; }

.hero-right .label {
    color: var(--text-muted);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 4px;
}

.hero-right .value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 14px;
}

/* Day progress bar (sunrise -> now -> sunset) */
.day-progress-wrap {
    max-width: 900px;
    margin: 22px auto 0 auto;
    animation: fadeInUp 0.55s ease 0.12s both;
}

.day-progress-labels {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: var(--text-muted);
    margin-bottom: 6px;
    font-family: 'JetBrains Mono', monospace;
}

.day-progress-track {
    position: relative;
    height: 6px;
    border-radius: 999px;
    background: linear-gradient(90deg, #1e293b, var(--accent-amber) 50%, #1e293b);
}

.day-progress-dot {
    position: absolute;
    top: 50%;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--text-primary);
    box-shadow: 0 0 0 4px rgba(238, 242, 248, 0.18);
    transform: translate(-50%, -50%);
}

/* Section headings */
.section-label {
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--text-muted);
    margin: 34px 0 14px 0;
}

/* Metric cards */
.metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 18px 16px;
    text-align: center;
    backdrop-filter: blur(15px);
    transition: transform 0.25s ease, background 0.25s ease, box-shadow 0.25s ease;
    animation: fadeInUp 0.5s ease both;
}

.metric-card:hover {
    transform: translateY(-6px);
    background: var(--surface-strong);
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.3);
}

.metric-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 24px;
    font-weight: 600;
    margin: 6px 0 2px 0;
}

.metric-label {
    color: var(--text-muted);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
}

/* Forecast cards */
.forecast-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 16px 10px;
    text-align: center;
    height: 176px;
    backdrop-filter: blur(15px);
    transition: transform 0.25s ease, background 0.25s ease, box-shadow 0.25s ease;
    animation: fadeInUp 0.5s ease both;
}

.forecast-card:hover {
    transform: translateY(-6px);
    background: var(--surface-strong);
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.3);
}

.forecast-date {
    color: var(--text-muted);
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.forecast-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    margin: 4px 0;
    border-radius: 14px;
    background: rgba(79, 209, 255, 0.08);
    border: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: var(--accent-sky);
}

.forecast-temp {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    font-weight: 600;
}

.forecast-condition {
    color: var(--text-muted);
    font-size: 12px;
    text-transform: capitalize;
}

/* Alerts */
div[data-testid="stAlertContentInfo"] { text-align: center; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #05070d, #0b0f1a);
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] * { color: var(--text-primary); }

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 6px 0 18px 0;
}

.sidebar-logo-icon {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    background: linear-gradient(135deg, rgba(79, 209, 255, 0.25), rgba(255, 184, 107, 0.2));
    border: 1px solid var(--border);
}

.sidebar-logo-text { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 18px; }
.sidebar-logo-sub { color: var(--text-muted); font-size: 11px; margin-top: -2px; }

.sidebar-section-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--text-muted);
    margin: 18px 0 10px 0;
}

.sidebar-feature {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 7px 0;
    font-size: 14px;
}

.sidebar-feature::before {
    content: "";
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--accent-sky);
    flex-shrink: 0;
}

.badge-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }

.badge {
    background: var(--surface-strong);
    border: 1px solid var(--border);
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 12px;
    color: var(--text-muted);
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">W</div>
        <div>
            <div class="sidebar-logo-text">Weather</div>
            <div class="sidebar-logo-sub">Live conditions & forecast</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-label">Features</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-feature">Real-time weather</div>
    <div class="sidebar-feature">5-day forecast</div>
    <div class="sidebar-feature">Sunrise &amp; sunset</div>
    <div class="sidebar-feature">Humidity</div>
    <div class="sidebar-feature">Wind details</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-label">Built With</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="badge-row">
        <span class="badge">Python</span>
        <span class="badge">Streamlit</span>
        <span class="badge">OpenWeather API</span>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FUNCTIONS ----------------

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return None
    return None


def get_forecast(city):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return None
    return None


def get_condition_code(condition):
    condition = condition.lower()
    if "clear" in condition:
        return "CLR"
    elif "cloud" in condition:
        return "CLD"
    elif "rain" in condition or "drizzle" in condition:
        return "RAIN"
    elif "storm" in condition or "thunder" in condition:
        return "STRM"
    elif "snow" in condition:
        return "SNOW"
    elif "mist" in condition or "fog" in condition or "haze" in condition:
        return "FOG"
    else:
        return "N/A"

# ---------------- HEADER ----------------

st.markdown("""
<div class="app-header">
    <div class="app-eyebrow">Live Conditions</div>
    <h1 class="app-title">Weather Dashboard</h1>
    <div class="app-subtitle">Real-time intelligence, powered by the OpenWeather API</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SEARCH ----------------

search_col1, search_col2 = st.columns([4, 1])

with search_col1:
    city = st.text_input("", placeholder="Search any city...", label_visibility="collapsed")

with search_col2:
    search = st.button("Get Weather", use_container_width=True)

# ---------------- MAIN APPLICATION ----------------

if search:
    if city.strip():
        with st.spinner("Fetching weather data..."):
            weather = get_weather(city)

        if weather:
            forecast = get_forecast(city)

            # ---------------- CURRENT DATA ----------------

            name = weather["name"]
            country = weather["sys"]["country"]
            temp = round(weather["main"]["temp"])
            feels = round(weather["main"]["feels_like"])
            humidity = weather["main"]["humidity"]
            pressure = weather["main"]["pressure"]
            wind = weather["wind"]["speed"]
            visibility = round(weather.get("visibility", 0) / 1000, 1)
            condition = weather["weather"][0]["description"]
            icon = get_condition_code(condition)
            sunrise = datetime.fromtimestamp(weather["sys"]["sunrise"])
            sunset = datetime.fromtimestamp(weather["sys"]["sunset"])
            now = datetime.now()

            # ---------------- LOCATION PILL ----------------

            st.markdown(
                f'<div class="location-pill">{name}, {country}</div>',
                unsafe_allow_html=True
            )

            # ---------------- HERO CARD ----------------

            st.markdown(f"""
            <div class="hero-card">
                <div class="hero-icon-col">
                    <div class="hero-icon">{icon}</div>
                </div>
                <div class="hero-center">
                    <p class="hero-temp">{temp}°C</p>
                    <div class="hero-condition">{condition}</div>
                </div>
                <div class="hero-right">
                    <div class="label">Feels Like</div>
                    <div class="value">{feels}°C</div>
                    <div class="label">Location</div>
                    <div class="value">{name}, {country}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # ---------------- DAY PROGRESS ----------------

            day_span = (sunset - sunrise).total_seconds()
            elapsed = (now - sunrise).total_seconds()
            fraction = max(0, min(1, elapsed / day_span)) if day_span > 0 else 0

            st.markdown(f"""
            <div class="day-progress-wrap">
                <div class="day-progress-labels">
                    <span>Sunrise {sunrise.strftime('%H:%M')}</span>
                    <span>Sunset {sunset.strftime('%H:%M')}</span>
                </div>
                <div class="day-progress-track">
                    <div class="day-progress-dot" style="left:{fraction * 100}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # ---------------- METRICS ----------------

            st.markdown('<div class="section-label">Conditions</div>', unsafe_allow_html=True)

            metrics = [
                (f"{humidity}%", "Humidity"),
                (f"{wind} m/s", "Wind"),
                (f"{pressure} hPa", "Pressure"),
                (f"{visibility} km", "Visibility"),
            ]

            metric_cols = st.columns(4)
            for col, (m_value, m_label) in zip(metric_cols, metrics):
                with col:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">{m_label}</div>
                        <div class="metric-value">{m_value}</div>
                    </div>
                    """, unsafe_allow_html=True)

            # ---------------- FORECAST ----------------

            st.markdown('<div class="section-label">5-Day Forecast</div>', unsafe_allow_html=True)

            if forecast:
                daily = [item for item in forecast["list"] if "12:00:00" in item["dt_txt"]]

                forecast_cols = st.columns(5)

                for index, item in enumerate(daily[:5]):
                    date = item["dt_txt"].split()[0]
                    forecast_temp = round(item["main"]["temp"])
                    forecast_condition = item["weather"][0]["description"]
                    forecast_icon = get_condition_code(forecast_condition)

                    with forecast_cols[index]:
                        st.markdown(f"""
                        <div class="forecast-card">
                            <div class="forecast-date">{date}</div>
                            <div class="forecast-icon">{forecast_icon}</div>
                            <div class="forecast-temp">{forecast_temp}°C</div>
                            <div class="forecast-condition">{forecast_condition}</div>
                        </div>
                        """, unsafe_allow_html=True)

        else:
            st.error("City not found. Please check spelling.")

    else:
        st.warning("Please enter a city name.")