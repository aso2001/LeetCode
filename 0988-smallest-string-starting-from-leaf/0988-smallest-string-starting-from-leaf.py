# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            nonlocal res, mn
            res = chr(ord('a') + root.val) + res
            if not root.left and not root.right:
                if len(res) < len(mn) or res[:len(mn)] != mn:
                    mn = min(mn, res)
                return mn
            if root.left:
                dfs(root.left)
                res = res[1:]
            if root.right:
                dfs(root.right)
                res = res[1:]

        mn = 'z'*9000
        res = ''
        dfs(root)
        return mn