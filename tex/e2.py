import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(node_position, goal_position):
    # Manhattan distance heuristic
    return abs(node_position[0] - goal_position[0]) + abs(
        node_position[1] - goal_position[1]
    )


def astar(grid, start, goal):
    # Create start and goal node
    start_node = Node(start)
    goal_node = Node(goal)

    # Initialize both open and closed sets
    open_set = []
    closed_set = set()

    # Add the start node to the open set
    heapq.heappush(open_set, start_node)

    # Main loop
    while open_set:
        # Select the node with the lowest f-score
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        # Goal node is reached
        if current_node.position == goal_node.position:
            return reconstruct_path(current_node)

        # Evaluate neighbors
        neighbors = get_neighbors(grid, current_node)
        for neighbor_position in neighbors:
            # Create a neighbor node
            neighbor_node = Node(neighbor_position, current_node)

            # Ignore the neighbor which is already evaluated
            if neighbor_node.position in closed_set:
                continue

            # Calculate the g, h, and f values
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # If a neighbor is in the open set and has a higher f-score, skip it
            if not add_to_open(open_set, neighbor_node):
                continue

            # Otherwise, add the neighbor to the open set
            heapq.heappush(open_set, neighbor_node)

    # Return None if no path is found
    return None


def get_neighbors(grid, node):
    (x, y) = node.position
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    # Filter out invalid neighbors
    valid_neighbors = []
    for nx, ny in neighbors:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            valid_neighbors.append((nx, ny))
    return valid_neighbors


def add_to_open(open_set, neighbor):
    for node in open_set:
        if neighbor.position == node.position and neighbor.g >= node.g:
            return False
    return True


def reconstruct_path(current_node):
    path = []
    while current_node:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]  # Return reversed path


# Example usage
grid = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

start = (0, 0)
goal = (4, 6)

path = astar(grid, start, goal)
print("Path:", path)
