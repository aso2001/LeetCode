# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, mx, cnt):
            if not root:
                return cnt
            if root.val >= mx:
                cnt += 1
                mx = root.val
            cnt = dfs(root.left, mx, cnt)
            return dfs(root.right, mx, cnt)

        
        return dfs(root, -math.inf, 0)