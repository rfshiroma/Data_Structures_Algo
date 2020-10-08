# python3
from graph_ADT import vertices, degree, incident_edges, opposite

'''Implementation for the topological sorting algorithm.'''

def topological_sort(g):
    '''Return a list of vertices of directed acyclic graph g (DAG) in topological order.

    If graph g has a cycle, the result will be incomplete.
    '''
    topo = []           # a list of vertices placed in topological order
    ready = []          # list of vertices that have no remaining constraints
    incount = []        # keep track of in-degree for each vertex
    for u in g.vertices():
        incount[u] = g.degree(u, False)     # paramenter requests incoming degree
        if incount[u] == 0:                 # if u has no incoming edges, it is free of constraints
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()             # u is free of constraints
        topo.append(u)              # add u to the topological order
        for e in g.incident_edges(u):  # consider all outgoing neighbours of u
            v = e.opposite(u)
            incount[v] -= 1             # v has one less constraint without u
            if incount[v] == 0:
                ready.append(v)
    return topo
