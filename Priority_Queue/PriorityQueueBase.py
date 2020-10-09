# python3

'''Implementation of a Priority Queue'''


# How to implement a priority queue by storing its entries in a positional list L. (see Section 7.4.) We provide two realizations, depending on whether or not we keep the entries in L sorted by key.

class PriorityQueueBase:
    ''' Abstract base class for a priority queue.'''

    class _Item:
        ''' Lightweight composite to store priority queue items.'''
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key       # compare items based on their keys

    # concrete method assuming abstract len
    def is_empty(self):
        ''' Return True if the priority queue is empty.'''
        return len(self) == 0
