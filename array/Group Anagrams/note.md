## Group Anagrams - Design Notes

### Problem Summary
- Found a time consuming issue when compared with other approaches.

### Chosen Approach
- Sorting

### Why Sorting?
- The simplest and understandable approach for beginners.

### Strengths
- relatively low space complexity : $`O(m*n)`$ 

### Limitations
- time consuming, though theoretical value of time complexity is $`O(m*nlogn)`$

### Alternatives Considered
- Hash Table : $`O(m * n)`$, need more space complexity ($`O(m)`$ for extra space and $`O(m * n)`$ for the output list)

### Design Philosophy
- Chose the simplest way
