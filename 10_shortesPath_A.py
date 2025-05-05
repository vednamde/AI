import heapq

def a_star_city(graph, start, goal, heuristics):
    pq = [(heuristics[start], 0, start, [])]  # (f = h + g, g, city, path)
    visited = set()

    while pq:
        f, g, city, path = heapq.heappop(pq)

        if city in visited:
            continue

        visited.add(city)

        if city == goal:
            return path + [city]

        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                new_g = g + cost
                h = heuristics[neighbor]
                heapq.heappush(pq, (new_g + h, new_g, neighbor, path + [city]))

    return None

# Simple Graph
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('G', 4)],
    'C': [('G', 1)],
    'G': []
}

# Heuristic values to goal 'G' (arbitrary values for example)
heuristics = {
    'A': 3,
    'B': 5,
    'C': 2,
    'G': 0
}

path = a_star_city(graph, 'A', 'G', heuristics)

print("A* City Path:", path)
