# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inOrder(root):
            nonlocal res
            if not root:
                return 0
            inOrder(root.left)
            res += (root.val if low <= root.val <= high else 0)
            inOrder(root.right)
            return res
            
        res = 0
        return inOrder(root)