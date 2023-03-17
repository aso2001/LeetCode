class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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