def estimate_budget(flight_price, hotel_price_per_night, days):

    # Hotel total
    hotel_cost = hotel_price_per_night * days

    # Food + local travel estimate
    local_expense = days * 1500

    # Total cost
    total = flight_price + hotel_cost + local_expense

    return {
        "flight_cost": flight_price,
        "hotel_cost": hotel_cost,
        "local_expense": local_expense,
        "total_budget": total
    }