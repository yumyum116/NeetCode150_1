## Length of Last Word - Design Notes

### Problem Summary
- When empty string or full-wide space passes, indexerror might happen.

### Chosen Approach
- Iteration (backforce)

### Why iteration (backforce)?
- Simple, intensive, and the fastest way.

### Strengths
- Intensive and understandable
- If interested in last word only, the performance of this approach is the best

### Limitations
- IndexError might occur, when empty string or full-width space passes.

### Alternatives Considered
- Iteration (forward)    : efficient both in time complexitiy %`O(n)`$ and space complexity $`O(1)`$
- Built-In function      : Simplest, but has a space complexity $`O(n)`$
    
### Design Philosophy
- Chose the intensive approach
