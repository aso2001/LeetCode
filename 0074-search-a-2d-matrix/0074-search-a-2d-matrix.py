class Solution:
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search first ROW then COL. Time compexity O(log(m*n))
        # search row
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r)//2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                l = mid + 1
            else:
                break
        row = mid
        # search column
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r)//2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mx = matrix
        row = 0
        
        L, R = 0, len(mx) - 1
        while L <= R:
            mid  = (L + R) // 2
            if mx[mid][0] > target:
                R = mid - 1
            elif mx[mid][len(mx[0]) - 1] < target:
                L = mid + 1
            elif mx[mid][0] < target < mx[mid][len(mx[0]) - 1]:
                row = mid
                break
            elif mx[mid][0] == target or target == mx[mid][len(mx[0]) - 1]:
                return True

        L, R = 0, len(mx[0]) - 1
        while L <= R:
            mid = (L + R) // 2
            if mx[row][mid] > target:
                R = mid - 1
            elif mx[row][mid] < target:
                L = mid + 1
            else:
                return True
        return False