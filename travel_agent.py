from google import genai
from dotenv import load_dotenv
import os

# Import tools
from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import recommend_places
from tools.budget_tool import estimate_budget

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
# TOOL EXECUTION
# =========================

# Search flights
flight = search_flights(
    "Hyderabad",
    "Delhi"
)

# Recommend hotels
hotels = recommend_hotels(
    "Delhi"
)

# Recommend tourist places
places = recommend_places(
    "Delhi"
)

# Estimate budget
budget = estimate_budget(
    flight["price"],
    hotels[0]["price_per_night"],
    3
)

# =========================
# AI PROMPT
# =========================

prompt = f"""
You are an intelligent AI Travel Planner.

Create a detailed and professional 3-day travel itinerary.

TRAVEL DETAILS

Flight Information:
{flight}

Recommended Hotels:
{hotels}

Tourist Places:
{places}

Budget Information:
{budget}

Requirements:
1. Create day-wise itinerary
2. Suggest best hotel
3. Explain tourist attractions
4. Give budget summary
5. Give travel tips
6. Keep response clean and professional
"""

# =========================
# GENERATE AI RESPONSE
# =========================

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# =========================
# OUTPUT
# =========================

print("\n==============================")
print("     AI TRAVEL PLANNER")
print("==============================\n")

print(response.text)