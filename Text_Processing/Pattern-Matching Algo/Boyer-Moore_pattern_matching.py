# python3

'''An implementation of the Boyer-Moore algo'''

# The efficiency of the Boyer-Moore algorithm relies on creating a lookup table that quickly determines where a mismatched character occurs elsewhere in the pattern.

# We prefer to use a hash table to represent the last function, with only those characters from the pattern occurring in the structure. The space usage for this approach is proportional to the number of distinct alphabet symbols that occur in the pattern, and thus O(m). The expected lookup time remains independent of the problem (although the worst-case bound is O(m)).

# "Charachter comparions in order to skip alignments which provably will not result in a match or fruitful." - Ben Landmead

def find_boyer_moore(text, pattern):
    '''Return the lowest index of Text at which substring Pattern begins (or else -1).'''
    n, m = len(text), len(pattern)                  # introduce convenient notations
    if m == 0: return 0                             # important search for empty string
    last = {}                                       # build a dict called 'last'
    for k in range(m):
        last[pattern[k]] = k                        # later occurrence overwrites

    # align end of pattern at index m-1 of text
    i = m-1                                         # an index into Text
    k = m-1                                         # an index into Pattern
    while i < n:
        if text[i] == pattern[k]:                   # a matching character
            if k == 0:
                return i                            # pattern begins at index i of Text
            else:
                i -= 1                              # examine previous character
                k -= 1                              # of both Text and Pattern
        else:
            j = last.get(text[i], -1)               # last(text[i]) is -1 if not found
            i += m - min(k, j+1)                    # case analysis for jump step (Fig 13.3 (a) and (b))
            k = m - 1                               # restart at end of pattern
    return -1
