class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_t = Counter(text)
        count_b = Counter("balloon")

        res = len(text)
        for c in count_b:
            res = min(res, count_t[c] // count_b[c])
        return res