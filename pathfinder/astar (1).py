# astar.py
# --------
# A* (A-STAR) ALGORITHM — finds the SHORTEST PATH, but smarter than Dijkstra
#
# Simple idea:
#   Like Dijkstra, but with a HINT — it also considers straight-line distance
#   to the goal. So it explores places that are CLOSER to the goal first.
#
# The formula:
#   f(place) = g(place) + h(place)
#
#   g(place) = actual cost to reach this place from start
#   h(place) = estimated cost from this place to goal (straight-line distance)
#   f(place) = total estimated cost through this place
#
# Why is it better?
#   Dijkstra searches in ALL directions equally (like a circle growing outward).
#   A* searches mostly TOWARD the goal (like an arrow pointing at the goal).
#   Result: A* visits FEWER nodes but still finds the SHORTEST PATH.
#
# KEY TERM: "Admissible heuristic"
#   Our heuristic (straight-line distance) never OVERESTIMATES the true cost.
#   This guarantees A* still finds the shortest path.

import heapq
import math


def heuristic(positions, place, goal):
    """
    Estimate distance from 'place' to 'goal' using straight-line distance.
    This is the h(n) in the A* formula.
    Straight-line distance is always <= actual road distance, so it's admissible.
    """
    x1, y1 = positions[place]
    x2, y2 = positions[goal]
    return math.hypot(x2 - x1, y2 - y1)


def astar(positions, adjacency, start, end):
    """
    Find shortest path from start to end using A* algorithm.

    Arguments:
        positions - dictionary of { place: (x, y) } for the heuristic
        adjacency - dictionary of { place: [(neighbour, distance), ...] }
        start     - name of starting place (string)
        end       - name of destination place (string)

    Returns:
        path         - list of place names from start to end
        total_cost   - total distance of the path
        visited_log  - list of (place, cost) in the order visited (for animation)
        frontier_log - list of (place, cost) added to queue (for animation)
    """

    # Priority queue stores (f_cost, g_cost, place)
    # f_cost = g_cost + heuristic  ← this is what A* sorts by
    h_start = heuristic(positions, start, end)
    priority_queue = []
    heapq.heappush(priority_queue, (h_start, 0, start))

    # Best known actual cost (g) to reach each place
    g_cost = {start: 0}

    # Remember how we got to each place
    came_from = {start: None}

    # Track finalized places
    visited = set()

    # Logs for animation
    visited_log  = []
    frontier_log = []

    while priority_queue:
        # Pop place with lowest f_cost = g + h
        f, g, current_place = heapq.heappop(priority_queue)

        if current_place in visited:
            continue

        visited.add(current_place)
        visited_log.append((current_place, g))

        # GOAL REACHED — trace back path
        if current_place == end:
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            return path, g, visited_log, frontier_log

        # Check all roads from current place
        for neighbour, road_distance in adjacency[current_place]:
            new_g = g + road_distance  # actual cost to reach neighbour

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                came_from[neighbour] = current_place

                # f = actual cost + straight-line estimate to goal
                h = heuristic(positions, neighbour, end)
                f_new = new_g + h

                heapq.heappush(priority_queue, (f_new, new_g, neighbour))
                frontier_log.append((neighbour, new_g))

    # No path found
    return [], float('inf'), visited_log, frontier_log
