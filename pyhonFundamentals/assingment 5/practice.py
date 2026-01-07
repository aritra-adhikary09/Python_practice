import json

cities = {
    "Delhi": 19000000,
    "Tokyo": 37000000,
    "New York": 8400000
}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

with open("cities.json", "r") as f:
    loaded_cities = json.load(f)

print("Cities and their population:")
for city, population in loaded_cities.items():
    print(f"{city}: {population}")

new_city = input("Enter a new city name: ")

try:
    new_population = int(input("Enter the population: "))
    loaded_cities[new_city] = new_population

    with open("cities.json", "w") as f:
        json.dump(loaded_cities, f, indent=4)

    print("City added successfully!")
except ValueError:
    print("Invalid population input!")