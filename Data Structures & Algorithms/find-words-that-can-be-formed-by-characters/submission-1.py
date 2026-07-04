class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       count_c = collections.Counter(chars)
       count = 0
       for word in words:
            count_w = collections.Counter(word)
            if all(count_w[c] <= count_c[c] for c in count_w):
                count += len(word)
       return count