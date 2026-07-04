class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       count_c = collections.Counter(chars)
       count = 0
       for word in words:
            count_w = collections.Counter(word)
            mask = True
            for key, value in count_w.items():
                if key in count_c.keys() and value <= count_c[key]:
                    continue
                else:
                    mask = False
            if mask:
                count += len(word)
        
       return count