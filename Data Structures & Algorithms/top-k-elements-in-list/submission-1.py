class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = {}
        # for n in nums:
        #     if n not in d:
        #         d[n] = 1
        #     else:
        #         d[n] += 1
        # sorted_items = sorted(d.items(), key = lambda x: x[1], reverse = True)

        # return [item[0] for item in sorted_items[:k]]

        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range (len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
            
