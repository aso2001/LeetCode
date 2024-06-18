class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profile = [(0, 0)]
        for i in range(len(difficulty)):
            job_profile.append((profit[i], difficulty[i]))

        job_profile.sort(reverse=True)
        for i in range(len(job_profile) - 1):
            job_profile[i + 1] = (
                job_profile[i + 1][0],
                min(job_profile[i][1], job_profile[i + 1][1]),
            )

        net_profit = 0
        for ability in worker:
            L, R = 0, len(job_profile) - 1
            job_profit = 0
            while L <= R:
                mid = (L + R) // 2
                if job_profile[mid][1] <= ability:
                    job_profit = max(job_profit, job_profile[mid][0])
                    R = mid - 1
                else:
                    L = mid + 1
            net_profit += job_profit

        return net_profit