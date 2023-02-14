import matplotlib.pyplot as plt
import networkx as nx
import random
import time

def shortest_path(start, end, F, G):

    """
    This function demonstrates results from our algorithm and from networkx library using the same approach
    :param start: start node
    :param end: end node
    :param F: list of the shortest path to each point from start node, param end - index for end's element
    :param G: object of networkx that represents graph
    """
    # Calculation the shortest path from start node to end node using networkx
    pred, dist = nx.bellman_ford_predecessor_and_distance(G, start, end)
    print(dist[end], ' - the shortest path of networkx')

    print(F[end], " - the shortest path of manually-implemented algorithm ")

def create_edges(n):

    """
    :param n: amount of nodes
    :return edges: dict of edges where the keys are nodes that represent weight from one node to another.
    It is the same as a matrix
    """
    edges = {}

    for i in range(n):
        for j in range(n):

            # Initialization weight with 0 if nodes are equally
            if i == j:
                edges[i, j] = 0
                continue

            # repeat weight
            if i > 0 and i > j:
                repeated_edge = edges[j, i]
                edges[i, j] = repeated_edge
                continue

            # Initialize random weight
            edges[i, j] = random.random()

    return edges

def convert_edges_to_networkx(edges):

    """
    :param edges: dict of edges that was described earlier
    :return new_edges: tuple object that contains two nodes and the weight of edge between them
    """

    new_edges = []

    for j, i in edges.keys():

        weight = edges[j,i]
        new_edges.append((j, i, weight))

    return new_edges

n = 150 # Initialization the number of nodes
edges = create_edges(n) # Creation of edges

G = nx.complete_graph(n)  # Creation object of networkx - graph
converted_edges = convert_edges_to_networkx(edges) # Convert edges for networkx
G.add_weighted_edges_from(converted_edges) # Adding edges to graph

start = random.randrange(n) # Random initialization start node which from it will calculate the shortest path to each point
end = random.randrange(n) # Initializing node which we want to find short path from start
INF = 10 ** 9
F = [INF] * n # Creation the function - list that contains path from start node to the rest nodes
F[start] = 0 # Initialization edge from between start and start nodes)

def calculation_paths(n , F, edges):
    start_time = time.time()

    for k in range(1, n): # Iteration through all of edges
        for j, i in edges.keys(): # Iteration through all of weights
            if F[j] + edges[j, i] < F[i]:
                F[i] = F[j] + edges[j, i]

    print("--- %s seconds with optimization ---" % (time.time() - start_time))


print('Random start node = ', start, 'Random end node = ', end)
calculation_paths(n=n, F=F, edges=edges)
shortest_path(start=start, end=end, F=F, G=G) # Validate on mistakes

#nx.draw(G, with_labels=True, font_weight='bold') - it can draw the graph if it is necessary
#plt.show()