'''Create a Python dictionary that stores 3 city names and their populations.
Save this data into a file called cities.json.

Then:

Read the JSON file and print each city with its population.

Ask the user to enter a new city name and population, 
and update the JSON file with this new data.'''
# answer:
import json
Cities ={
    "Delhi": 19000000,
    "Tokyo": 37000000,
    "New York": 8400000
}

with open("cities.json","w") as f:
    json.dump(Cities,f)

with open("cities.json","r") as f:
    loaded_cities = json.load(f)

print("Cities and their population: ")

for city, population in loaded_cities.items():
    print(city,":",population)

new_city = input("Enter a new city name: ")
new_population = int(input("Enter the population: "))

loaded_cities[new_city] = new_population

with open("cities.json","w") as f:
    json.dump(loaded_cities,f)

print("Citiy added succesfully!")

# better and got this code from TA
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