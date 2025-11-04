# Approach    : Brute-force pairwise comparison approach
# Strength    : simple and no extra memory
# Limitation  : slow for large data resulting in Time Out

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
