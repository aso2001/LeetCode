class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for a in nums1:
            if a in nums2 and a not in res:
                res.append(a) 
        #print(res)
        return res