import copy

import matplotlib.pyplot as plt
import networkx as nx
import random
import time

def create_edges(n):

    """
    :param n: amount of nodes
    :return edges - python list: matrix indexes of which represent edges between 2 nodes
    """
    edges = []

    for i in range(n):
        row_edges = [] # Creation list which represents the row in edges
        for j in range(n):

            # Initialization weight with 0 if nodes are equally
            if i == j:
                row_edges.append(0)
                continue

            # repeat weight
            if i > 0 and i > j:
                repeated_edge = edges[j][i]
                row_edges.append(repeated_edge)
                continue

            # Initialize random weight
            row_edges.append(random.random())

        edges.append(row_edges)

    return edges

def convert_edges_to_networkx(edges):

    """
    :param edges: python list of edges that was described earlier
    :return new_edges: tuple object that contains two nodes and the weight of edge between them
    """

    new_edges = []
    n = len(edges)


    for i in range(n):
        for j in range(n):

            weight = edges[j][i]
            new_edges.append((j, i, weight))

    return new_edges

def shortest_path(start, end, F, G):

    """
    This function demonstrates results from our algorithm and from networkx library using the same approach
    :param start: start node
    :param end: end node
    :param F: list of the shortest path to each point from start node, param end - index for end's element
    :param G: object of networkx that represents graph
    """

    short_path = INF
    n = len(F)
    # Calculation the shortest path from start node to end node using networkx
    pred, dist = nx.bellman_ford_predecessor_and_distance(G, start, end)
    print(dist[end], ' - the shortest path of networkx')

    for i in range(1, n):

        if F[i][end] < short_path:
            short_path = F[i][end]

    print(short_path, " - the shortest path of manually-implemented algorithm ")

n = 150 # Initialization the number of nodes

edges = create_edges(n) # Creation of edges
start = random.randrange(n) # Random initialization start node which from we will calculate the shortest path to each point
INF = 10 ** 9

# Creation the function - list that contains weights from start node to the rest of them for different edge
F = [[INF] * n for i in range(n)]
F[0][start] = 0 # Initialization edge from between start and start nodes)

def calculation_paths(n , F, edges):

    """
    :param n: amount of nodes
    :param F: list of the shortest paths from start node to the rest for each edge
    :param edges: weights of edges
    """
    start_time = time.time()

    for k in range(1, n): # Iteration through edges
        for i in range(n): # Iteration through weights for certain edge
             F[k][i] = F[k - 1][i] # Fixating the best short path
             for j in range(n): # Iteration that is needed to extract paths from F and weights from edges

                 if F[k - 1][j] + edges[j][i] < F[k][i]: # Comparison between best short path and offered path
                     F[k][i] = F[k - 1][j] + edges[j][i] # Replacement the best short path

    print("--- %s seconds for edges represented as a list ---" % (time.time() - start_time))

calculation_paths(n=n, F=F, edges=edges)
G = nx.complete_graph(n) # Initializing graph using networkx

converted_edges = convert_edges_to_networkx(edges) # convert edges for graph
G.add_weighted_edges_from(converted_edges) # Adding edges

end = random.randrange(n) # Initializing node which we want to find short path from start to
print('Random start node = ', start, 'Random end node = ', end)
shortest_path(start=start, end=end, F=F, G=G) # Checking results

#nx.draw(G, with_labels=True, font_weight='bold') - it can draw the graph if it is necessary
#plt.show()
