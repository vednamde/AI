import copy
import random

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank tile
]

# Heuristic: Number of misplaced tiles
def heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    return misplaced

# Get position of blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate all possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing algorithm
def hill_climbing(start_state, max_iterations=1000):
    current = start_state
    current_h = heuristic(current)
    steps = 0

    while steps < max_iterations:
        neighbors = get_neighbors(current)
        next_state = None
        best_h = current_h

        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < best_h:
                next_state = neighbor
                best_h = h

        if next_state is None:
            break  # Local optimum reached

        current = next_state
        current_h = best_h
        steps += 1

        print(f"Step {steps} - Heuristic: {current_h}")
        for row in current:
            print(row)
        print()

        if current_h == 0:
            print("Goal reached!")
            return current

    print("Stopped at local optimum or max iterations.")
    return current

# Example usage
if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]
    final_state = hill_climbing(start)
