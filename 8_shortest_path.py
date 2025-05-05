import heapq

def best_first_city(graph, start, goal, heuristics):
    pq = [(heuristics[start], start, [])]  # Priority Queue: (heuristic, city, path_so_far)
    visited = set()

    while pq:
        _, city, path = heapq.heappop(pq)

        if city in visited:
            continue

        visited.add(city)

        if city == goal:
            return path + [city]

        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [city]))

    return None

# Example Graph
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('G', 4)],
    'C': [('G', 1)],
    'G': []
}

# Heuristic values to goal G
heuristics = {
    'A': 3,
    'B': 5,
    'C': 2,
    'G': 0
}

# Run search
path = best_first_city(graph, 'A', 'G', heuristics)

print("City Path:", path)
