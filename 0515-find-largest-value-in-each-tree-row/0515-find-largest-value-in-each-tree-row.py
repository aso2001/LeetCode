# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        nxt = []
        mx = -math.inf
        res = []
        while True:
            while q:
                cur = q.pop()
                mx = max(mx, cur.val)
                if cur.left:
                    nxt.append(cur.left)
                if cur.right:
                    nxt.append(cur.right)
            if nxt:
                q = nxt.copy()
                nxt = []
                res.append(mx)
                mx = -math.inf
            else:
                res.append(mx)
                return res