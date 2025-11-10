## Longest Common Prefix - Design Notes

### Problem Summary
- Extra memory is used due to redundant code.

### Chosen Approach
- Horizontal Scanning

### Why Horizontal Scanning?
- The intensive and understandable approach for beginners.

### Strengths
- Fast enough $`O(n*m)`$ and no extra memory $`O(1)`$ 

### Limitations
- 

### Alternatives Considered
- Vertical Scanning   : another approach with same effiency of horizontal approach, but shorter code rather than horizontal one
- Sorting             : low space complexity $`O(1)`$, but has a time complexity $`O(n * mlogm)`$
- Trie                : another approach with same effiency of horizontal approach, but complex code
    
### Design Philosophy
- Chose the intensive approach
