# python3
from graph_ADT import incident_edges
from graph_ADT import opposite

'''Python implementation of Breadth-First Search (BFS) on a graph, starting at source vertex s.'''

# A BFS proceeds in rounds and subdivides the vertices into LEVELS. The BFS algorithm is similar to sending out, in all directions, many explores who collectively traverse a graph in coordinated manner.
def BFS(g, u, discovered):
    '''Perform BFS of the undiscovered portion of Graph g starting at source Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    '''
    level = [s]             # first level includes only s
    while len(level) > 0:
        next_level = []     # prepare to gather newly found vertices
        for u in level:
            for e in g.incident_edges(u):       # for eevery outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:     # v is an unvisited vertex
                    discovered[v] = e       # e i the tree edge that discovered v
                    next_level.append(v)    # v will be futher considered in next pass
    level = next_level                      # relabel 'next' level to become current
