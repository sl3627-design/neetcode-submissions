class Solution:
    def CreateHash(self, s: str) -> dict:
        temp = {}
        for e in s:
            if e not in temp:
                temp[e] = 1
            else:
                temp[e] += 1
        return temp
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            return self.CreateHash(s) == self.CreateHash(t)