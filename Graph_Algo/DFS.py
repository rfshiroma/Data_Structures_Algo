# python3

from graph_ADT import incident_edges
from graph_ADT import opposite

'''Python implementation of a basic Depth-First Search (DFS) algorithm.'''

def DFS(g, u, discovered):
    '''Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    discovered: is a dictionary mapping each vertex to the edge that was used to discover it during the DFS. (u should be "discovered" prior to tha call.)
    Newly discovered vertices will be added to the dictionary as a result.
    '''
    for e in g.incident_edges(u):       # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:         # v is an unvisited vertex
            discovered[v] = e           # e is the tree edge that discovered v
            DFS(g, v, discovered)       # recursively explore from v

# In order to track which vertices have been visited, and to build a representation othe resulting DFS tree, this implementation introduces a thrid parameter, named discovery (which will be assigned with result variable):
result = {u: None}      # a new distionary, with u trivially discovered
DFS(g, u, result)

# A basic DFS function can be used as a tool to identify the (directed) path leading from vertex u to v, if v is reachable from u.
def construct_path(u, v, discovered):
    '''Returns an ordered list of vertices on the path from u to v.'''
    path = []                           # empty path by default
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]        # find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()  # list method: redirect path from u to v
    return path

# When a graph is not connected, we need to identify all of the connected components of an UNDIRECTED graph (DFS forest because the graph may not be connected), or the strongly connected components of a DIRECTED graph (more complicated since it uses two separate DFS search traversals, but the details are beyond the scope of the below code).
def DFS_complete(g):
    '''Perform DFS for entire graph and return forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    '''
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            DFS(g, u, forest)           # u will be the root of a tree
    return forest
