# Approach    :
# Results     :
# Strength    :
# Limitation  :

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        column_words = [[0]]
        for i in range(len(words)):
            for j in range(len(word[i])):
                if j == column_words[i][0]:
                    column_words[i].append(words[i][j])
                else:
                    column_words[i + 1].append([j, words[i][j]])
        for i in range(len(words)):
            if words[i] != column_words[i][1]:
                return False
        else:
            return True
