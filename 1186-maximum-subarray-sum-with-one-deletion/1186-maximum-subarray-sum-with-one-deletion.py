class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        a = arr
        ln = len(arr)

        if max(a) <= 0:
            return max(a)
        if ln == 1:
            return a[0]

        # skip, noskip = [0]*ln, [0]*ln
        res = -10**5
        skip_prev, noskip_prev = 0, 0
        for i in range(ln):
            noskip = max(a[i], noskip_prev + a[i])
            skip = max(skip_prev + a[i], noskip_prev)
            res = max(res, skip, noskip)
            skip_prev, noskip_prev = skip, noskip

            # noskip[i] = max(a[i], noskip[i-1] + a[i])
            # skip[i] = max(skip[i-1] + a[i], noskip[i-1])
            # res = max(res, skip[i], noskip[i])
        return res
