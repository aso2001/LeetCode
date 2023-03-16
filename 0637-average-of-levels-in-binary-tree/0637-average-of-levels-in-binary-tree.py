# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = [root]
        lev, lsum, lcnt = [], 0, 0
        res = [root.val]

        while True:
            while q:
                cur = q.pop()
                if cur.left:
                    lev.append(cur.left)
                    lsum += cur.left.val
                    lcnt += 1
                if cur.right:
                    lev.append(cur.right)
                    lsum += cur.right.val
                    lcnt += 1
            if not lev:
                return res
            res.append(lsum/lcnt)
            q = lev
            lev, lsum, lcnt = [], 0, 0     