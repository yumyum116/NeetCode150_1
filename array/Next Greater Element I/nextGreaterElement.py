# Approach    : Linear scan
# Results     : runtime -> 195 ms, memory -> 17.91 MB
# Strength    : relatively low memory usage
# Limitation  : time consuming

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and j == len(nums2) - 1:
                    result.append(-1)
                    break
                elif nums1[i] == nums2[j]:
                    result.append(nums2[j])
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > result[i]:
                            result[i] = nums2[k]
                            break
                    else:
                        result[i] = -1
                        break
        return result
