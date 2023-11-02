# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            nonlocal cnt
            if not root:
                return [0, 0]

            left = rec(root.left)
            right = rec(root.right)

            cur_sum = root.val + left[0] + right[0]
            cur_cnt = 1 + left[1] + right[1]

            if cur_sum // cur_cnt == root.val:
                cnt += 1
            return [cur_sum, cur_cnt]

        cnt = 0
        rec(root)
        return cnt