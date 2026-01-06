# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        res = []
        while q:
            lq = len(q)
            slev = 0
            for i in range(lq):
                cur = q.popleft()
                slev += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(slev)
        
        mx = max(res)
        for i in range(len(res)):
            if  res[i] == mx:
                return i + 1