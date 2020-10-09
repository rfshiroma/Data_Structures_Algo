# python3
'''Implementation of priority queue with a Sorted List'''

# Inheriting from from the PriorityQueueBase class
from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList


# base class defines _Item
class SortedPriorityQueue(PriorityQueueBase):
    '''A min-oriented priority queue implemented with a sorted list.'''


    def __init__(self):
        '''Create a new empty Priority Queue.'''
        self._data = PositionalList()
