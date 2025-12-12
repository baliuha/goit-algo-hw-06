import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    G = nx.complete_graph(5)
    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    G = nx.relabel_nodes(G, mapping)
    G.add_edges_from([('A', 'F'), ('F', 'G')])

    return G


def create_weighted_graph():
    DG = nx.complete_graph(5, create_using=nx.DiGraph)

    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    DG = nx.relabel_nodes(DG, mapping)
    DG.add_edge('G', 'F', weight=2, label=2)
    DG.add_edge('F', 'A', weight=2, label=2)

    for u, v in DG.edges():
        if u in ['G', 'F']:
            continue
        # default weight
        DG[u][v]['weight'] = 5
        DG[u][v]['label'] = 5

    # adjustments
    DG['A']['D']['weight'] = 20
    DG['A']['D']['label'] = 20

    DG['A']['B']['weight'] = 2
    DG['A']['B']['label'] = 2

    DG['B']['D']['weight'] = 2
    DG['B']['D']['label'] = 2

    return DG


def draw_graph(G):
    plt.figure(figsize=(6, 6))
    pos = nx.circular_layout(G)
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="#CF0722", node_size=2500,
        font_color='white', font_size=18, font_weight='bold',
        edge_color='gray', width=1.5
    )

    plt.title("Complete Graph")
    plt.show()


def draw_weighted_graph(DG):
    plt.figure(figsize=(6, 6))

    pos = nx.circular_layout(DG)
    nx.draw(
        DG, pos,
        with_labels=True,
        node_color="#0EB157", node_size=2500,
        font_color='white', font_size=18, font_weight='bold',
        edge_color='gray', width=1.5
    )

    edge_labels = nx.get_edge_attributes(DG, 'label')
    nx.draw_networkx_edge_labels(
        DG, pos,
        edge_labels=edge_labels,
        label_pos=0.3,
        font_color='red'
    )

    plt.title("Weighted Graph")
    plt.show()


def print_statistics(G):
    print("="*20)
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Graph Density: {nx.density(G)}")
    print(f"Is graph connected? {nx.is_connected(G)}")

    print("="*20)
    for node, degree in G.degree():
        print(f"Node {node} has degree: {degree}")

    print("="*20)
    print(f"Degree Centrality: {nx.degree_centrality(G)}")
    print(f"Closeness Centrality: {nx.closeness_centrality(G)}")
    print(f"Betweenness Centrality: {nx.betweenness_centrality(G)}")


if __name__ == "__main__":
    my_graph = create_graph()
    print_statistics(my_graph)
    draw_graph(my_graph)
