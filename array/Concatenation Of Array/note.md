## Concatenation Of Array - Design Notes

### Problem Summary
- Redundant code.

### Chosen Approach
- Two-pass iteration

### Why two-pass iteration?
- Intensive and understandable approach rather than one-pass approach.

### Strengths
- relatively high performance in memory access
- readable 

### Limitations
- relatively slow in runtime when compared with one-pass iteration
- low memory efficiency when compared with one-pass iteration

### Alternatives Considered
- One-pass iteration  : time complexitiy %`O(n)`$, space complexity $`O(n)`$
    
### Design Philosophy
- Chose the understandable way
