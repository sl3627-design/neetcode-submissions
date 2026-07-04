class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countm = Counter(magazine)
        countr = Counter(ransomNote)

        for c in countr:
            if countm[c] < countr[c]:
                return False
        
        return True
