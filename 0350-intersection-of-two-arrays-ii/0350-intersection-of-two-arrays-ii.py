class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dd1 = defaultdict(int)
        dd2 = defaultdict(int)
        for c in nums1:
            dd1[c] += 1
        for c in nums2:
            dd2[c] += 1
        res = []
        for d in dd1:
            res.extend(min(dd1[d], dd2[d])*[d])
        return res 