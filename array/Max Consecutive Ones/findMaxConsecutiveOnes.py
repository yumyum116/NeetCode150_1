# Approach    : Linear scan
# Result      : runtime -> 0.907 sec, memory -> 51.9 MB
# Strength    : fast and low space complexity O(1)
# Limitation  : 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)
        return max(result)
