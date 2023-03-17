# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Optimal solution
        def dfs(root, res):
            if not root:
                return 0
            res = 10*res + root.val
            if not root.left and not root.right:
                return res
            return dfs(root.left, res) + dfs(root.right, res)

        res = 0
        return dfs(root, 0)

    
    def sumNumbers2(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal ss, res
            if not root.left and not root.right:
                tmp = int(''.join(res))
                ss += tmp
                res.pop()
            if root.left:
                res.append(str(root.left.val))
                dfs(root.left)
                if not root.right:
                    res.pop()
            if root.right:
                res.append(str(root.right.val))
                dfs(root.right)
                res.pop()

        ss = 0
        res = [str(root.val)]
        dfs(root)

        return ss