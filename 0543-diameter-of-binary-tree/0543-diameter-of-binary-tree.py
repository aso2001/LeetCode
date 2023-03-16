# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return 0, 0
        
        diamL, heightL = self.dfs(root.left)
        diamR, heightR = self.dfs(root.right)
        diam = max(diamL, diamR, heightL + heightR)
        return diam, 1 + max(heightL, heightR)
        
# (1) the max diameter may paas through the root, or lie completely on one side of the tree (2) and (3)