# python3

'''
TreeMap class that implements of the sorted map ADT using a binary search tree.

Takes advantage of multiple inheritance for code reuse.

Brief guid to the organization of proposed code:
  1. Beginning of TreeMap class including redefined Position class and nonpublic search utilities;
  2. Positional methods first(), last(), before(p), after(p), and find_position(p) accessor;
  3. Selected methods of the sorted map ADT: find_min(), find_ge(k), and find_range(start, stop); related methods are omitted for the sake of brevity;
  4. __getitem__(k), __setitem__(k,v), and __iter__();
  5. Deletion either by position, as delete(p), or by key, as __delitem__(k).
'''

class TreeMap(LinkedBinaryTree, MapBase):
    '''Sorted map implementation using a binary search tree.'''

    # ---------------- override Position class ----------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            '''Return key of map's key-value pair.'''
            return self.element()._key

        def value(self):
            '''Return value of map's key-value pair.'''
            return self.element()._value

    # ---------------- nonpublic utilities ----------------
    def _subtree_search(self, p, k):
        '''Return Position of p's subtree having key k, or last node searched.'''
        if k == p.key():                            # found match
            return p
        elif k < p.key():                           # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:                                       # serach right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                    # unsuccessful search

    def _subtree_first_position(self, p):
        '''Return Position of first item in subtree rooted at p.'''
        walk = p
        while self.left(walk) is not None:          # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        '''Return Position of last item in subtree rooted at p.'''
        walk = p
