class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = {i+1 for i in range(len(nums))}
        res = []
        for n in nums:
            if n in a:
                a.remove(n)
            elif n not in a:
                res.append(n)
        
        res.append(list(a)[0])
        return res
