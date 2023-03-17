# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = []
        def InOrder(root, res):
            if root is None:
                return res
            InOrder(root.left, res)
            res.append(root.val)
            InOrder(root.right, res)

        InOrder(root, res)

        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True