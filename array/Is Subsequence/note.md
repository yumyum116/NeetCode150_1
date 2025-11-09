## Is Subsequence - Design Notes

### Problem Summary
- Found a time consuming issue when compared with other approaches.

### Chosen Approach
- Two-pointers

### Why Two-pointers?
- Simplest and fast enough with the most size of data

### Strengths
- fast enough in terms of runtime and no extra memory $`O(1)`$

### Limitations
- in case of static 't' with variant 's', this approach could be insufficient

### Alternatives Considered
- Brute-Force                           : intensive and easy to deploy, and fast enough with small size of input, but inefficient with very long string
- Recursion                             : with time complexitiy %`O(n*m)`$ and space complexity $`O(n)`$, readable and understandable
- Dynamic Programming  (Top-Down)       : intensive expression of recursive and efficient approach, though complicated coding and too heavy for isSubsequence
- Dynamic Programming  (Bottom-Up)      : scalability, but space complexity is vague $`O(n*m)`$, thus not suit for extreme long strings
- Follow-Up Solution   (Index Jumping)  : relatively fast in time complexity $`O(n+m)`$ and space complexity is $`O(m)`$
    
### Design Philosophy
- Chose the simplest approach
