## Contains Duplicate - Design Notes

### Problem Summary
Found a timeout issue with large test cases.

### Chosen Approach
- Brute-Force

### Why Brute-Force?
- The simplest and understandable approach for beginners.

### Strengths
- simple implementation
- low extra memory : $`O(1)`$

### Limitations
- time consuming : $`O(n^2)`$
- low efficiency in memory access

### Alternatives Considered
- Sorting : $`O(n log n)`$
- Hash Set : $`O(n)`$, the most efficient way both in time complexity and memory access
- Hash Map : $`O(n)`$, the most efficient way in time complexity, though consumes more memory than a Hash Set

### Design Philosophy
- Chose the simplest way
