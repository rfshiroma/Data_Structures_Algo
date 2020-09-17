# PATTERN-MATCHING ALGORITHMS

## The Boyer-Moore Algo
The main idea of the Boyer-Moore algorithm is to improve the running time of the brute-force algorithm by adding two potentially time-saving heuristics. Roughly stated, these heuristics are as follows:
  - Looking-Glass Heuristic
  - Character-Jump Heuristic

The efficiency of the Boyer-Moore algorithm relies on creat- ing a lookup table that quickly determines where a mismatched character occurs elsewhere in the pattern.

## The Knuth-Morris-Pratt Algo
The KMP Algo performs pattern matching on a text string of length n and a pattern string of length m in O(n + m) time. 
