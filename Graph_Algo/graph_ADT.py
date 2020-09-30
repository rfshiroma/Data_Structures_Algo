# python3

'''Python implementation of a Graph ADT which supports directed or undirected graphs.'''
# Usage of adjacency map representation

# ---------------- nested Vertex class ----------------
class Vertex:
    '''Lightweight vertex structure for a graph.'''
    __slot__ = '_element'

    def __init__(self, x):
        '''Do not call constructor directly. Use Graph's insert_vertex(x).'''
        self._element = x

    def element(self):
        '''Return element associated with this vertex.'''
