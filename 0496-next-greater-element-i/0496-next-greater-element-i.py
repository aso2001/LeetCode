class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dd = {}
        for i in range(len(nums1)): dd[nums1[i]] = i
        stack = []
        res = [-1]*len(nums1)

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                top = stack.pop()
                if top in dd:
                    res[dd[top]] = nums2[i]
            stack.append(nums2[i])
        return res