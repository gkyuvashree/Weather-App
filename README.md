# Weather Dashboard

A modern real-time weather intelligence dashboard built using Python, Streamlit, and OpenWeather API. The application provides live weather information and a 5-day forecast through a clean, responsive, dark-themed user interface.

## Overview

Weather Dashboard is a web-based weather application that fetches real-time weather data from the OpenWeather API and presents it through an interactive dashboard.

Users can search for any city worldwide and view detailed weather insights including temperature, humidity, wind speed, atmospheric pressure, visibility, sunrise, sunset, and upcoming forecast data.

The project focuses on API integration, real-time data processing, modern UI development, and responsive dashboard design using Streamlit.

## Features

### Real-Time Weather Information

- Search weather data by city name
- Current temperature display
- Feels-like temperature
- Weather condition monitoring
- Location-based weather details

### Weather Metrics

- Humidity percentage
- Wind speed
- Atmospheric pressure
- Visibility distance

### Sun Information

- Sunrise timing
- Sunset timing
- Day progress visualization between sunrise and sunset

### Forecast System

- 5-day weather forecast
- Daily temperature prediction
- Weather condition summary
- Forecast visualization cards

### User Interface

- Modern dark-themed dashboard
- Glassmorphism design
- Responsive layout
- Custom CSS styling
- Interactive hover effects
- Smooth UI animations
- Clean dashboard components

## Tech Stack

### Programming Language

- Python

### Framework

- Streamlit

### API

- OpenWeather API

### Libraries Used

- requests - API communication
- datetime - Time and date processing


##  Live Demo

https://weather-app-oaehaqgkvrwskyeg5uo2qt.streamlit.app/

## Project Structure

```
Weather-App/
│
├── app.py              # Main Streamlit application
├── config.py           # API key configuration
├── requirements.txt    # Project dependencies
├── README.md           # Documentation
└── .gitignore          # Ignored files
```

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/gkyuvashree/Weather-App.git
```

### Navigate to the Project Directory

```bash
cd Weather-App
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## API Configuration

This application uses OpenWeather API for retrieving weather information.

### Steps:

1. Create an account on OpenWeather.
2. Generate an API key.
3. Create a file:

```
config.py
```

4. Add your API key:

```python
API_KEY = "your_api_key_here"
```

Replace `your_api_key_here` with your actual API key.

## Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## Application Workflow

1. User enters a city name.
2. Application sends a request to OpenWeather API.
3. API returns weather information in JSON format.
4. Weather data is processed using Python.
5. Streamlit displays the information through an interactive dashboard.

## Weather Data Displayed

The dashboard provides:

- Current weather condition
- Temperature
- Feels-like temperature
- Humidity
- Wind speed
- Atmospheric pressure
- Visibility
- Sunrise time
- Sunset time
- 5-day forecast

## Design Highlights

The interface includes:

- Custom CSS-based design system
- Dark futuristic theme
- Glass-effect cards
- Responsive dashboard layout
- Minimal and professional UI components
- Smooth transitions and hover interactions

## Error Handling

The application handles:

- Invalid city names
- API request failures
- Network errors
- Missing weather data

## Future Improvements

- Add automatic user location detection
- Add interactive weather maps
- Add hourly weather forecast
- Add historical weather analytics
- Add weather alerts and notifications
- Deploy using Streamlit Cloud

## Learning Outcomes

Through this project, the following concepts were implemented:

- REST API integration
- JSON data processing
- HTTP requests
- Real-time data handling
- Streamlit application development
- Custom UI/UX design
- Environment variable management
- Error handling in API-based applications

## Author

Yuvashree

GitHub:
https://github.com/gkyuvashree
