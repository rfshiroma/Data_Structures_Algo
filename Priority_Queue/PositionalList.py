# python3

'''Doubly Linked List Implementation'''
# The Positional List Abstract Data Type
# Each method of the postional list ADT runs in worst-case O(1) time when implemented with a doubly linked list.

class PositionalList(_DoublyLinkedBase):
    '''A sequential container of elements allowing positional access.'''

    # ---------------- nested Position class ----------------
    class Position:
        '''An abstract representing the location of a single element.'''

        def __init__(self, container, node):
            pass

        def element(self):
            pass

        def __eq__(self, other):
            pass

        def __ne__(self, other):
            pass

    # ---------------- utility method ----------------
    def _validate(self, p):
        pass

    def _make_position(self, node):
        pass

    # ---------------- accessors ----------------
    def first(self):
        pass

    def last(self):
        pass

    def before(self, p):
        pass

    def after(self, p):
        pass

    def __iter__(self):
        pass

    # ---------------- mutators ----------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        pass

    def add_first(self, e):
        pass

    def add_last(self, e):
        pass

    def add_before(self, p, e):
        pass

    def add_after(self, p, e):
        pass

    def delete(self, p):
        pass

    def replace(self, p, e):
        pass
