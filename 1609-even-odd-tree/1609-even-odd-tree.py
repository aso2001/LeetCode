# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        lev = 1
        while q:
            prev = -math.inf if lev % 2 else math.inf
            length = len(q)
            for _ in range(length):
                cur = q.popleft()
                if lev % 2 and (cur.val <= prev or not cur.val % 2):
                    return False
                elif not lev % 2 and (cur.val >= prev or cur.val % 2):
                    return False
                prev = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            lev += 1
        return True