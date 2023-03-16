# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur:
                q.append(cur.left)
                q.append(cur.right)
            else:
                while q:
                    if q.popleft():
                        return False
        return True

    def isCompleteTree1(self, root: Optional[TreeNode]) -> bool:
        # BFS solution (level order traversal) O(1) space
        q = deque([root])
        prevL = 0
        while q:
            L = len(q)
            flag = 0
            for i in range(L):
                cur = q.popleft()
                if (cur.left and flag) or (not cur.left and cur.right) or ((cur.left or cur.right) and 2*prevL > L):
                    # bail out if previous node right child is missing :: if right child exists but left child is missing :: next to last level is not complete 2*prevL > L
                    return False
                if not cur.right:  # mark missing right child
                    flag = 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            prevL = L
        return True