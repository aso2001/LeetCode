# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([[root, 1, 0]])  #[node, num, lev]
        prevLev, prevNum = 0, 1
        while q:
            node, num, lev = q.popleft()

            if lev > prevLev:
                prevLev = lev
                prevNum = num

            res = max(res, num - prevNum + 1)
            if node.left:
                q.append([node.left, 2*num, lev + 1])
            if node.right:
                q.append([node.right, 2*num + 1, lev + 1])
        return res        