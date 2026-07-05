class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        for i in range(k):
            gifts[-1] = int(gifts[-1]**0.5)
            gifts.sort()
        
        return sum(gifts)