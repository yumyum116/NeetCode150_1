# Approach    : Two Pointers
# Results     : runtime -> 0 ms, memory -> 17.72 MB
# Strength    : fastest and no extra memory
# Limitation  : Writing operations are not optimized

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k  += 1
        return k
