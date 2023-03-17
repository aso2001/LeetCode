# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return max(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))
        return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))