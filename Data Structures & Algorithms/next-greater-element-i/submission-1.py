class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d = {}
        # for i in range (len(nums2) - 1):
        #     for j in range (i + 1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             d[nums2[i]] = nums2[j]
        #             break 
        #         else:
        #             d[nums2[i]] = -1
        
        # d[nums2[len(nums2) - 1]] = -1
        # res = []
        # for num in nums1:
        #     res.append(d[num])
        
        # return res


        nge = {}
        stack = []

        for x in nums2:
            while stack and stack[-1] < x:
                nge[stack.pop()] = x
            stack.append(x)

        for x in stack:
            nge[x] = -1
        
        return [nge[x] for x in nums1]


        


        