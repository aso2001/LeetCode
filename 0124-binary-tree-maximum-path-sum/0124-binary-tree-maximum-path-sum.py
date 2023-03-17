# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxSum(root):
            if not root:
                return 0, -math.inf
            
            maxL, wL = maxSum(root.left)
            maxR, wR = maxSum(root.right)
            maxL = max(maxL, 0)
            maxR = max(maxR, 0)

            res = max(wL, wR, root.val + maxL + maxR)  # total result = max(with split Right, w/s Left, without split )
            return root.val + max(maxL, maxR), res     # no split path, with split

        return maxSum(root)[1] 