import networkx as nx
from collections import deque
from task1 import create_graph


def dfs_iterative(graph, start, goal):
    """
    Depth-First Search (DFS) implementation using a Stack (LIFO)
    """
    visited = set()
    # (current_node, path_so_far)
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()

        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)

            neighbors = list(graph.neighbors(vertex))
            # reverse neighbors before pushing to stack
            for neighbor in sorted(neighbors, reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None


def bfs_iterative(graph, start, goal):
    """
    Breadth-First Search (BFS) implementation using a Queue (FIFO)
    """
    visited = {start}
    # (current_node, path_so_far)
    queue = deque([(start, [start])])

    while queue:
        (vertex, path) = queue.popleft()

        for neighbor in graph.neighbors(vertex):
            if neighbor == goal:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


if __name__ == "__main__":
    G = create_graph()
    start_node = 'G'
    target_node = 'D'

    print(f"Comparing agorithms: Path from {start_node} to {target_node}")
    bfs_path = bfs_iterative(G, start_node, target_node)
    print(f"BFS path: {bfs_path}")
    print(f"Length: {len(bfs_path) - 1} edges")

    dfs_path = dfs_iterative(G, start_node, target_node)
    print(f"DFS path: {dfs_path}")
    print(f"Length: {len(dfs_path) - 1} edges")

    nx_shortest = nx.shortest_path(G, source=start_node, target=target_node)
    print(f"NetworkX shortest path: {nx_shortest}")
