class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            if numbers[L] + numbers[R] < target:
                L += 1
            elif numbers[L] + numbers[R] > target:
                R -= 1
            else:
                return [L + 1, R + 1]


    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        # Brute force O(n^2) with some optimization 
        for i in range(len(numbers) - 1):
            if i + 2 < len(numbers) and numbers[i + 2] == numbers[i + 1] == numbers[i]:
                continue
            for j in range(i + 1, len(numbers)):
                if j + 2 < len(numbers) and numbers[j + 2] == numbers[j + 1] == numbers[j]:
                    continue
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]