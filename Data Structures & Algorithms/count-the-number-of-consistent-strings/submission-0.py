class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            word = set(word)
            if word.issubset(allowed):
                count += 1
        
        return count 