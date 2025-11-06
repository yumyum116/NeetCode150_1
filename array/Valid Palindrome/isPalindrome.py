# Approach    : Reverse String
# Result      : runtime -> 22 ms, memory -> 17.69 MB
# Strength    : low space complexity O(n)
# Limitation  : time consuming O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = list(str(x))
        flag = 0
        if x % 2 == 0:
            for i in range(int(len(num) / 2)):
                if num[i] == num[len(num) - i - 1]:
                    flag += 1
        else:
            for i in range(int(len(num) / 2)):
                if num[i] == num[len(num) - i - 1]:
                    flag += 1
        if flag == int(len(num) / 2):
            return True
        else:
            return False
