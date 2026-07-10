class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        numop = 0
        for value in count.values():
            if value == 1:
                return -1
            elif value % 6 == 0 or value % 3 == 0:
                numop += value // 3
            else:
                numop += value // 3 + 1
        
        return numop 