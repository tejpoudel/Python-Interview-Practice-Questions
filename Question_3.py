"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum
spanning tree connects all vertices in a graph with the smallest possible total
weight of edges. Your function should take in and return an adjacency list
structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
"""
# A utility function to find set of an element i
# (uses path compression technique)
import collections

# Union-Find

parent = dict()
rank = dict()

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def question3(graph):
    for vertex in graph.keys():
        make_set(vertex)

    minimum_spanning_tree = set()

    edges = get_edges(graph)
    edges.sort()
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            minimum_spanning_tree.add(edge)

    adj = collections.defaultdict(list)
    for weight, vertex1, vertex2 in minimum_spanning_tree:
        adj[vertex1].append((vertex2, weight))
        adj[vertex2].append((vertex1, weight))
    return adj


# Utility function to convert adjacency lists to edge list (dictionary input)
def get_edges(adj):
    edge_list = []
    for vertex, edges in adj.iteritems():
        for edge in edges:
            if vertex < edge[0]:
                edge_list.append((edge[1], vertex, edge[0]))
    return edge_list

graph1 = {
    'A': [('B', 1), ('C', 5), ('D', 3)],
    'B': [('A', 1), ('C', 4), ('D', 2)],
    'C': [('B', 4), ('D', 1)],
    'D': [('A', 3), ('B', 2), ('C', 1)],
}
minimum_spanning_tree1 = {
    'A': [('B', 1)],
    'B': [('A', 1), ('D', 2)],
    'C': [('D', 1)],
    'D': [('C', 1), ('B', 2)]
}

graph2 = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 4)],
    'C': [('A', 5), ('B', 4)]
}

minimum_spanning_tree2 = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 4)],
    'C': [('B', 4)]
}


graph3 = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 2)],
    'C': [('A', 3), ('B', 4), ('D', 3), ('E', 2), ('F', 6), ('G', 3)],
    'D': [('B', 2), ('C', 3), ('E', 1)],
    'E': [('C', 2), ('D', 1), ('G', 2)],
    'F': [('C', 6), ('G', 4)],
    'G': [('C', 3), ('E', 2), ('F', 4)]
}


minimum_spanning_tree3 = {
    'A': [('B', 2)],
    'B': [('A', 2), ('D', 2)],
    'C': [('E', 2)],
    'D': [('E', 1), ('B', 2)],
    'E': [('D', 1), ('C', 2), ('G', 2)],
    'F': [('G', 4)],
    'G': [('E', 2), ('F', 4)]
}

assert question3(graph1) == minimum_spanning_tree1
assert question3(graph2) == minimum_spanning_tree2
assert question3(graph3) == minimum_spanning_tree3

# If tests passed
print('Tests passed for question 3')