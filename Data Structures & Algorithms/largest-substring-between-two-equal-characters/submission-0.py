class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # keep track of characters seen and their indices
        # char -> first index
        char_index = {}
        res = -1

        for i, c in enumerate(s): 
            if c in char_index:
                res = max(res, i - char_index[c] - 1)
            else:
                char_index[c] = i
        return res

