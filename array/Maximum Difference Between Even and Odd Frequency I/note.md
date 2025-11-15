## Maximum Difference Between Even and Odd Frequency I - Design Notes

### Problem Summary
- Found a time and memory consuming issue with large data.

### Chosen Approach
- Brute-Force

### Why Brute-Force?
- Easy to debug and fast enough with small data set.

### Strengths
- Fast enough $`O(n + k^2)`$, where k is the length of odd/even number list 

### Limitations
- time and memory consuming with large data and low performance due to double iteration

### Alternatives Considered
- Optimized    : fastest approach with time complexity of $`O(n)`$ and space complexity of $`O(1)`$
    
### Design Philosophy
- Chose a simple approach
