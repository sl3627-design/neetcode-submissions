from collections import Counter
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
        # return self.CreateHash(s) == self.CreateHash(t)
        shash = Counter(s)
        thash = Counter(t)
        return shash == thash