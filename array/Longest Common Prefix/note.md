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
- when prefix is long, time consuming until fidings of mismatch characters and low efficiency in memory usage

### Alternatives Considered
- Vertical Scanning   : best approach when prefix is long or low memory capacity
- Sorting             : low space complexity $`O(1)`$, but has a time complexity $`O(n * mlogm)`$
- Trie                : another approach with same effiency of horizontal approach, but complex code
    
### Design Philosophy
- Chose the intensive approach
