# python3

'''Python implementation of a Graph ADT which supports directed or undirected graphs.'''
# Usage of adjacency map representation

# ---------------- nested Vertex class ----------------
# to be nested within Graph class
class Vertex:
    '''Lightweight vertex structure for a graph.'''
    __slot__ = '_element'

    def __init__(self, x):
        '''Do not call constructor directly. Use Graph's insert_vertex(x).'''
        self._element = x

    def element(self):
        '''Return element associated with this vertex.'''
        pass

    def __hash__(self):
        pass

# ---------------- nested Edge class ----------------
# to be nested within Graph class
class Edge:
    '''Lightweight edge structure for a graph.'''
    __slot__ = 'origin', 'destination', 'element'

    def __init__(self, u, v, x):
        pass

    def endpoints(self):
        pass

    def opposite(self, v):
        pass

    def element(self):
        pass

    def __hash__(self):
        pass

# ---------------- Graph class ----------------
class Graph:
    '''Representation of a simple graph using an adjacency map.'''

    def __init__(self, directed=False):
        pass

    def is_directed(self):
        pass

    def vertex_count(self):
        pass

    def vertices(self):
        pass

    def edge_count(self):
        pass

    def edges(self):
        pass

    def get_edges(self, u, v):
        pass

    def degree(self, v, outgoing=True):
        pass

    def incident_edges(self, v, outgoing=True):
        pass

    def insert_vertex(self, x=None):
        pass

    def insert_edge(self, u, v, x=None):
        pass
