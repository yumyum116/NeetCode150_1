# Approach   : Dynamic Programming
# Results    : runtime -> 0.858sec, memory -> 52.2MB
# Strength   : intensive and understandable, and space complexity is O(n^2)
# Limitation : high time complexity when constant multiple

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangles = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    triangles[i].append(1)
                else:
                    triangles[i].append(int(triangles[i - 1][j - 1]) + int(triangles[i - 1][j]))
        return triangles
