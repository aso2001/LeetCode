# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def preOrder(root):
            nonlocal res
            if not root:
                return
            if root and (not root.left and not root.right):
                res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
            return res
        
        res = []
        res1 = preOrder(root1)
        res = []
        res2 = preOrder(root2)
        return res1 == res2