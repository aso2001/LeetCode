# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        def counter(root):
            if not root:
                return 0
            return 1 + counter(root.left) + counter(root.right)
        
        def search(root, x):
            if not root: 
                return None
            if root.val == x:
                return root
            return search(root.left, x) or search(root.right, x)

        xp = search(root, x)                # find pointer to x value Node
        xpl_cnt, xpr_cnt = 0, 0     
        xpl_cnt = counter(xp.left)          # count number of nodes in left and right branch
        xpr_cnt = counter(xp.right)
        rest = n - xpl_cnt - xpr_cnt - 1    # count for third branch
        if max(rest, xpl_cnt, xpr_cnt) < n/2: # To win the game the maximum branch should have at least half of the nodes
            return False
        return True