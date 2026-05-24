import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Import tools
from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import recommend_places
from tools.budget_tool import estimate_budget
from tools.weather_tool import get_weather

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

# =========================
# GEMINI CLIENT
# =========================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("✈️ AI Travel Planner")

st.write(
    "Plan smart trips using Generative AI 🚀"
)

# =========================
# USER INPUTS
# =========================

source = st.text_input(
    "Enter Source City",
    "Hyderabad"
)

destination = st.text_input(
    "Enter Destination City",
    "Delhi"
)

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=3
)

# =========================
# GENERATE BUTTON
# =========================

if st.button("Generate Travel Plan"):

    try:

        # =========================
        # FLIGHT SEARCH
        # =========================

        flight = search_flights(
            source,
            destination
        )

        # =========================
        # HOTEL RECOMMENDATION
        # =========================

        hotels = recommend_hotels(
            destination
        )

        # =========================
        # PLACES RECOMMENDATION
        # =========================

        places = recommend_places(
            destination
        )

        # =========================
        # WEATHER FORECAST
        # Delhi coordinates
        # =========================

        weather = get_weather(
            28.6139,
            77.2090
        )

        temperatures = weather["daily"]["temperature_2m_max"]

        # =========================
        # BUDGET ESTIMATION
        # =========================

        budget = estimate_budget(
            flight["price"],
            hotels[0]["price_per_night"],
            days
        )

        # =========================
        # AI PROMPT
        # =========================

        prompt = f"""
        You are an intelligent AI Travel Planner.

        Create a detailed and professional travel itinerary.

        TRAVEL DETAILS

        Flight Information:
        {flight}

        Recommended Hotels:
        {hotels}

        Tourist Places:
        {places}

        Weather Forecast:
        {temperatures}

        Budget Information:
        {budget}

        Requirements:
        1. Create day-wise itinerary
        2. Include weather for each day
        3. Suggest best hotel
        4. Explain tourist attractions
        5. Give budget summary
        6. Give travel tips
        7. Explain why recommendations were selected
        8. Keep response clean and professional
        """

        # =========================
        # GENERATE AI RESPONSE
        # =========================

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        # =========================
        # DISPLAY RESULTS
        # =========================

        st.success("Travel Plan Generated Successfully ✅")

        st.subheader("🛫 Flight Details")
        st.write(flight)

        st.subheader("🏨 Recommended Hotels")
        st.write(hotels)

        st.subheader("📍 Tourist Places")
        st.write(places)

        st.subheader("🌦️ Weather Forecast")
        st.write(temperatures)

        st.subheader("💰 Budget Estimation")
        st.write(budget)

        st.subheader("🤖 AI Travel Plan")
        st.write(response.text)

    except Exception as e:

        st.error(f"Error: {e}")