import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def f(self):
        return self.g + self.h

def astar_search(start_state, goal_state, heuristic):
    open_list = []
    closed_set = set()

    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_list, (start_node.f(), id(start_node), start_node))

    while open_list:
        _, _, current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor_state in get_neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue

            g = current_node.g + 1  # Assuming uniform cost for all edges
            h = heuristic(neighbor_state, goal_state)
            neighbor_node = Node(neighbor_state, current_node, g, h)

            heapq.heappush(open_list, (neighbor_node.f(), id(neighbor_node), neighbor_node))

    return None

def get_neighbors(state):
    x, y = state
    # Assuming movement is allowed in 4 directions (up, down, left, right)
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return neighbors


def heuristic(state, goal_state):
    # Assuming state and goal_state are tuples representing coordinates (x, y)
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

# Example usage:
start_state = (0, 0)  # Example start state, replace with actual start state
goal_state = (5, 5)   # Example goal state, replace with actual goal state
path = astar_search(start_state, goal_state, heuristic)
print("A* Path:", path)
