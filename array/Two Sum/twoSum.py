# Approach    : Brute-Force
# Result      : runtime -> 2834ms, memory -> 18.58 MB
# Strength    : low memory use
# Limitation  : time consuming

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: List[int] = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                else:
                    j += 1
        return result
