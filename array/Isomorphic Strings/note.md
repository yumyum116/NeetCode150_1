## Ismorphic Strings - Design Notes

### Problem Summary
- Time and memory consuming
- complex
- may cause bugs

### Approach
<dl>
  <dt> 1. For each string, build a list of groups</dt>
  <dd> Each group contains: </dd>
  <dd> - a charcter </dd>
  <dd> - the list of indices where the character appears </dd>
  <dd> - ex: "egg" -> [['e', 0], ['g', 1, 2]] </dd>
  <dt> 2. Compare the length of each string </dt>
  <dt> 3. If step 2 returns true, then compare each group of pair </dt>
  <dd> For each group index i: </dd>
  <dd> - check whether the lengths of the two groups match </dd>
  <dd> - then check whether all recorded positions match </dd>
  <dt> 4. If all group comparisons match, return true </dt>
</dl>
