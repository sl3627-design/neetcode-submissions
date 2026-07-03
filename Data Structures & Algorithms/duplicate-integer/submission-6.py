from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        
        # d = set()
        # for n in nums:
        #     if n not in d:
        #         d.add(n)
        #     else:
        #         return True
        # return False