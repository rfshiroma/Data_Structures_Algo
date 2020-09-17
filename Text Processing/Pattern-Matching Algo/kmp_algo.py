# python3

'''Implementation of the Knuth-Morris-Pratt pattern-matching algo.'''

def find_kmp(text, pattern):
    '''Return te lowest index of Text at which substring Pattern begins (or else -1).'''
    n, m = len(text), len(pattern)              # introduce convenient notations
    if m == 0: return 0                         # important search for empty string
    fail = compute_kmp_fail(pattern)            # rely on utility to precompute
    j = 0                                       # index of text
    k = 0                                       # index of pattern
    while j < n:
        if text[j] == pattern[k]:               # pattern[0:1+k] matched thus far
            if k == m - 1:                      # match is complete
                return j - m + 1
                j += 1                          # try to extend match
                k += 1
        elif k > 0:
            k = fail[k - 1]                     # reuse suffix of pattern[0:k]
        else:
            j += 1
    return -1                                   # reached end without match


# The KMP pattern-matching algo relies on a utility function called compute_kmp_fail. Note how the algorithm uses the previous values of the failure function to efficiently compute new values.
def compute_kmp_fail(pattern):
    '''Utility that computes and returns KMP "fail" list.'''
    m = len(pattern)
    fail = [0] * m                              # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:                                # compute f(j) during this pass, if nonzero
        if pattern[j] == pattern[k]:            # k + 1characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:                             # k follows a matching prefix
            k = fail[k-1]
        else:                                   # no match found starting at j
            j += 1
    return fail
