class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        sn = (1 << n - 1) 
        dd = {}
        for i in range(len(req_skills)):
            dd[req_skills[i]] = i

        pp = [0]*len(people)
        for j in range(len(people)):
            for s in people[j]:
                i = dd[s]
                pp[j] |= (1 << i)

        dp = [-1]*(1 << n)
        dp[0] = 0

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            for p in range(len(people)):
                new_terget = i & (~pp[p])
                if new_terget != i:
                    p_msk = dfs(new_terget) | (1 << p)
                    if dp[i] == -1 or p_msk.bit_count() < dp[i].bit_count():
                        dp[i] = p_msk 
            return dp[i]

        tmp = dfs((1 << n) - 1)
        res = []
        for i in range(len(people)):
            if (tmp >> i) & 1:
                res.append(i)
        return res