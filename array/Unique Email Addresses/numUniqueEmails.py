# Approach   : Built-In Functions
# Results    : runtime -> 7 ms, memory -> 18.06 MB
# Strength   : low space complexity O(n)
# Limitation : time consuming

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", '')
            normalized.add(local + "@" + domain)
        
        return len(normalized)
