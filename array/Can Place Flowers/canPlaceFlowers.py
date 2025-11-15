# Approach   : linear scan
# Results    : runtime -> 18 ms, memory -> 18.12 MB
# Strength   : relatively low memory consumption O(1)
# Limitation : time consuming and redundant

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if n == 1 and len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        
        count_zero = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                count_zero += 1
        if count_zero < n:
            return False
        
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i > 0 and i < len(flowerbed) - 1 :
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            if n == 0:
                return True
        return False
