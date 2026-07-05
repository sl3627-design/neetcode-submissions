class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd_max = 1
        even_min = float('inf')
        for key, value in count.items():
            if value%2 != 0:
                odd_max = max(odd_max, value)
            else:
                even_min = min(even_min, value)
        
        return odd_max - even_min