import json

def recommend_places(city):

    # Open places JSON
    with open("data/places.json", "r", encoding="utf-8") as file:
        places = json.load(file)

    matching_places = []

    # Search places by city
    for place in places:

        place_city = place.get("city", "")

        if place_city.lower() == city.lower():

            matching_places.append(place)

    # No places found
    if len(matching_places) == 0:
        return "No places found"

    # Return top 5 places
    return matching_places[:5]