# Approach    : String Parsing
# Results     : runtime -> 0 ms, memory -> 17.92 MB
# Strength    : fastest
# Limitation  : space consuming

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            phone_number = details[i][:9]
            gender = details[i][10:11]
            age = details[i][11:13]
            seat = details[i][13:]
            if int(age) > 60:
                count += 1
        return count
