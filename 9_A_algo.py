import heapq

# Heuristic: number of misplaced tiles
def heuristic(state, goal):
    return sum(1 if state[i] != goal[i] and state[i] != 0 else 0 for i in range(9))

# Possible moves for each position
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def a_star_8_puzzle(start, goal):
    pq = [(heuristic(start, goal), 0, start, [])]  # (f = g + h, g, state, path)
    visited = set()
    
    while pq:
        f, g, state, path = heapq.heappop(pq)
        
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        
        if state == goal:
            return path + [state]
        
        zero_pos = state.index(0)
        for move_pos in moves[zero_pos]:
            new_state = state[:]
            new_state[zero_pos], new_state[move_pos] = new_state[move_pos], new_state[zero_pos]
            if tuple(new_state) not in visited:
                new_g = g + 1
                h = heuristic(new_state, goal)
                heapq.heappush(pq, (new_g + h, new_g, new_state, path + [state]))
    
    return None

# Example
start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solution = a_star_8_puzzle(start, goal)

print("A* 8 Puzzle Path:")
for step in solution:
    print(step[:3])
    print(step[3:6])
    print(step[6:])
    print("---")
