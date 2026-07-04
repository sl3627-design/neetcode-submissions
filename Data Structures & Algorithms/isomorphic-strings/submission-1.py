class Solution:
    def helper(self, s:str, t:str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] != t[i]:
                return False
            d[s[i]] = t[i]
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s,t) and self.helper(t,s)