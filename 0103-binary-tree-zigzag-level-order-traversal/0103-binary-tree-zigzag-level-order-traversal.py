# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        if not root: return None
        q = deque([root])
        res, cnt = [[root.val]], 0
        while q:
            lev = []
            L = len(q)
            for i in range(L):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    lev.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    lev.append(cur.right.val)
            if not cnt%2:
                lev = lev[::-1]
            cnt += 1
            if lev:
                res.append(lev)
        return res