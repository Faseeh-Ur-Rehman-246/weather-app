import streamlit as st
import requests

# WEATHER APP

st.set_page_config(
    page_title="My Weather App",
    page_icon="🌤️",
    layout="centered"
)

# CITY LIST

list_name = [
    "Karachi",
    "Lahore",
    "Faisalabad",
    "Rawalpindi",
    "Multan",
    "Gujranwala",
    "Hyderabad",
    "Khanewal",
    "Peshawar",
    "Islamabad",
    "Quetta",
    "Sargodha",
    "Sialkot",
    "Bahawalpur",
    "Sukkur",
    "Larkana",
    "Nawabshah",
    "Mirpur Khas",
    "Abbottabad",
    "Mardan",
    "Swat"
]

# TITLE

st.title("🌤️ My Weather App")

st.write("Check the current weather of any city in the world.")

# CITY SELECTION

city_option = st.selectbox(
    "Select a City",
    ["Select from List"] + list_name + ["Other City"]
)

# MANUAL CITY INPUT

if city_option == "Other City":

    city = st.text_input(
        "Enter Any City in the World",
        placeholder="Example: London, Tokyo, Dubai, New York"
    )

elif city_option == "Select from List":

    city = ""

else:

    city = city_option

# GET WEATHER BUTTON

if st.button("Done"):

    if city.strip() == "":

        st.warning("Please select a city or enter a city name.")

    else:

        # API KEY

        API_KEY = st.secrets["OPENWEATHER_API_KEY"]

        # API URL

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY
        }

        # GET WEATHER DATA

        response = requests.get(
            url,
            params=params
        )

        # SUCCESS

        if response.status_code == 200:

            data = response.json()

            # WEATHER INFORMATION

            weather_climate = data["weather"][0]["main"]

            weather_description = data["weather"][0]["description"]

            temperature = int(
                data["main"]["temp"] - 273.15
            )

            pressure = data["main"]["pressure"]

            # ACTUAL CITY NAME FROM API

            city_name = data["name"]

            country = data["sys"]["country"]

            # DISPLAY RESULT

            st.subheader(
                f"Weather in {city_name}, {country}"
            )

            # TWO COLUMNS

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Weather Climate",
                    weather_climate
                )

            with col2:

                st.metric(
                    "Temperature",
                    f"{temperature} °C"
                )

            # WEATHER DESCRIPTION

            st.info(
                f"Weather Description: {weather_description}"
            )

            # PRESSURE

            st.success(
                f"Pressure: {pressure} hPa"
            )

        # CITY NOT FOUND

        elif response.status_code == 404:

            st.error(
                f"City '{city}' was not found. Please check the spelling."
            )

        # OTHER API ERROR

        else:

            st.error(
                "Unable to get weather data. Please try again."
            )