# Approach    : Sorting
# Results     : Runtime -> 19s, Memory -> 18.63 MB
# Strength    : no extra memory
# Limitation  : time consuming O(nlogn + mlogm) and may be space consuming O(1) or O(n + m) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = sorted(s)
        new_t = sorted(t)
        if len(s) == len(t):
            for i in range(len(s)):
                for j in range(len(t)):
                    if new_s[i] == new_t[j]:
                        i += 1
                        j += 1
                    else:
                        break
                if i == len(s) and j == len(t):
                    return True
                else:
                    break
        return False
