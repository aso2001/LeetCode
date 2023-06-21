class Solution:
    def minCost2(self, nums: List[int], cost: List[int]) -> int:
        # TLE
        mc = math.inf
        ss = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] != nums[j]:
                    ss += cost[j] * abs(nums[i] - nums[j])
            mc = min(mc, ss)
            ss = 0
        return mc

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_cost(base):
            return sum(abs(base - num) * c for num, c in zip(nums, cost))
        
        L, R = min(nums), max(nums)
        res = get_cost(nums[0])
        
        while L < R:
            mid = (L + R) // 2
            cost1 = get_cost(mid)
            cost2 = get_cost(mid + 1)
            res = min(cost1, cost2) 
            if cost1 > cost2:
                L = mid + 1
            else:
                R = mid       
        return res