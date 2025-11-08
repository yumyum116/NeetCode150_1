# Approach    : Iteration (Two Pass)
# Results     : runtime -> 0.787 sec, memory -> 52.2 MB
# Strength    : time complexity O(n) and no extra memory O(n)
# Limitation  : -

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            ans.append(nums[i])
        for i in range(n, 2*n):
            ans.append(nums[i-n])
        return ans
