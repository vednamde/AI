def is_goal(state, goal):
    return goal in state

def get_possible_moves(state, a_cap, b_cap):
    a, b = state
    moves = []

    # Fill Jug A
    moves.append((a_cap, b))
    # Fill Jug B
    moves.append((a, b_cap))
    # Empty Jug A
    moves.append((0, b))
    # Empty Jug B
    moves.append((a, 0))
    # Pour A → B
    pour = min(a, b_cap - b)
    moves.append((a - pour, b + pour))
    # Pour B → A
    pour = min(b, a_cap - a)
    moves.append((a + pour, b - pour))

    return moves

def dfs_water_jug(a_cap, b_cap, goal):
    start = (0, 0)
    stack = [(start, [start])]
    visited = set()

    while stack:
        (state, path) = stack.pop()
        if state in visited:
            continue
        visited.add(state)

        if is_goal(state, goal):
            return path

        for move in get_possible_moves(state, a_cap, b_cap):
            if move not in visited:
                stack.append((move, path + [move]))

    return None

# Example usage
if __name__ == "__main__":
    A_CAPACITY = 6
    B_CAPACITY = 5
    GOAL = 4  # Goal: get 4 liters in either jug

    solution = dfs_water_jug(A_CAPACITY, B_CAPACITY, GOAL)
    if solution:
        print("Solution found:")
        for step in solution:
            print(f"Jug A: {step[0]}L, Jug B: {step[1]}L")
    else:
        print("No solution found.")
