class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        sorted_items = sorted(d.items(), key = lambda x: x[1], reverse = True)

        return [item[0] for item in sorted_items[:k]]
        
        
            
