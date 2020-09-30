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
        return self._element

    def __hash__(self):         # will allow vertex to be a map key
        return hash(id(self))

# ---------------- nested Edge class ----------------
# to be nested within Graph class
class Edge:
    '''Lightweight edge structure for a graph.'''
    __slot__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        '''Do not call constructor directly. Use Graph's insert_edge(u,v,x).'''
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        '''Return (u,v) tuple for vertices u and v.'''
        return(self._origin, self._destination)

    def opposite(self, v):
        '''Return the vertex that is opposite v on this edge.'''
        return self._destination if v is self.origin else self.origin

    def element(self):
        '''Return element associated with this edge.'''
        return self._element

    def __hash__(self):         # will allow edge to be a map key
        return hash( (self._origin, self._destination) )

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
