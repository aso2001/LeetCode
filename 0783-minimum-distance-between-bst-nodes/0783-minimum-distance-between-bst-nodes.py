# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # O(1) space solution
        prev = None
        mn = math.inf

        def inOrder(root):
            nonlocal mn, prev
            if not root:
                return
            inOrder(root.left)
            if prev:
                mn = min(mn, root.val - prev.val)
            prev = root
            inOrder(root.right)

        inOrder(root)
        return mn
    

    def minDiffInBST2(self, root: Optional[TreeNode]) -> int:
        # O(n) space and time solution
        res = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        mn = math.inf
        for i in range(1,len(res)):
            mn = min(mn, res[i] - res[i-1])
        return mn