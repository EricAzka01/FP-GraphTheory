import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
TRAFFIC_SIMULATION_INTERVAL = 3
MAX_TRAFFIC_FLOW = 1000

def collect_traffic_data():
    traffic_flow = min(random.randint(100, 1000), MAX_TRAFFIC_FLOW)
    vehicle_density = random.uniform(0.1, 1.0)
    weather_conditions = random.choice(['sunny', 'rainy', 'windy'])
    return traffic_flow, vehicle_density, weather_conditions

def adjust_traffic_signals(congestion_level):
    if congestion_level == 'Low':
        return "Traffic signals adjusted for Low congestion"
    elif congestion_level == 'Moderate':
        return "Traffic signals adjusted for Moderate congestion"
    else:
        return "Traffic signals adjusted for High congestion"

def analyze_traffic(traffic_flow, vehicle_density):
    if vehicle_density < 0.3:
        return 'Low'
    elif 0.3 <= vehicle_density < 0.7:
        return 'Moderate'
    else:
        return 'High'

def initialize_traffic_graph():
    return {
        'Jalan Sudirman': {'Jalan Thamrin': 3, 'Jalan Kuningan': 2},
        'Jalan Thamrin': {'Jalan Sudirman': 3, 'Jalan MH Thamrin': 1},
        'Jalan Kuningan': {'Jalan Sudirman': 2, 'Jalan Gatot Subroto': 5},
        'Jalan MH Thamrin': {'Jalan Thamrin': 1, 'Jalan Gatot Subroto': 3},
        'Jalan Gatot Subroto': {'Jalan Kuningan': 5, 'Jalan MH Thamrin': 3}
    }

def dijkstra(graph, start, end):
    shortest_distance = {node: float('inf') for node in graph}
    shortest_distance[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda x: shortest_distance[x])
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = shortest_distance[current_node] + weight
            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance

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

def print_traffic_info(traffic_flow, vehicle_density, weather_conditions):
    print(f"Traffic Flow: {traffic_flow} vehicles/hour")
    print(f"Vehicle Density: {vehicle_density:.2f} vehicles/km^2")
    print(f"Weather: {weather_conditions}")

def print_shortest_path(start_node, end_node, shortest_path):
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")

def visualize_traffic_flow(ax, traffic_flow, weather_conditions):
    labels = ['Traffic Flow']
    values = [traffic_flow]

    ax.clear()
    ax.bar(labels, values, color=['blue'])
    ax.set_title('Traffic Flow Visualization')
    ax.set_ylim(0, MAX_TRAFFIC_FLOW)

def visualize_vehicle_density(ax, vehicle_density, weather_conditions):
    labels = ['Vehicle Density']
    values = [vehicle_density]

    ax.clear()
    ax.bar(labels, values, color=['green'])
    ax.set_title('Vehicle Density Visualization')
    ax.set_ylim(0, 1.0)

def visualize_shortest_path(ax, graph, shortest_path):
    for node in graph:
        for neighbor, weight in graph[node].items():
            ax.plot([node, neighbor], [graph[node][neighbor]] * 2, marker='o', color='gray', linestyle='dashed')

    for i in range(len(shortest_path) - 1):
        ax.plot([shortest_path[i], shortest_path[i + 1]], [graph[shortest_path[i]][shortest_path[i + 1]]] * 2,
                marker='o', color='red', linewidth=2)

    ax.set_title('Shortest Path Visualization')

def update_plot(frame):
    traffic_flow, vehicle_density, weather_conditions = collect_traffic_data()
    print_traffic_info(traffic_flow, vehicle_density, weather_conditions)

    visualize_traffic_flow(ax1, traffic_flow, weather_conditions)
    visualize_vehicle_density(ax2, vehicle_density, weather_conditions)

    congestion_level = analyze_traffic(traffic_flow, vehicle_density)
    print(adjust_traffic_signals(congestion_level))

    start_node = random.choice(list(traffic_graph.keys()))
    end_node = random.choice(list(traffic_graph.keys()))

    shortest_path = dijkstra(traffic_graph, start_node, end_node)
    print_shortest_path(start_node, end_node, shortest_path)
    visualize_shortest_path(ax3, traffic_graph, shortest_path)

    print("-" * 40)

if __name__ == "__main__":
    traffic_graph = initialize_traffic_graph()

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

    animation = FuncAnimation(fig, update_plot, interval=TRAFFIC_SIMULATION_INTERVAL * 1000)

    plt.show()
