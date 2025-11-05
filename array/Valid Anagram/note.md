## Contains Duplicate - Design Notes

### Problem Summary
- Found a time consuming issue comparing with other approaches.
- Redundant code

### Chosen Approach
- Sorting

### Why Sorting?
- The simplest and understandable approach for beginners.

### Strengths
- low extra memory : $`O(1)`$ *depends on the environments

### Limitations
- time consuming : $`O(nlogn + mlogm)`$
- may cause space complexity : O(n + m)

### Alternatives Considered
- Hash Map : $`O(n + m)`$, one of the efficient ways both in time complexity and space complexity ($`O(1)`$)
- Hash Table : $`O(n + m)`$, one of the efficient ways both in time complexity and space complexity ($`O(1)`$)
### Design Philosophy
- Chose the simplest way
