## Remove Element - Design Notes

### Problem Summary
- Writing operation is not optimized

### Chosen Approach
- Two Pointers (Forward overwrite)

### Why Two pointers ?
- Preserves the order of elements which leads to being stable and no extra memory required.

### Strengths
- Stable
- low extra memory, only $`O(1)`$ memory needs

### Limitations
- Writing operation in not optimized
- Concept is complex for beginners

### Alternatives Considered
- Brute Force                   : simple and intensive, but extra memory $`O(n)`$ is required
- Two Pointers (swap with last) : efficient if occurence of val is rare, but may perform more swaps when val appears frequently 
    
### Design Philosophy
- Stable and no extra memory required
