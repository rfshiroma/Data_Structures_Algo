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
            '''Constructor should not be invoked by user.'''
            self._container = container
            self._node = node

        def element(self):
            '''Return the element stored at this Position.'''
            return self._node._element

        def __eq__(self, other):
            '''Return True if other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            '''Return True if other does not represent the same location.'''
            return not (self == other)          # opposite of __eq__

    # ---------------- utility method ----------------
    def _validate(self, p):
        pass

    def _make_position(self, node):
        '''Return Position instance for given node (or None if sentinel).'''
        if node is self._header or node is self._trailer:
            return None                                 # boundary violation
        else:
            return self.Position(self, node)            # legitimate position

    # ---------------- accessor methods ----------------
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
        '''Add element between existing nodes and return new Position.'''
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        '''Insert element e at the front of the list and return new Position.'''
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''Insert element e at the back of the list and return new Position.'''
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        '''Insert element e into list before Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        '''Insert element e into list after Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        '''Remove and return the element at Position p.'''
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        '''Replace the element at Position p with e.

        Return the element formely at Position p.
        '''
        original = self._validate(p)
        old_value = original._element           # temporarily store old element
        original._element = e                   # replace with new element
        return old_value                        # return the old element value
