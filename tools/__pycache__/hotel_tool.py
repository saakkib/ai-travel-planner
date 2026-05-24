import json

def recommend_hotels(city):

    # Open hotels JSON
    with open("data/hotels.json", "r", encoding="utf-8") as file:
        hotels = json.load(file)

    matching_hotels = []

    # Search hotels by city
    for hotel in hotels:

        hotel_city = hotel.get("city", "")

        if hotel_city.lower() == city.lower():

            matching_hotels.append(hotel)

    # No hotels found
    if len(matching_hotels) == 0:
        return "No hotels found"

    # Sort by rating (highest first)
    sorted_hotels = sorted(
        matching_hotels,
        key=lambda x: x.get("rating", 0),
        reverse=True
    )

    # Return top 3 hotels
    return sorted_hotels[:3]