class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        if len(nums1) > len(nums2):
            if len(nums1) > len(nums2) * 6:
                return -1
        n1 = len(nums1)
        n2 = len(nums2)
        s1 = sum(nums1)
        s2 = sum(nums2)
        cnt = 0
        if s1 == s2:
            return cnt

        mx, mn = [], []
        if s2 > s1:
            nums1, nums2 = nums2, nums1
            s1, s2, n1, n2 = s2, s1, n2, n1
        nums1.sort()
        nums2.sort(reverse = True)
        for i in range(n1):
            if nums1[i] > 1:
                mx.append(nums1[i] - 1)
        for i in range(n2):
            if nums2[i] < 6:
                mn.append(6 - nums2[i])

        while s1 > s2:
            if mx and mn:
                if mx[-1] >= mn[-1]:
                    s1 -= mx.pop()
                else:
                    s2 += mn.pop()
            elif mx or mn:
                if mx:
                    s1 -= mx.pop()
                else:
                    s2 += mn.pop()
            cnt += 1
        return cnt