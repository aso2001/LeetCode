class Solution:
    def minOperations(self, nums, targetSum):
        totalSum = sum(nums)
        target = totalSum - targetSum  # Calculate the target sum difference

        if target < 0:
            return -1  # Return -1 if target sum is not achievable

        if target == 0:
            return len(nums)  # Return the number of elements if target sum is 0

        n = len(nums)  # Number of elements in the list
        minOperations = float('inf')  # Minimum operations to achieve the target sum
        currentSum = 0  # Current sum of elements
        leftIndex = 0
        rightIndex = 0  # Pointers for the sliding window

        while rightIndex < n:
            currentSum += nums[rightIndex]
            rightIndex += 1

            while currentSum > target and leftIndex < n:
                currentSum -= nums[leftIndex]
                leftIndex += 1

            if currentSum == target:
                minOperations = min(minOperations, n - (rightIndex - leftIndex))

        return -1 if minOperations == float('inf') else minOperations  # Return the minimum operations or -1 if not possible
        # n = len(nums)
        # pfx, sfx = [0]*n, [0]*n

        # pfx[0] = nums[0]
        # for i in range(1, n):
        #     pfx[i] = pfx[i-1] + nums[i]
        
        # sfx[n-1] = nums[n-1]
        # for i in range(n-2, -1, -1):
        #     sfx[i] = sfx[i+1] + nums[i]

        # res = -1
        # for i in range(-1, n):
        #     if i == -1:
        #         start = 0
        #     else:
        #         start = pfx[i]
        #     if start > x:
        #         return res
        #     j = n
        #     sfxj = 0
        #     while start + sfxj < x and j > i:
        #         j -= 1
        #         sfxj = sfx[j]
        #     if start + sfxj == x:
        #         if res > 0:
        #             res = min(res, (i+1 if i >= 0 else 0) + (n - j))
        #         else:
        #             res = (i+1 if i >= 0 else 0) + (n - j)