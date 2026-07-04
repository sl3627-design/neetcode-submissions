class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        res = []
        for q in queries:
            count = 0
            for word in words[q[0]: q[1]+1]:
                if word[0] in vowels and word[-1] in vowels:
                    count += 1
            
            res.append(count)
        
        return res