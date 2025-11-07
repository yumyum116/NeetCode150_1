# Approach    : Sorting
# Result      : runtime -> 0.712 sec, memory -> 52.8 MB
# Strength    : simple and understandable
# Limitation  : time consuming O(m * nlogn), where m is the number of strings and n is the length of the longest string.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
