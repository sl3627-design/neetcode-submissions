class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []; n = len(nums)

        d = collections.Counter(nums)

        for key, value in d.items():
            if value > n // 3:
                res.append(key)
        
        return res