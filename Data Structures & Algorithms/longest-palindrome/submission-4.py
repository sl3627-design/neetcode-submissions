class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        
        l = 0
        b = False
        for key, value in d.items():
            if value % 2 == 0:
                l += value
            else:
                l += (value // 2)*2
                b = True
        if b:
            l += 1
        return(l)