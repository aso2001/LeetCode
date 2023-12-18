# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preOrder(root):
            nonlocal res
            if not root:
                return
            res += str(root.val)

            if root.left or root.right:
                res += '('
                preOrder(root.left) 
                res += ')'

            if root.right:
                res += '('
                preOrder(root.right)  
                res += ')'

        res = '' 
        preOrder(root)
        return res