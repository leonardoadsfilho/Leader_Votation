from ReadFile import read_graph_from_file
from Graph import *

filename = 'grafo.txt'
grafo = read_graph_from_file(filename)
leader = find_node_with_max_value(grafo)
draw_graph_with_highlighted_node(grafo, leader)

grafo, neighbor = update_random_vertex_value(grafo, leader)
draw_graph_with_highlighted_node(grafo, neighbor)

tree, root = bfs_tree(grafo, neighbor)
draw_tree(tree, root)

new_leader, value = find_node_with_max_value_tree(tree)
draw_graph_with_highlighted_node(grafo, new_leader)