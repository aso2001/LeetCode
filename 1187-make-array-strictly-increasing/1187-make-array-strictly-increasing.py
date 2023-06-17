class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = list(set(arr2))
        arr2.sort()

        dp = {-1:0}

        for i in range(len(arr1)):
            new_dp = defaultdict(lambda: math.inf)
            for prev in dp:
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
            dp = new_dp

        return min(dp.values()) if dp else -1