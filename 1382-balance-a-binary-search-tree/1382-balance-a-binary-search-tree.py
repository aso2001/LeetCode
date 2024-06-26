# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inOrder(root):
            nonlocal res
            if not root:
                return res
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        def build(L, R):
            if L <= R:
                mid = (L + R) // 2
                return TreeNode(res[mid], build(L, mid - 1), build(mid + 1, R))
                
        res = []
        inOrder(root)
        return build(0, len(res) - 1)