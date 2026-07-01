class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        
        for key, value in res.items():
            if value > int(len(nums)/2):
                return key