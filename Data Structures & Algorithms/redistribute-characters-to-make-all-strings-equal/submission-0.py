class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()

        for word in words:
            counter += Counter(word)
        
        return all(k%len(words) == 0 for k in counter.values())