class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        if k == len(blocks):
            return Counter(blocks[:k])['W']
        for i in range(len(blocks) - k):
            count = Counter(blocks[i:i+k])['W']
            res = min(res, count)
        
        return res