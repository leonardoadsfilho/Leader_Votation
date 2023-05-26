import networkx as nx

def read_graph_from_file(filename):
    G = nx.Graph()

    with open(filename, 'r') as file:
        # Read the number of vertices
        num_vertices = int(file.readline().strip())

        # Read the number of edges
        num_edges = int(file.readline().strip())

        # Add vertices to the graph
        for _ in range(num_vertices):
            line = file.readline().strip()
            vertex, value = map(int, line.split())
            G.add_node(vertex, value=value)

        # Add edges to the graph
        for _ in range(num_edges):
            line = file.readline().strip()
            source, target = map(int, line.split()[:2])  # Consider only the first two elements
            G.add_edge(source, target)

    return G