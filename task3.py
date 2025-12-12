from task1 import create_weighted_graph, draw_weighted_graph


def print_table(distances, visited, previous_nodes):
    print("-" * 50)
    print("{:<10} {:<15} {:<10} {:<15}".format("Node", "Distance", "Visited", "Previous"))
    print("-" * 50)

    for vertex in sorted(distances.keys()):
        dist_val = distances[vertex]
        dist_str = "∞" if dist_val == float('infinity') else str(dist_val)

        visited_str = "Yes" if vertex in visited else "No"
        prev_node = previous_nodes[vertex]
        prev_str = str(prev_node) if prev_node is not None else "-"

        print("{:<10} {:<15} {:<10} {:<15}".format(vertex, dist_str, visited_str, prev_str))
    print("-" * 50 + "\n")


def dijkstra_algorithm(graph, start, target):
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0

    # dictionary for the path: {node: parent_node}
    previous_nodes = {vertex: None for vertex in graph.nodes()}    
    unvisited = list(graph.nodes())
    visited = []

    step = 1
    while unvisited:
        # select unvisited node with smallest distance
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # if target is visited, we can stop
        if current_vertex == target:
            visited.append(current_vertex)
            print(f"Step {step}: Reached Target '{target}'")
            print_table(distances, visited, previous_nodes)
            break

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            new_distance = distances[current_vertex] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # record where we came from
                previous_nodes[neighbor] = current_vertex

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        print(f"Step {step}: Visiting '{current_vertex}'")
        print_table(distances, visited, previous_nodes)
        step += 1

    path = []
    current = target

    # if route was not found
    if distances[target] == float('infinity'):
        return [], float('infinity')

    # backtracking, get the route
    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    # reverse the list to get nodes in correct order
    path = path[::-1]

    return path, distances[target]


if __name__ == "__main__":
    my_graph = create_weighted_graph()
    start_node = 'G'
    target_node = 'D'

    print(f"Finding shortest path from {start_node} to {target_node}")
    shortest_path, total_cost = dijkstra_algorithm(my_graph, start_node, target_node)
    print("FINAL RESULT")
    print(f"Path: {shortest_path}")
    print(f"Cost: {total_cost}")

    draw_weighted_graph(my_graph)
