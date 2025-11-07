## Group Anagrams - Design Notes

### Problem Summary
- Found a time consuming issue when compared with other approaches.
- Redundant code

### Chosen Approach
- Reverse String

### Why Reverse String?
- The simplest and understandable approach for beginners.

### Strengths
- low space complexity : $`O(n*k)`$ 

### Limitations
- time consuming, though theoretical value of time complexity is $`O(n*klogk)`$
  This may come from redundant condition and redundant code especially when converting float value to integer.

### Alternatives Considered
- Two Pointers : $`O(n)`$, the efficient way in space complexity ($`O(1)`$)

### Design Philosophy
- Chose the simplest way
