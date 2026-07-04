class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # vowels = ["a", "e", "i", "o", "u"]
        # res = []
        # for q in queries:
        #     count = 0
        #     for word in words[q[0]: q[1]+1]:
        #         if word[0] in vowels and word[-1] in vowels:
        #             count += 1
            
        #     res.append(count)
        
        # return res

        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        prefix = [0] * (n + 1)
        for i, w in enumerate(words):
            prefix[i + 1] = prefix[i] + (w[0] in vowels and w[-1] in vowels)
        return [prefix[r + 1] - prefix[l] for l, r in queries]