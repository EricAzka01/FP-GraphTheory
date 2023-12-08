import random
import time

# Representing a graph as an adjacency matrix
# This represents a simple graph with weighted edges
graph = {
    1: {2: 3, 3: 1},
    2: {1: 3, 4: 5},
    3: {1: 1, 4: 2, 5: 4},
    4: {2: 5, 3: 2, 5: 1},
    5: {3: 4, 4: 1}
}

# Dijkstra's algorithm to find the shortest path
def dijkstra(graph, start, end):
    shortest_distance = {node: float('inf') for node in graph}
    shortest_distance[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current_node = None
        min_distance = float('inf')
        for node in graph:
            if shortest_distance[node] < min_distance and node not in visited:
                current_node = node
                min_distance = shortest_distance[node]

        if current_node is None:
            break

        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = shortest_distance[current_node] + weight
            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance

    # Reconstructing the shortest path
    path = []
    current = end
    while current != start:
        path.append(current)
        for neighbor, weight in graph[current].items():
            if shortest_distance[current] - weight == shortest_distance[neighbor]:
                current = neighbor
                break
    path.append(start)
    return path[::-1]

def simulate_traffic_management():
    while True:
        start_node = random.randint(1, 5)
        end_node = random.randint(1, 5)
        
        shortest_path = dijkstra(graph, start_node, end_node)
        
        print(f"Shortest path from Node {start_node} to Node {end_node}: {shortest_path}")
        
        time.sleep(3)  # Simulate traffic analysis every 3 seconds

# Run the traffic management system
simulate_traffic_management()