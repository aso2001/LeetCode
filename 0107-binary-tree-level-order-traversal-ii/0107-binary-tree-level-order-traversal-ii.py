# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return root
        q, res = deque([root]), [[root.val]]
        nxt0, nxt = deque(), []

        while True:
            while q:
                cur = q.popleft()
                if cur.left:
                    nxt0.append(cur.left)
                    nxt.append(cur.left.val)
                if cur.right:
                    nxt0.append(cur.right)
                    nxt.append(cur.right.val)
            if not nxt0:
                break
            q = nxt0
            res.append(nxt)
            nxt0, nxt = deque(), []

        L, R = 0, len(res) - 1
        while L < R:
            res[L], res[R] = res[R], res[L]
            R -= 1
            L += 1
        return res