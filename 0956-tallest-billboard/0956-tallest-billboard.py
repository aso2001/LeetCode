class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def helper(half_rods):
            states = set()
            states.add((0, 0))
            for r in half_rods:
                new_states = set()
                for L, R in states:
                    new_states.add((L + r, R))
                    new_states.add((L, R + r))
                states |= new_states
                
            dp = {}
            for L, R in states:
                dp[L - R] = max(dp.get(L - R, 0), L)
            return dp

        n = len(rods)
        first_half = helper(rods[:n//2])
        second_half = helper(rods[n//2:])

        res = 0
        for diff in first_half:
            if -diff in second_half:
                res = max(res, first_half[diff] + second_half[-diff])
        return res