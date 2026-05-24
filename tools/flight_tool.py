import json

def search_flights(source, destination):

    # Open flights JSON file
    with open("data/flights.json", "r", encoding="utf-8") as file:
        flights = json.load(file)

    matching_flights = []

    # Search matching flights
    for flight in flights:

        flight_source = flight.get("from", "")
        flight_destination = flight.get("to", "")

        if (
            flight_source.lower() == source.lower()
            and
            flight_destination.lower() == destination.lower()
        ):

            matching_flights.append(flight)

    # No flights found
    if len(matching_flights) == 0:
        return "No flights found"

    # Find cheapest flight
    cheapest_flight = min(
        matching_flights,
        key=lambda x: x["price"]
    )

    return cheapest_flight