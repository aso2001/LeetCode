class Solution:
    def maxScore(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        
        def dfs(mask, op):
            if mask in dd:
                return dd[mask]
            
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue
                        
                    newMask = mask | (1 << i) | (1 << j)
                    score = op * math.gcd(nums[i], nums[j])
                    dd[mask] = max(dd[mask], score + dfs(newMask, op + 1))
            return dd[mask]
        
        return dfs(0, 1)