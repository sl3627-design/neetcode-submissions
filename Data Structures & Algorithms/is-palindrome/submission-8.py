# Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        a, b = 0, len(s) - 1

        while b >= a:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        
        return True 