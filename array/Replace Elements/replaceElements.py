# Approach     : Brute-force
# Results      : runtime -> 0.75 sec, memory -> 52.6 MB
# Strength     : no extra memory
# Limitation   : time consuming with large data O(n^2)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        for i in range(n - 1):
            result[i] = arr[i + 1]
            for j in range(i + 1, n):
                if result[i] < arr[j]:
                    result[i] = arr[j]
        result[n - 1] = -1
        return result
