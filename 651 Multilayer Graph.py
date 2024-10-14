import networkx as nx
import matplotlib.pyplot as plt

def create_multilayer_graph():
    # Layer 1: 5 nodes
    layer1 = nx.Graph()
    layer1_nodes = range(1, 6)
    layer1.add_nodes_from(layer1_nodes)
    layer1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

    # Layer 2: 5 nodes
    layer2 = nx.Graph()
    layer2_nodes = range(6, 11)
    layer2.add_nodes_from(layer2_nodes)
    layer2.add_edges_from([(6, 7), (7, 8), (8, 9), (9, 10)])

    # Layer 3: 4 nodes
    layer3 = nx.Graph()
    layer3_nodes = range(11, 15)
    layer3.add_nodes_from(layer3_nodes)
    layer3.add_edges_from([(11, 12), (12, 13), (13, 14)])

    # Layer 4: 3 nodes
    layer4 = nx.Graph()
    layer4_nodes = range(15, 18)
    layer4.add_nodes_from(layer4_nodes)
    layer4.add_edges_from([(15, 16), (16, 17)])

    # Generate a multilayer graph
    multilayer_graph = nx.Graph()

    # Merge multiple layers into one graph
    multilayer_graph = nx.compose(multilayer_graph, layer1)
    multilayer_graph = nx.compose(multilayer_graph, layer2)
    multilayer_graph = nx.compose(multilayer_graph, layer3)
    multilayer_graph = nx.compose(multilayer_graph, layer4)

    # Adding inter-layer connections
    for node1 in layer1_nodes:
        for node2 in layer2_nodes:
            multilayer_graph.add_edge(node1, node2)

    for node2 in layer2_nodes:
        for node3 in layer3_nodes:
            multilayer_graph.add_edge(node2, node3)

    for node3 in layer3_nodes:
        for node4 in layer4_nodes:
            multilayer_graph.add_edge(node3, node4)

    return multilayer_graph, layer1_nodes, layer2_nodes, layer3_nodes, layer4_nodes


#
multilayer_graph, layer1_nodes, layer2_nodes, layer3_nodes, layer4_nodes = create_multilayer_graph()

# Set color for nodes in each layer
node_colors = []
for node in multilayer_graph.nodes():
    if node in layer1_nodes:
        node_colors.append('yellow')
    elif node in layer2_nodes:
        node_colors.append('pink')
    elif node in layer3_nodes:
        node_colors.append('pink')
    elif node in layer4_nodes:
        node_colors.append('pink')

# Set position for nodes in each layer
pos = {
    1: (0, 1), 2: (0, 2), 3: (0, 3), 4: (0, 4), 5: (0, 5),
    6: (1, 1), 7: (1, 2), 8: (1, 3), 9: (1, 4), 10: (1, 5),
    11: (2, 1.5), 12: (2, 2.5), 13: (2, 3.5), 14: (2, 4.5),
    15: (3, 2), 16: (3, 3), 17: (3, 4),
}

# plot digram
plt.figure(figsize=(10, 8))
nx.draw(multilayer_graph, pos, with_labels=False, node_color=node_colors, edge_color='gray', node_size=500, font_size=10)

plt.title("Multilayer Graph with Different Colors for Each Layer")
plt.show()

