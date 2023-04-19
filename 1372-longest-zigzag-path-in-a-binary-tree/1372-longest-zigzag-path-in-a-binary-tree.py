# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def maxZigZag(node, res, direction):
            if not node:
                return res
            if direction == 0:
                l = maxZigZag(node.left, res + 1, 1)
                r = maxZigZag(node.left, 0, 0)
            else:
                r = maxZigZag(node.right, res + 1, 0) 
                l = maxZigZag(node.right, 0, 1)
            return max(r, l)

        res1 = maxZigZag(root, 0, 0)
        res2 = maxZigZag(root, 0, 1)
        return max(res1, res2) - 1