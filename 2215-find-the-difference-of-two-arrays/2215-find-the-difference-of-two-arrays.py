class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0, ans1, res = [], [], []
        dd0, dd1 = {}, {}
        for i in range(len(nums1)):
            if nums1[i] not in dd0:
                dd0[nums1[i]] = 1
        for i in range(len(nums2)):
            if nums2[i] not in dd1:
                dd1[nums2[i]] = 1
        for n1 in dd0:
            if n1 not in dd1:
                ans0.append(n1)
        for n2 in dd1:
            if n2 not in dd0:
                ans1.append(n2)
        return [ans0, ans1]