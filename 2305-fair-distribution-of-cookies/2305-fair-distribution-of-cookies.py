class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0]*k
        n = len(cookies)

        def dfs(i, cnt):
            if n - i < cnt:
                return math.inf
            if i == n:
                return max(child)
            
            res = math.inf
            for j in range(k):
                cnt -= int(child[j] == 0)
                child[j] += cookies[i]
                
                res = min(res, dfs(i + 1, cnt))

                child[j] -= cookies[i]
                cnt += int(child[j] == 0)
            return res
        
        return dfs(0, k)