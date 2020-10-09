# python3
'''Implementation of priority queue with an Unsorted List'''

# Inheriting from from the PriorityQueueBase class
from PriorityQueueBase import PriorityQueueBase



# base class defines _Item
class UnsortedPriorityQueue(PriorityQueueBase):
    '''A min-oriented priority queue implemented with an unsorted list.'''


    def _find_min(self):  # nonpublic utility
        '''Returns Position of item with minimum key.'''
        if self.is_empty():        # is_empty inherited from base case
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        '''Create a new empty Priority Queue.'''
        self._data = PositionalList()

    def __len__(self):
        '''Return the # of items in the priority queue.'''
        return len(self._data)

    def add(self):
        '''Add a key-value pair.'''
        self._data.add_last(self._Item(key, value))

    def min(self):
        '''Return but do not remove (k,v) tuple with minimum key.'''
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        '''Remove and return (k,v) tuple with minimum key.'''
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
