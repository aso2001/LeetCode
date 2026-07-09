class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        queryResult = [False] * len(queries)

        prevNum = nums[0]
        nums[0] = 0

        for i in range(1, len(nums)):
            if nums[i] - prevNum <= maxDiff:
                prevNum = nums[i]
                nums[i] = nums[i - 1] + 1
            else:
                prevNum = nums[i]
                nums[i] = 0

        for i in range(len(queries)):
            if abs(queries[i][0] - queries[i][1]) <= nums[max(queries[i][0], queries[i][1])]:
               queryResult[i] = True

        return queryResult