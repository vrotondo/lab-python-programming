# Pizza Order Cost Calculator

# Get user input
print("Welcome to Rotondo's Pizza Cost Calculator!")

# Ask for pizza style
size = input("What size pizza would you like? (small, medium, large): ").strip().lower()

# Ask for the number of toppings
toppings = int(input("How many extra toppings would you like? "))  # Added space after ?

# Ask for delivery distance
distance = int(input("What is the delivery distance in miles? "))  # Added space after ?

# Calculate base cost based on pizza style
if size == 'small':
    base_cost = 8
elif size == 'medium':
    base_cost = 10
elif size == 'large':
    base_cost = 12
else:
    print("Invalid pizza size. Please enter small, medium, or large.")
    exit()

# Calculate toppings cost ($1 per topping)
toppings_cost = toppings * 1

# Calculate delivery fee
# $2 for first 5 miles, $1 for each additional mile
if distance <= 0:
    delivery_fee = 0
elif distance >= 5 and distance <= 10:  # Fixed syntax error here (=< to <=)
    delivery_fee = 2
elif distance > 10:
    delivery_fee = 3
else:
    additional_miles = distance - 5
    delivery_fee = 2 + (additional_miles * 1)

# Calculate total cost
total_cost = base_cost + toppings_cost + delivery_fee

# Display the result with formatted output
print("\n--- Order Summary ---")
print(f"Pizza Size: {size.capitalize()}")
print(f"Base Cost: ${base_cost:.2f}")
print(f"Number of Toppings: {toppings}")
print(f"Toppings Cost: ${toppings_cost:.2f}")
print(f"Delivery Distance: {distance} miles")
print(f"Delivery Fee: ${delivery_fee:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print("Thank you for your order!")