class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countm = Counter(magazine)
        for r in ransomNote:
            if r not in countm:
                return False
            if r in countm:
                countm[r] -= 1
        
        return all(x >= 0 for x in countm.values())
