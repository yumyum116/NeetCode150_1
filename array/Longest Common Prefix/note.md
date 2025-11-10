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
- when prefix is long, time consuming and low efficiency in memory usage

### Alternatives Considered
- Vertical Scanning   : best approach when prefix is long or low memory capacity
- Sorting             : simple and fast enough, $`O(n * mlogm)`$, with small data and low space complexity $`O(1)`$ 
- Trie                : another approach with same effiency of horizontal approach, but complex code
    
### Design Philosophy
- Chose the intensive approach
