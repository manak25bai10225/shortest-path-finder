# graph.py
# --------
# This file creates the city map.
# A city map is just a GRAPH:
#   - NODES = places (like "Airport", "Hospital")
#   - EDGES = roads connecting two places
#   - WEIGHT = distance of that road (shorter road = smaller number)

import math

# The city is stored as two simple dictionaries:
#
# node_positions = { "Place Name": (x, y) }
#   tells us WHERE each place is on the screen
#
# adjacency = { "Place Name": [("Neighbour", distance), ...] }
#   tells us which places are connected by roads


def get_distance(positions, place_a, place_b):
    """Calculate straight-line distance between two places."""
    x1, y1 = positions[place_a]
    x2, y2 = positions[place_b]
    return round(math.hypot(x2 - x1, y2 - y1), 2)


def add_road(adjacency, positions, place_a, place_b):
    """Connect two places with a road. Distance is auto-calculated."""
    dist = get_distance(positions, place_a, place_b)
    adjacency[place_a].append((place_b, dist))
    adjacency[place_b].append((place_a, dist))  # road goes both ways


def build_city():
    """
    Build and return a sample city with 20 places and roads.
    Returns two things:
        positions  - where each place is (x, y)
        adjacency  - which places are connected
    """

    # --- Step 1: Define all places and their (x, y) position on screen ---
    positions = {
        # City centre
        "Central Station": (350, 270),
        "City Hall":        (230, 270),
        "Market Square":    (470, 270),
        "University":       (350, 150),
        "Hospital":         (350, 390),
        "Museum":           (230, 150),
        "Stadium":          (470, 150),
        "Old Town":         (230, 390),
        "Tech Park":        (470, 390),

        # Outer ring road
        "North Gate":       (350,  60),
        "South Gate":       (350, 480),
        "West Gate":        (100, 270),
        "East Gate":        (600, 270),
        "NW Corner":        (100,  60),
        "NE Corner":        (600,  60),
        "SW Corner":        (100, 480),
        "SE Corner":        (600, 480),

        # Extra places
        "Airport":          (600, 150),
        "Harbor":           (600, 390),
        "Suburbs":          (100, 390),
    }

    # --- Step 2: Start with empty adjacency list for every place ---
    adjacency = {place: [] for place in positions}

    # --- Step 3: Connect places with roads ---
    roads = [
        # Inner city roads
        ("Central Station", "City Hall"),
        ("Central Station", "Market Square"),
        ("Central Station", "University"),
        ("Central Station", "Hospital"),
        ("City Hall",       "Museum"),
        ("City Hall",       "Old Town"),
        ("Market Square",   "Stadium"),
        ("Market Square",   "Tech Park"),
        ("University",      "Museum"),
        ("University",      "Stadium"),
        ("Hospital",        "Old Town"),
        ("Hospital",        "Tech Park"),

        # Diagonal shortcuts through city centre
        ("Museum",    "Central Station"),
        ("Stadium",   "Central Station"),
        ("Old Town",  "Central Station"),
        ("Tech Park", "Central Station"),

        # Outer ring road
        ("NW Corner",  "North Gate"),
        ("North Gate", "NE Corner"),
        ("NE Corner",  "East Gate"),
        ("East Gate",  "SE Corner"),
        ("SE Corner",  "South Gate"),
        ("South Gate", "SW Corner"),
        ("SW Corner",  "West Gate"),
        ("West Gate",  "NW Corner"),

        # Ring road connecting to inner city
        ("NW Corner",   "Museum"),
        ("NE Corner",   "Airport"),
        ("Airport",     "Stadium"),
        ("Airport",     "East Gate"),
        ("East Gate",   "Harbor"),
        ("Harbor",      "Tech Park"),
        ("Harbor",      "SE Corner"),
        ("South Gate",  "Hospital"),
        ("SW Corner",   "Suburbs"),
        ("Suburbs",     "Old Town"),
        ("Suburbs",     "West Gate"),
        ("West Gate",   "City Hall"),
        ("North Gate",  "University"),
        ("NW Corner",   "West Gate"),
    ]

    for place_a, place_b in roads:
        add_road(adjacency, positions, place_a, place_b)

    return positions, adjacency
