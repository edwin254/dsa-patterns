""" undireted-path quiz
 wite a function that takes an array of edges for a undirected 
"""

edges = [
    ['A', 'J'],
    ['A', 'K'],
    ['B', 'J'],
    ['B', 'K'],
    ['C', 'J'],
    ['C', 'K'],
]

# using DFS

def undirected_path_quiz(edges, start_node, end_node):
        # build an adjacency list
    def build_graph(edges):
        adj_list = {}

        for node_1, node_2 in edges:
            if node_1 not in adj_list:
                adj_list[node_1] = []
            adj_list[node_1].append(node_2)

            if node_2 not in adj_list:
                adj_list[node_2] = []
            adj_list[node_2].append(node_1)

        # print(adj_list)

        return adj_list

    def find_path(graph, start_node, end_node):
        print(visited_nodes, start_node)
        node_stack = [start_node]
        if start_node == end_node:
            print("DONE")
            return True
        
        last_visited = node_stack.pop()
        visited_nodes.add(last_visited)
        current_node_children = graph[start_node]
        node_stack.extend(current_node_children)
        print("=====================")
        print(visited_nodes, start_node, node_stack)

        for node in current_node_children:
            if node in visited_nodes:
                continue

            if(find_path(graph,current_node_children[-1], end_node )):
                return True
        return False


    visited_nodes = set()
    graph = build_graph(edges)
    return find_path(graph, start_node, end_node)


print(undirected_path_quiz(edges, 'A', 'K'))