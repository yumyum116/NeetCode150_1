## String Matching in an Array - Design Notes

### Problem Summary
- Found a time consuming issue
- too complex and can improve to KMP, Rabin-Karp or Trie

### Chosen Approach
- Brute-Force *not similar to original, but the logic itself is almost same

### Why Brute-Force?
- Intensive and fast enough with small data

### Strengths
- no extra memory structure : $`O(1)`$ for extra space and $`O(n)`$ for the output list
- high flexiblity
- enable to extract strings concisely

### Limitations
- time consuming : $`O(n^2 * m^2)`$

### Alternatives Considered
- Sorting                             :
- Knuth-Morris-Pratt (KMP) Algorithm  : 
- Rabin-Karp Algorithm (Rolling Hash) :
- Z-Algorithm                         :
- Trie                                :
      
### Design Philosophy
- Chose the intensive way

