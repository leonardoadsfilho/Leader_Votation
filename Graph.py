import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

import random


def draw_graph_with_values(G):
    pos = nx.spring_layout(G)  # Positions for all nodes

    # Draw nodes
    nx.draw_networkx_nodes(G, pos)

    # Draw edges
    nx.draw_networkx_edges(G, pos)

    # Draw node labels with values
    labels = {node: f"{node} ({G.nodes[node].get('value', 0)})" for node in G.nodes}
    nx.draw_networkx_labels(G, pos, labels)

    plt.axis("off")  # Disable axis
    plt.show()  # Show the graph

    return G

def remove_edges_to_vertex(G, vertex):
    edges_to_remove = []
    for source, target in G.edges():
        if target == vertex:
            edges_to_remove.append((source, target))
    
    neighbor =  random.choice(list(G.neighbors(vertex)))

    G.remove_edges_from(edges_to_remove)
    G.remove_node(vertex)

    return G, neighbor

def update_random_vertex_value(G, leader):
    if G.number_of_nodes() > 0:
        G.nodes[leader]['value'] = -1
        G, neighbor = remove_edges_to_vertex(G, leader)

    return G, neighbor

def find_node_with_max_value(G):
    max_value = float('-inf')
    max_node = None

    for node in G.nodes():
        node_value = G.nodes[node].get('value', 0)
        if node_value > max_value:
            max_value = node_value
            max_node = node

    return max_node

def find_tree_root(tree):
    for node in tree.nodes():
        if tree.degree(node) == 0:
            return node

def bfs_tree(graph, start_node):
    visited = set()
    queue = deque([(start_node, None)])
    tree = nx.Graph()
    root = start_node
    node_values = {}  # Dicionário para armazenar os valores dos nós

    while queue:
        node, parent = queue.popleft()
        if node not in visited:
            visited.add(node)
            if parent is not None:
                tree.add_edge(parent, node)
            node_values[node] = graph.nodes[node].get('value', None)  # Armazena o valor do nó
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, node))

    # Atribui os valores dos nós à árvore resultante
    for node, value in node_values.items():
        tree.nodes[node]['value'] = value

    return tree, root

def draw_tree(tree, root):
    pos = nx.spring_layout(tree)

    # Definir cores e tamanhos dos nós
    node_colors = ['red' if node == root else 'lightblue' for node in tree.nodes()]
    node_sizes = [1000 if node == root else 500 for node in tree.nodes()]

    # Desenhar nós e arestas
    nx.draw_networkx_nodes(tree, pos, node_color=node_colors, node_size=node_sizes)
    nx.draw_networkx_edges(tree, pos)

    # Desenhar rótulos dos nós com seus valores
    labels = {node: f"{node} ({tree.nodes[node].get('value', 0)})" for node in tree.nodes}
    nx.draw_networkx_labels(tree, pos, labels=labels)

    plt.axis("off")  # Desativar eixos
    plt.show()  # Mostrar o desenho da árvore

def find_node_with_max_value_tree(tree):
    max_value = float('-inf')
    max_node = None

    for node in tree.nodes():
        node_value = tree.nodes[node].get('value', 0)
        if node_value > max_value:
            max_value = node_value
            max_node = node

    return max_node, max_value

def draw_graph_with_highlighted_node(G, node):
    pos = nx.spring_layout(G)
    node_colors = ['red' if n == node else 'lightblue' for n in G.nodes()]
    node_sizes = [1000 if n == node else 500 for n in G.nodes()]

    labels = {n: f"{n} ({G.nodes[n].get('value', 0)})" for n in G.nodes()}

    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, node_size=node_sizes, edge_color='gray')
    plt.show()