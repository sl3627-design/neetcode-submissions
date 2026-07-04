class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        low = min(nums); high = max(nums)
        res = []
        while low <= high:
            if low in d.keys():
                while d[low] > 0:
                    d[low] -= 1
                    res.append(low)
            low += 1
        
        return res
