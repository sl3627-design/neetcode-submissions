class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l, r = 0, len(s) - 1
        pal = []
        for c in s:
            if c.isalnum():
                pal.append(c)
        
        return pal == pal[::-1]