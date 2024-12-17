"""
This is the logistics module.

It calculates distance between two points. and the time it takes to travel between them.
And other logistics related functions.

For example:

    from geopy import distance

    newport_ri = (41.49008, -71.312796) 
    cleveland_oh = (41.499498, -81.695391)
    print(distance.distance(newport_ri, cleveland_oh).miles)
"""


# build a list of 10 cities in the USA and their coordinates

cities = {
    "New York": (40.7128, 74.0060),
    "Los Angeles": (34.0522, 118.2437),
    "Chicago": (41.8781, 87.6298),
    "Houston": (29.7604, 95.3698),
    "Phoenix": (33.4484, 112.0740),
    "Philadelphia": (39.9526, 75.1652),
}


from geopy import distance

# builf a function to calculate the distance between two cities


def calc_distance(city1, city2):
    """
    Calculate the distance between two cities
    """
    coords_1 = cities[city1]
    coords_2 = cities[city2]

    return distance.distance(coords_1, coords_2).km


# build a function to calculate the time it takes to travel between two cities


def travel_time(city1, city2):
    """
    Calculate the time it takes to travel between two cities
    """
    dist = calc_distance(city1, city2)
    time = dist / 1000

    return time


# build a function to  findthe coordinates of a city by searching for the city in geopy


def get_coords(city):
    """
    Find the coordinates of a city
    """
    return cities[city]


# build a function to calculate the total distance of the cities


def total_distance(cities):
    """
    Calculate the total distance of the cities
    """
    total = 0
    for i in range(len(cities) - 1):
        total += calc_distance(cities[i], cities[i + 1])

    return total


# build a function to calculate the cost of shipping between two cities


def shipping_cost(city1, city2, weight):
    """
    Calculate the cost of shipping between two cities
    """
    time = travel_time(city1, city2)
    cost = time * weight

    return cost


# call the functions

print(calc_distance("New York", "Los Angeles"))
print(travel_time("New York", "Los Angeles"))
print(shipping_cost("New York", "Los Angeles", 10))
