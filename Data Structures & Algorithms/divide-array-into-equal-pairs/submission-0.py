class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = collections.Counter(nums)

        for key, value in d.items():
            if value % 2 != 0:
                return False

        return True