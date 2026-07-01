class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words.sort(key = len)
        for i in range (len(words)):
            for word in words[i+1:]:
                if words[i] in word and words[i] not in result:
                    result.append(words[i])

        return result
        