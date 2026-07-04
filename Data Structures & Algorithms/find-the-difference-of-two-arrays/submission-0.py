class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        res.append(self.helper(nums1, nums2))
        res.append(self.helper(nums2, nums1))

        return res

    def helper(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for n in nums1:
            if n not in nums2:
                res.append(n)
        
        return res