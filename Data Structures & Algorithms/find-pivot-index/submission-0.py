class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = [0] + nums + [0]
        for i in range(1, len(n)-1):
            if sum(n[:i]) == sum(n[i+1:]):
                return i-1
        
        return -1
