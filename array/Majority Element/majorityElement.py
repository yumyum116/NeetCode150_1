# Approach    : Built-in Approach
# Results     : runtime -> 5 ms, memory -> 19.38 MB
# Strength    : relatively faster and efficient more han other approaches
# Limitation  : no room for optimazation

import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = collections.Counter(nums)
        map = map.most_common()
        if map[0][1] > len(nums) / 2:
            return map[0][0]
