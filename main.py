from tools.budget_tool import estimate_budget

# Example values
flight_price = 2907
hotel_price_per_night = 3650
days = 3

result = estimate_budget(
    flight_price,
    hotel_price_per_night,
    days
)

print("\n===== BUDGET ESTIMATION =====\n")

print(result)