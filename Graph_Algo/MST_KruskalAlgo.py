# python3

# for managin the cluster partition
from Partition import Partition
from HeapPriorityQueue import HeapPriorityQueue

'''Implementation of Kruskal's algorithm for the minimum spanning tree (MST) problem'''

def MST_Kruskal(g):
    '''Compute a minimum spanning tree (MST) of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.

    The elements of the graph's edges are assumed to be weights.
    '''
    tree = []                               # list of edges in spanning tree
    pq = HeapPriorityQueue()                # entries are edges in G, with weights as key
    forest = Partition()                    # keeps track of forest clusters
    position = {}                           # map each node to its Partition entry

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)              # edge's element is assumed to be its weight

    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u,v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a,b)

    return tree
