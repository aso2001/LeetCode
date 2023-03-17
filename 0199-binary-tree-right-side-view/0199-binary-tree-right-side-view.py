# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        res = []
        q = []
        q.append(root)

        while q:
            lev = []
            res.append(q[-1].val)
            for cur in q:
                if cur.left:
                    lev.append(cur.left)
                if cur.right:
                    lev.append(cur.right)
            q = lev
        return res