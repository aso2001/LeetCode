class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        def helper(requests, indee, n, idx, cnt):
            nonlocal res
            if idx == len(requests):
                for i in range(n):
                    if indee[i]:
                        return
                res = max(res, cnt)
                return
            
            indee[requests[idx][0]] -= 1
            indee[requests[idx][1]] += 1
            helper(requests, indee, n, idx + 1, cnt + 1)
            indee[requests[idx][0]] += 1
            indee[requests[idx][1]] -= 1
            
            helper(requests, indee, n, idx + 1, cnt)

        indee = [0]*n
        helper(requests, indee, n, 0, 0)
        return res