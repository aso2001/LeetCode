# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if (p.val < q.val and p.val <= root.val <= q.val) or (q.val < p.val and q.val <= root.val <= p.val):
            return root
        elif (p.val < q.val and q.val < root.val) or (q.val < p.val and p.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val < q.val and p.val > root.val) or (q.val < p.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)