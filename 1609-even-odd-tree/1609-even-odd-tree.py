# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root.val % 2: return False
        q = deque()
        nxt = deque()
        lev = 0
        q.append(root)
        while True:
            while q:
                cur = q.popleft()
                if cur.left:
                    nxt.append(cur.left)
                if cur.right:
                    nxt.append(cur.right)
            if not nxt:
                break
            prev = math.inf
            if lev % 2:
                prev -= prev
                for n in nxt:
                    if n.val <= prev or not n.val % 2:
                        return False
                    prev = n.val
            else:
                for n in nxt:
                    if n.val >= prev or n.val % 2:
                        return False
                    prev = n.val
            q = nxt.copy()
            nxt = deque()
            lev += 1
        return True