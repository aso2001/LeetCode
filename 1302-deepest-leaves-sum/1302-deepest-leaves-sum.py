# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        nxt = deque()
        prev = deque([root])
        while q:
            cur = q.popleft()
            if cur.left:
                nxt.append(cur.left)
            if cur.right:
                nxt.append(cur.right)
            if not q:
                if nxt:
                    prev = nxt.copy()
                    q = nxt
                    nxt = deque()
        res = 0
        for p in prev:
            res += p.val
        return res