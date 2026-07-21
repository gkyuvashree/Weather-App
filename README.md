# Weather Dashboard

A real-time weather dashboard application built using Python, Streamlit, and OpenWeather API. The application allows users to search for any city and view current weather conditions along with a 5-day forecast through an interactive and modern interface.

## Overview

Weather Dashboard is a Python-based application that integrates with the OpenWeather API to fetch live weather information. The application provides users with detailed weather insights such as temperature, humidity, wind speed, atmospheric pressure, visibility, sunrise, sunset timings, and upcoming weather forecasts.

The project focuses on API integration, real-time data processing, and building a clean user interface using Streamlit.

## Features

- Real-time weather data retrieval using OpenWeather API
- Search weather information by city name
- Current temperature and feels-like temperature
- Weather condition display with dynamic icons
- Humidity monitoring
- Wind speed information
- Atmospheric pressure details
- Visibility measurement
- Sunrise and sunset timings
- 5-day weather forecast
- Modern dark-themed user interface
- Responsive dashboard layout

## Tech Stack

### Programming Language

- Python

### Framework

- Streamlit

### API

- OpenWeather API

### Libraries Used

- requests - API communication
- python-dotenv - Environment variable management
- datetime - Date and time processing

## Project Structure

```
Weather-App/
│
├── app.py              # Main Streamlit application
├── config.py           # API key configuration
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignored files
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gkyuvashree/Weather-App.git
```

### 2. Navigate to Project Directory

```bash
cd Weather-App
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## API Configuration

This project uses the OpenWeather API to fetch real-time weather information.

### Steps:

1. Create an account on OpenWeather.
2. Generate an API key.
3. Create a file named:

```
config.py
```

4. Add your API key:

```python
API_KEY = "your_api_key_here"
```

Replace `your_api_key_here` with your actual OpenWeather API key.

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

## Application Workflow

1. User enters a city name.
2. The application sends a request to the OpenWeather API.
3. Weather data is received in JSON format.
4. The application processes the response.
5. Weather information is displayed through the Streamlit dashboard.

## Weather Information Displayed

The dashboard provides:

- Current weather condition
- Temperature
- Feels-like temperature
- Humidity percentage
- Wind speed
- Atmospheric pressure
- Visibility distance
- Sunrise time
- Sunset time
- Five-day weather forecast

## Future Improvements

- Add hourly weather forecast visualization
- Add weather maps using geolocation
- Add user current location detection
- Add weather alerts and notifications
- Add historical weather analysis
- Deploy application using Streamlit Cloud

## Learning Outcomes

This project helped implement:

- API integration
- HTTP requests
- JSON data parsing
- Real-time data handling
- Streamlit application development
- User interface design
- Environment variable management

## Author

Yuvashree

GitHub:
https://github.com/gkyuvashree
