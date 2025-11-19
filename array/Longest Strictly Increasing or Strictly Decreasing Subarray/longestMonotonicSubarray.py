# Approach    : Linear scan
# Results     : runtime -> 1 ms, memory -> 17.76 MB
# Strength    : fast enough and low memory consumption O(1)
# Limitation  : when input data is small enough, other approaches may result in high efficiency

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = decrease = 1
        result = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increase += 1
                decrease = 1
            elif nums[i] < nums[i-1]:
                decrease += 1
                increase = 1
            else:
                increase = decrease = 1
            result = max(result, increase, decrease)
        return result
