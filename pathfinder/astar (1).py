
import heapq
import math


def heuristic(positions, place, goal):
    x1, y1 = positions[place]
    x2, y2 = positions[goal]
    return math.hypot(x2 - x1, y2 - y1)


def astar(positions, adjacency, start, end):
    h_start = heuristic(positions, start, end)
    priority_queue = []
    heapq.heappush(priority_queue, (h_start, 0, start))
    g_cost = {start: 0}
    came_from = {start: None}
    visited = set()
    visited_log  = []
    frontier_log = []

    while priority_queue:
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
