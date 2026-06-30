# Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # s = "".join(char for char in s if char.isalnum())
        # a, b = 0, len(s) - 1

        # while b >= a:
        #     if s[a] != s[b]:
        #         return False
        #     a += 1
        #     b -= 1
        
        # return True 
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True 