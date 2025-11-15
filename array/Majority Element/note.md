## Majority Element - Design Notes

### Problem Summary
- no room for optimazation

### Chosen Approach
- Built-In Approach

### Why built-in approach?
- At the first trial with hash map, time exceeded and chose the faster way.

### Strengths
- Fast enough $`O(n)`$ 

### Limitations
- no room for improvement or customization

### Alternatives Considered
- Sorting                 : no extra memory $`O(1)`$, but time consuming $`O(nlogn)`$
- Hash Map                : faster than sorting, but time and memory consuming with large data
- Bit Manipulation        : faster and efficient with large data
- Moore Voting Algorithm  : more efficient compared to sorting as it requires only a single pass through the array and does not change the original order of the elements
- Randomization           : faster, but may cause runtime issue
    
### Design Philosophy
- Chose the faster approach to overcome runtime issue
