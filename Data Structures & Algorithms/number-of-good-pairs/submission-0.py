class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        count = 0
        for key, value in d.items():
            if value >= 2:
                count += value*(value-1)//2
        
        return count