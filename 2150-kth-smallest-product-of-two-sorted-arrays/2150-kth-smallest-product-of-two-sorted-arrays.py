class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Solution 1:
        def cnt(x):
            c = 0
            for a in nums1:
                if a > 0:
                    c += bisect_right(nums2, x // a)
                elif a < 0:
                    t = x // a + (1 if x % a else 0)
                    c += n2 - bisect_left(nums2, t)
                else:
                    if x >= 0:
                        c += n2
            return c

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1        
        n2 = len(nums2)
        lo = min(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        hi = max(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        while lo < hi:
            m = (lo + hi) // 2
            if cnt(m) >= k:
                hi = m
            else:
                lo = m + 1
        return lo