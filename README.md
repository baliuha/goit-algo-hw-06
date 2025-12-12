# Analysis of BFS and DFS algorithms

For this assignment, we analyzed a graph consisting of a graph with nodes A-E.
The objective was to find and compare paths from node **G** to node **D**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/163070b3-f36d-4bd6-8e60-6a1965ab40a0"
       width="350">
</p>

## Results

| Algorithm | Path Found | Path Length (Edges) |
|-----------|------------|---------------------|
| **BFS** (Breadth-First Search) | `['G', 'F', 'A', 'D']` | 3 |
| **DFS** (Depth-First Search) | `['G', 'F', 'A', 'B', 'C', 'D']` | 5 |


### 1. BFS (Breadth-First Search)
The algorithm operates using a queue (**FIFO** - First In, First Out). It explores the graph layer by layer: first checking the immediate neighbors (Level 1), then the neighbors of those neighbors (Level 2), and so on.
BFS is guaranteed to find the **shortest path** in an unweighted graph.

### 2. DFS (Depth-First Search)
The algorithm operates using a stack (**LIFO** - Last In, First Out). It attempts to traverse as deep as possible along a single branch before backtracking.
DFS **does not guarantee** the shortest path. It finds the **first valid path** available based on the traversal order, which often results in longer routes in dense graphs.
